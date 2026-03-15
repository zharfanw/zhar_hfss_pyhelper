import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.NewProject()
oProject.InsertDesign("HFSS", "HFSSDesign1", "HFSS Terminal Network", "")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
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
					"NAME:subsrate_thickness",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.127mm"
				],
				[
					"NAME:copper_thickness",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "35um"
				],
				[
					"NAME:air_gap",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.02in"
				],
				[
					"NAME:lambda",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "7.89mm"
				],
				[
					"NAME:w_ind",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1.8mm"
				],
				[
					"NAME:the_L",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "2.7mm"
				],
				[
					"NAME:absolute_x",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0mm"
				],
				[
					"NAME:absolute_y",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0mm"
				],
                [
					"NAME:cell_length",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "2.367mm"
				],
				[
					"NAME:cell_width",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "2.367mm"
				]
			]
		]
	])

def create_uc_copper(oEditor,name_uc='unitcell_cond_',abs_x_mm=0,abs_y_mm=0,the_L=2.7,w_ind=1.8):
    firstBox_name=name_uc+"_1_"
    oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, str(abs_x_mm)+"mm"+"+(cell_length/2)-("+str(w_ind)+"mm"+"/2)",
		"YPosition:="		, str(abs_y_mm)+"mm"+"+(cell_length/2)-("+str(the_L)+"mm"+"/2)",
		"ZPosition:="		, "subsrate_thickness",
		"XSize:="		, str(w_ind)+"mm",
		"YSize:="		, str(the_L)+"mm",
		"ZSize:="		, "copper_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, firstBox_name,
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
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
    secondBox_name=name_uc+"_2_"
    oEditor.CreateBox(  
	[
		"NAME:BoxParameters",
		"XPosition:="		, str(abs_x_mm)+"mm"+"+(cell_length/2)-("+str(the_L)+"mm"+"/2)",
		"YPosition:="		, str(abs_y_mm)+"mm"+"+(cell_length/2)-("+str(w_ind)+"mm"+"/2)",
		"ZPosition:="		, "subsrate_thickness",
		"XSize:="		, str(the_L)+"mm",
		"YSize:="		, str(w_ind)+"mm",
		"ZSize:="		, "copper_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, secondBox_name,
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
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
    oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, firstBox_name+","+secondBox_name
	], 
	[
		"NAME:UniteParameters",
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
				firstBox_name
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

def create_substrate(oEditor,name_sub='substrate',width=3,length=3):
    oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "0mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, str(width)+"mm",
		"YSize:="		, str(length)+"mm",
		"ZSize:="		, "subsrate_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, name_sub,
		"Flags:="		, "",
		# "Color:="		, "(143 175 143)",
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
				name_sub
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
    

## Define MetaSurface Param
x_count=20
y_count=20

cell_length = 2.367
cell_width = 2.367

# create_uc_copper(oEditor)
# create_uc_copper(oEditor,name_uc='unitcell_cond_1',abs_x_mm=3,abs_y_mm=3)
# create_uc_copper(oEditor,name_uc='unitcell_cond_2',abs_x_mm=6,abs_y_mm=6)

create_substrate(oEditor,name_sub='substrate',width=cell_length*x_count,length=cell_length*x_count)

# for ix in range(x_count):
#     for iy in range(y_count):
#         create_uc_copper(oEditor, name_uc="uc_"+str(ix)+"_"+str(iy), abs_x_mm=cell_length*ix, abs_y_mm=cell_length*iy)
# oEditor = oDesign.SetActiveEditor("3D Modeler")

import csv

file_path = 'D:\matched_parameters_20x20.csv'


with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header row
    # print(f"Header: {header}")

    row_count = 0
    for row in reader:
        row_count += 1
        # You can process each 'row' here.
        # 'row' will be a list of strings representing the columns.
        # For demonstration, we'll just print the first few rows.
        ix=int(row[0])
        iy=int(row[1])
        the_L=float(row[3])
        w_ind=float(row[2])
        create_uc_copper(oEditor, name_uc="uc_"+str(row[0])+"_"+str(row[1]), abs_x_mm=cell_length*ix, abs_y_mm=cell_length*iy,the_L=the_L,w_ind=w_ind)
# 
        # if row_count <= 5:
        #     # print(f"Row {row_count}: {row}")
        #     create_uc_copper(oEditor, name_uc="uc_"+str(row[0])+"_"+str(row[1]), abs_x_mm=cell_length*ix, abs_y_mm=cell_length*iy)
# 
        # elif row_count == 100:
            # print(f"Row {row_count}: {row}")
        # elif row_count == 6:
            # print("... (truncated after 5 rows for brevity)")

    # print(f"\nSuccessfully read {row_count} rows from '{file_path}'.")
