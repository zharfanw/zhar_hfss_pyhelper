import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")

import math
import csv
# from dataclasses import dataclass, field
# from typing import Dict, List
# import matplotlib.pyplot as plt

# Definisi struct
# @dataclass
# class RowData:
#     frequency: float
#     dimensi: Dict[str, float] = field(default_factory=dict)
#     ang_deg: float = 0.0
class RowData(object):
    def __init__(self, frequency, dimensi, ang_deg):
        self.frequency = float(frequency)
        self.dimensi = dimensi
        self.ang_deg = float(ang_deg)

def helper_load_csv(filename, delimiter= ',', visualize= False):
    rows=[]

    # with open(filename, newline='', encoding='utf-8') as csvfile:
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        header = next(reader)  # ambil header
        clean_header = [h.split(" ")[0] for h in header]

        # cari index kolom
        freq_idx = 0
        ang_idx  = len(header) - 1
        dimensi_headers = clean_header[1:ang_idx]  # kolom tengah = dimensi

        for r in reader:
            frequency = float(r[freq_idx])
            ang_deg   = float(r[ang_idx])

            # ambil semua dimensi -> dict
            dimensi_dict = {}
            for i, col_name in enumerate(dimensi_headers, start=1):
                dimensi_dict[col_name] = float(r[i])

            row = RowData(frequency=frequency, dimensi=dimensi_dict, ang_deg=ang_deg)
            rows.append(row)

    # Jika minta visualisasi
    if visualize:
        # Contoh: ambil dimensi pertama untuk x-axis
        if dimensi_headers:
            x_vals = [row.dimensi[dimensi_headers[0]] for row in rows]
            y_vals = [row.frequency for row in rows]
            z_vals = [row.ang_deg for row in rows]

            plt.figure()
            sc = plt.scatter(x_vals, z_vals, c=y_vals, cmap="viridis")
            plt.colorbar(sc, label="Phase (deg)")
            plt.xlabel(dimensi_headers[0])
            plt.ylabel("Phase (deg)")
            plt.title("Dimension")
            plt.grid(True)
            plt.show()

    return rows


## Measurement in mm

# # Terminology
# uC = Unit cell
# xlenUc = Length of unit cell in X-axis
# ylenUc = Length of unit cell in Y-axis
# xorgUc = offset between origin of unit cell from global origin
# yorgUc = offset between origin of unit cell from global origin
# cUc = center of unit cell
# rUc = length between center of unit-cell to focal-point
# phuC = designed phase for unit cell

# # define dimension of Unit Cell
# xlenUc = 3
# ylenUc = 3

# # define Antenna array profile
# xnumUc = 15
# ynumUc = 15

# # f_0 = 38GHz, alpha_0 = 7.80mm,
# # define focal-point
# foc_x = (xnumUc*xlenUc)/2
# foc_y = (ynumUc*ylenUc)/2
# foc_z = 32 # 1cm
# f_0 = 38e9 # 38GHz

## Setup for 40x40uC, Ao = 120mm^2
# define dimension of Unit Cell
name_project="AntennaLensArray_BigRect"
name_design="AntennaGenerated_40uC_120mm"
xlenUc = 3
ylenUc = 3

# define Antenna array profile
xnumUc = 40
ynumUc = 40

# f_0 = 38GHz, alpha_0 = 7.80mm,
# define focal-point
foc_x = (xnumUc*xlenUc)/2
foc_y = (ynumUc*ylenUc)/2
foc_z = 60 # 6cm
f_0 = 38e9 # 38GHz

# =========================
# Wrap untuk RADIAN
# =========================
def wrap_rad_pos(rad):
    """Wrap ke [0, 2*pi)"""
    return rad % (2*math.pi)

def wrap_rad_sym(rad):
    """Wrap ke [-pi, pi)"""
    return (rad + math.pi) % (2*math.pi) - math.pi

# =========================
# Wrap untuk DEGREE
# =========================
def wrap_deg_pos(deg):
    """Wrap ke [0, 360)"""
    return deg % 360

def wrap_deg_sym(deg):
    """Wrap ke [-180, 180)"""
    return (deg + 180) % 360 - 180


def generate_alpha(f_0):
    c=3e8 # 300 x 10^6 m/s
    alpha_0 = c/f_0
    return alpha_0
def generate_alpha_mm(f_0):
    alpha_0_mm = generate_alpha(f_0)*1000
    return alpha_0_mm

def generate_phase(dist_uc_to_focal,dist_ant_to_docal,f_0):
    alpha_0 = generate_alpha_mm(f_0)
    temp_form = math.sqrt(dist_uc_to_focal**2+dist_ant_to_docal**2)
    phase_rad = (2*math.pi/alpha_0)*(temp_form-dist_ant_to_docal)
    return phase_rad

def generate_phase_deg(dist_uc_to_focal,dist_ant_to_docal,f_0):
    phase_rad = generate_phase(dist_uc_to_focal,dist_ant_to_docal,f_0)
    return math.degrees(phase_rad)

def generateUnitCell(oDesign,oEditor,xorgUc,yorgUc,xlenUc,ylenUc,param_1,index):
    # RingPosition
    x_rect_pos = xorgUc+(xlenUc/2)-(param_1/2)
    y_rect_pos = yorgUc+(ylenUc/2)-(param_1/2)

    # Bottom Layer
    oEditor.CreateBox(
        [
            "NAME:BoxParameters",
            "XPosition:="		, str(xorgUc)+"mm",
            "YPosition:="		, str(yorgUc)+"mm",
            "ZPosition:="		, "0mm",
            "XSize:="		, "xlenUc",
            "YSize:="		, "xlenUc",
            "ZSize:="		, "cond_thickness"
        ], 
        [
            "NAME:Attributes",
            "Name:="		, "BottomRing"+str(index),
            "Flags:="		, "",
            "Color:="		, "(143 175 143)",
            "Transparency:="	, 0,
            "PartCoordinateSystem:=", "Global",
            "UDMId:="		, "",
            "MaterialValue:="	, "\"copper\"",
            "SurfaceMaterialValue:=", "\"\"",
            "SolveInside:="		, False,
            "ShellElement:="	, False,
            "ShellElementThickness:=", "nan ",
            "ReferenceTemperature:=", "nan ",
            "IsMaterialEditable:="	, True,
            "UseMaterialAppearance:=", True,
            "IsLightweight:="	, False
        ])
    oEditor.CreateBox(
        [
            "NAME:BoxParameters",
            "XPosition:="		, str(xorgUc)+"mm"+"+outer_ring_width/2",
            "YPosition:="		, str(yorgUc)+"mm"+"+outer_ring_width/2",
            "ZPosition:="		, "0mm",
            "XSize:="		, "xlenUc-outer_ring_width",
            "YSize:="		, "ylenUc-outer_ring_width",
            "ZSize:="		, "cond_thickness"
        ], 
        [
            "NAME:Attributes",
            "Name:="		, "BottomRingTool"+str(index),
            "Flags:="		, "",
            "Color:="		, "(143 175 143)",
            "Transparency:="	, 0,
            "PartCoordinateSystem:=", "Global",
            "UDMId:="		, "",
            "MaterialValue:="	, "\"vacuum\"",
            "SurfaceMaterialValue:=", "\"\"",
            "SolveInside:="		, True,
            "ShellElement:="	, False,
            "ShellElementThickness:=", "0mm",
            "ReferenceTemperature:=", "20cel",
            "IsMaterialEditable:="	, True,
            "UseMaterialAppearance:=", False,
            "IsLightweight:="	, False
        ])
    oEditor.Subtract(
        [
            "NAME:Selections",
            "Blank Parts:="		, "BottomRing"+str(index),
            "Tool Parts:="		, "BottomRingTool"+str(index)
        ], 
        [
            "NAME:SubtractParameters",
            "KeepOriginals:="	, False,
            "TurnOnNBodyBoolean:="	, True
        ])
    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Geometry3DAttributeTab",
                [
                    "NAME:PropServers", 
                    "BottomRing"+str(index),
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Material Appearance",
                        "Value:="		, True
                    ]
                ]
            ]
        ])
    oEditor.CreateBox(
        [
            "NAME:BoxParameters",
            "XPosition:="		, str(x_rect_pos)+"mm",
            "YPosition:="		, str(y_rect_pos)+"mm",
            "ZPosition:="		, "0mm",
            "XSize:="		, str(param_1)+"mm",
            "YSize:="		, str(param_1)+"mm",
            "ZSize:="		, "cond_thickness"
        ], 
        [
            "NAME:Attributes",
            "Name:="		, "BottomRect"+str(index),
            "Flags:="		, "",
            "Color:="		, "(143 175 143)",
            "Transparency:="	, 0,
            "PartCoordinateSystem:=", "Global",
            "UDMId:="		, "",
            "MaterialValue:="	, "\"copper\"",
            "SurfaceMaterialValue:=", "\"\"",
            "SolveInside:="		, False,
            "ShellElement:="	, False,
            "ShellElementThickness:=", "nan",
            "ReferenceTemperature:=", "nan ",
            "IsMaterialEditable:="	, True,
            "UseMaterialAppearance:=", True,
            "IsLightweight:="	, False
        ])
    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Geometry3DAttributeTab",
                [
                    "NAME:PropServers", 
                    "BottomRect"+str(index)
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Material Appearance",
                        "Value:="		, True
                    ]
                ]
            ]
        ])

    # Substrate Layer
    oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, str(xorgUc)+"mm+"+"0mm",
		"YPosition:="		, str(yorgUc)+"mm+"+"0mm",
		"ZPosition:="		, "cond_thickness",
		"XSize:="		, "xlenUc",
		"YSize:="		, "ylenUc",
		"ZSize:="		, "substrate_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Subtrate_"+str(index),
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"Rogers RT/duroid 5880 (tm)\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "nan ",
		"ReferenceTemperature:=", "nan ",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Geometry3DAttributeTab",
                [
                    "NAME:PropServers", 
                    "Subtrate_"+str(index),
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Material Appearance",
                        "Value:="		, True
                    ]
                ]
            ]
        ])


    # Create Upper Layer
    oEditor.CreateBox(
        [
            "NAME:BoxParameters",
            "XPosition:="		, str(xorgUc)+"mm"+"+0mm",
            "YPosition:="		, str(yorgUc)+"mm"+"+0mm",
            "ZPosition:="		, "substrate_thickness+cond_thickness",
            "XSize:="		, "xlenUc",
            "YSize:="		, "ylenUc",
            "ZSize:="		, "cond_thickness"
        ], 
        [
            "NAME:Attributes",
            "Name:="		, "UpperRing"+str(index),
            "Flags:="		, "",
            "Color:="		, "(143 175 143)",
            "Transparency:="	, 0,
            "PartCoordinateSystem:=", "Global",
            "UDMId:="		, "",
            "MaterialValue:="	, "\"copper\"",
            "SurfaceMaterialValue:=", "\"\"",
            "SolveInside:="		, False,
            "ShellElement:="	, False,
            "ShellElementThickness:=", "nan ",
            "ReferenceTemperature:=", "nan ",
            "IsMaterialEditable:="	, True,
            "UseMaterialAppearance:=", True,
            "IsLightweight:="	, False
        ])
    oEditor.CreateBox(
        [
            "NAME:BoxParameters",
            "XPosition:="		, str(xorgUc)+"mm"+"+outer_ring_width/2",
            "YPosition:="		, str(yorgUc)+"mm"+"+outer_ring_width/2",
            "ZPosition:="		, "substrate_thickness+cond_thickness",
            "XSize:="		, "xlenUc-outer_ring_width",
            "YSize:="		, "ylenUc-outer_ring_width",
            "ZSize:="		, "cond_thickness"
        ], 
        [
            "NAME:Attributes",
            "Name:="		, "UpperRingTool"+str(index),
            "Flags:="		, "",
            "Color:="		, "(143 175 143)",
            "Transparency:="	, 0,
            "PartCoordinateSystem:=", "Global",
            "UDMId:="		, "",
            "MaterialValue:="	, "\"vacuum\"",
            "SurfaceMaterialValue:=", "\"\"",
            "SolveInside:="		, True,
            "ShellElement:="	, False,
            "ShellElementThickness:=", "0mm",
            "ReferenceTemperature:=", "20cel",
            "IsMaterialEditable:="	, True,
            "UseMaterialAppearance:=", False,
            "IsLightweight:="	, False
        ])
    oEditor.Subtract(
        [
            "NAME:Selections",
            "Blank Parts:="		, "UpperRing"+str(index),
            "Tool Parts:="		, "UpperRingTool"+str(index)
        ], 
        [
            "NAME:SubtractParameters",
            "KeepOriginals:="	, False,
            "TurnOnNBodyBoolean:="	, True
        ])
    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Geometry3DAttributeTab",
                [
                    "NAME:PropServers", 
                    "UpperRing"+str(index)
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Material Appearance",
                        "Value:="		, True
                    ]
                ]
            ]
        ])
    oEditor.CreateBox(
        [
            "NAME:BoxParameters",
            "XPosition:="		, str(x_rect_pos)+"mm",
            "YPosition:="		, str(y_rect_pos)+"mm",
            "ZPosition:="		, "substrate_thickness+cond_thickness",
            "XSize:="		, str(param_1)+"mm",
            "YSize:="		, str(param_1)+"mm",
            "ZSize:="		, "cond_thickness"
        ], 
        [
            "NAME:Attributes",
            "Name:="		, "UpperRect"+str(index),
            "Flags:="		, "",
            "Color:="		, "(143 175 143)",
            "Transparency:="	, 0,
            "PartCoordinateSystem:=", "Global",
            "UDMId:="		, "",
            "MaterialValue:="	, "\"copper\"",
            "SurfaceMaterialValue:=", "\"\"",
            "SolveInside:="		, False,
            "ShellElement:="	, False,
            "ShellElementThickness:=", "nan",
            "ReferenceTemperature:=", "nan ",
            "IsMaterialEditable:="	, True,
            "UseMaterialAppearance:=", True,
            "IsLightweight:="	, False
        ])
    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Geometry3DAttributeTab",
                [
                    "NAME:PropServers", 
                    "UpperRect"+str(index),
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Material Appearance",
                        "Value:="		, True
                    ]
                ]
            ]
        ])


oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject(name_project)
oProject.InsertDesign("HFSS", name_design, "HFSS Terminal Network", "")
oDesign = oProject.SetActiveDesign(name_design)
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:substrate_thickness",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.787mm"
				],
				[
					"NAME:cond_thickness",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "17um"
				],
				[
					"NAME:top_length",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1.5mm"
				],
                [
					"NAME:outer_ring_width",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.1mm"
				],
                [
					"NAME:xlenUc",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "3mm"
				],
				[
					"NAME:ylenUc",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "3mm"
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")



# bangun profil unit-cell (2D grid)
unitcell_profile = []
current_index = 0
current_xorgUc = 0
current_yorgUc = 0

for_viz = []
for_viz_phase = []
for_viz_b_phase = []


database_Uc = helper_load_csv("D:\Master_NSYSU\CodeRepository_ThisPeriod\zhar_antenna_design\py_helper\data.csv", delimiter=",", visualize=False)

for iy in range(ynumUc):
    current_xorgUc = 0

    curr_x = []
    curr_x_phase = []
    curr_x_b_phase = []
    for ix in range(xnumUc):
        cUcx = current_xorgUc+(xlenUc/2)
        cUcy = current_yorgUc+(ylenUc/2)
        rUc = math.sqrt(math.pow(foc_x-cUcx,2)+math.pow(foc_y-cUcy,2))

        # phase_uc
        phase_Uc = generate_phase_deg(rUc,foc_z,f_0)
        phase_Uc = wrap_deg_sym(phase_Uc)
        
        # get possible Phase from Simulation
        best_ph = None
        best_Uc = None
        bef_err = 999
        for dat_uC in database_Uc:
            curr_err = abs(phase_Uc - dat_uC.ang_deg)
            if(curr_err < bef_err):
                best_ph = dat_uC.ang_deg
                best_Uc = dat_uC
                bef_err = curr_err
        

        # Generate Single Profile
        # rUc = math.sqrt()
        unitcell_profile.append({
            "index" : current_index,
            "x_index":ix,
            "y_index":iy,    
            "x_org_uc":current_xorgUc,
            "y_org_uc":current_yorgUc,
            "r_Uc":rUc,
            "phase_Uc":phase_Uc,
            "sel_phase":best_ph,
            "design_uC":best_Uc
        })
        current_index = current_index+1
        current_xorgUc = current_xorgUc + xlenUc

        curr_x.append(rUc)
        curr_x_phase.append(phase_Uc)
        curr_x_b_phase.append(best_ph)

    for_viz.append(curr_x)
    for_viz_phase.append(curr_x_phase)
    for_viz_b_phase.append(curr_x_b_phase)
    current_yorgUc = current_yorgUc + ylenUc
    

# tampilkan hasil
for row in unitcell_profile:
    # print(row)
    # print(row["index"]," -> ")
    # print("Generate Cell")
    generateUnitCell(oDesign,oEditor,row["x_org_uc"],row["y_org_uc"],xlenUc,ylenUc,row["design_uC"].dimensi["top_length"],row['index'])

# generateUnitCell(oDesign,oEditor,0,0,3,3,0.1,0)
# for i in range(1, 2):
#     generateUnitCell(oDesign,oEditor,3*i,3*i,3,3,0.1*i,i)





# # Visualization only
# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()
# # Plot tile
# cax = ax.imshow(for_viz, origin='lower', cmap='plasma')

# # Tambah colorbar
# cbar = fig.colorbar(cax, ax=ax)
# cbar.set_label("distance[mm]")

# # Label axis
# ax.set_xlabel("X index (column)")
# ax.set_ylabel("Y index (row)")
# ax.set_title("Distance between Unit-cell to focal Point[mm] Tile Plot")

# fig2, ax2 = plt.subplots()
# # Plot tile
# cax2 = ax2.imshow(for_viz_phase, origin='lower', cmap='plasma')

# # Tambah colorbar
# cbar2 = fig2.colorbar(cax2, ax=ax2)
# cbar2.set_label("Phase[deg]")

# # Label axis
# ax2.set_xlabel("X index (column)")
# ax2.set_ylabel("Y index (row)")
# ax2.set_title("Phase Distribution on Tile Plot")

# fig3, ax3 = plt.subplots()
# # Plot tile
# cax3 = ax3.imshow(for_viz_b_phase, origin='lower', cmap='plasma')

# # Tambah colorbar
# cbar3 = fig2.colorbar(cax3, ax=ax3)
# cbar3.set_label("Phase[deg]")

# # Label axis
# ax3.set_xlabel("X index (column)")
# ax3.set_ylabel("Y index (row)")
# ax3.set_title("Sel Phase Distribution on Tile Plot")

# plt.show()