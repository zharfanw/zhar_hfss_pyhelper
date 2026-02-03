# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2024.1.0
# 9:31:02  Jan 05, 2026
# ----------------------------------------------



def mils2mm(val):
	return val*0.0254

def mm2mils(val):
	return val*39.3701

## Create Metasurface 2x2
unit_cell_x=33
unit_cell_y=33
cell_length = 2.367 # mm
cell_width = 2.367 # mm
cell_length_str = str(cell_length)+"mm"
cell_width_str = str(cell_width)+"mm"
size_w_ind=0.3945

## Generate Cap_layer1
# Create First cap1

# for iy in range(unit_cell_y):
# 	for ix in range(unit_cell_x):
# 		set_current_cell(ix, iy)
# 		build_unit_cell()

import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
# oProject = oDesktop.SetActiveProject("Project8")
# oDesign = oProject.SetActiveDesign("HFSSDesign3")
oProject = oDesktop.NewProject()
oDesign = oProject.InsertDesign("HFSS", "HFSSDesign1", "HFSS Terminal Network", "")

oEditor = oDesign.SetActiveEditor("3D Modeler")

def generate_local_variable(oProject,oEditor,oDesign):
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
						"Value:="		, "10mil"
					],
					[
						"NAME:substrate_pp",
						"PropType:="		, "VariableProp",
						"UserDef:="		, True,
						"Value:="		, "4mil"
					],
					[
						"NAME:lambda",
						"PropType:="		, "VariableProp",
						"UserDef:="		, True,
						"Value:="		, "7.89mm"
					],
					[
						"NAME:top_length",
						"PropType:="		, "VariableProp",
						"UserDef:="		, True,
						"Value:="		, "1.5mm"
					],
					[
						"NAME:top_length_2",
						"PropType:="		, "VariableProp",
						"UserDef:="		, True,
						"Value:="		, "1.9mm"
					],
					[
						"NAME:top_length_3",
						"PropType:="		, "VariableProp",
						"UserDef:="		, True,
						"Value:="		, "2.1mm"
					],
					[
						"NAME:copper_thickness",
						"PropType:="		, "VariableProp",
						"UserDef:="		, True,
						"Value:="		, "35um"
					],
					[
						"NAME:w_ind",
						"PropType:="		, "VariableProp",
						"UserDef:="		, True,
						"Value:="		, "0.3945mm"
					],
					[
						"NAME:cell_length",
						"PropType:="		, "VariableProp",
						"UserDef:="		, True,
						"Value:="		, "0.3*lambda"
					],
					[
						"NAME:cell_width",
						"PropType:="		, "VariableProp",
						"UserDef:="		, True,
						"Value:="		, "0.3*lambda"
					],
					[
						"NAME:current_x_cell",
						"PropType:="		, "VariableProp",
						"UserDef:="		, True,
						"Value:="		, "0mm"
					],
					[
						"NAME:current_y_cell",
						"PropType:="		, "VariableProp",
						"UserDef:="		, True,
						"Value:="		, "0mm"
					]
				]
			]
		])


def create_cond(oProject,oEditor,oDesign,name_cap,position_x,position_y,position_z,size_x,size_y):
	oEditor = oDesign.SetActiveEditor("3D Modeler")
	oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, str(position_x)+"mm",
		"YPosition:="		, str(position_y)+"mm",
		"ZPosition:="		, str(position_z)+"mm",
		"XSize:="		, str(size_x)+"mm",
		"YSize:="		, str(size_y)+"mm",
		"ZSize:="		, "copper_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, name_cap,
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
	oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				name_cap
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

def create_cap1(oProject,oEditor,oDesign,name_cap,position_grid_x,position_grid_y,size_patch):
	oEditor = oDesign.SetActiveEditor("3D Modeler")
	oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, str(position_grid_x*cell_length+((cell_length-size_patch)/2))+"mm",
		"YPosition:="		, str(position_grid_y*cell_width+((cell_width-size_patch)/2))+"mm",
		"ZPosition:="		, str(0)+"mm",
		"XSize:="		, str(size_patch)+"mm",
		"YSize:="		, str(size_patch)+"mm",
		"ZSize:="		, "copper_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, name_cap,
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
	oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				name_cap
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

def create_cap2(oProject,oEditor,oDesign,name_cap,position_grid_x,position_grid_y,size_patch):
	oEditor = oDesign.SetActiveEditor("3D Modeler")
	oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, str(position_grid_x*cell_length+((cell_length-size_patch)/2))+"mm",
		"YPosition:="		, str(position_grid_y*cell_width+((cell_width-size_patch)/2))+"mm",
		"ZPosition:="		, "copper_thickness+substrate_pp+copper_thickness+substrate_pp",
		"XSize:="		, str(size_patch)+"mm",
		"YSize:="		, str(size_patch)+"mm",
		"ZSize:="		, "copper_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, name_cap,
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
	oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				name_cap
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

def create_cap3(oProject,oEditor,oDesign,name_cap,position_grid_x,position_grid_y,size_patch):
	oEditor = oDesign.SetActiveEditor("3D Modeler")
	oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, str(position_grid_x*cell_length+((cell_length-size_patch)/2))+"mm",
		"YPosition:="		, str(position_grid_y*cell_width+((cell_width-size_patch)/2))+"mm",
		"ZPosition:="		, "copper_thickness+substrate_pp+copper_thickness+substrate_pp+copper_thickness+substrate_thickness+copper_thickness+substrate_pp",
		"XSize:="		, str(size_patch)+"mm",
		"YSize:="		, str(size_patch)+"mm",
		"ZSize:="		, "copper_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, name_cap,
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
	oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				name_cap
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


def create_ind1(oProject,oEditor,oDesign,name_ind,position_grid_x,size_w_ind,max_cell_length):
	oEditor = oDesign.SetActiveEditor("3D Modeler")
	oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, str(cell_length*position_grid_x+((cell_length-size_w_ind)/2))+"mm",
		"YPosition:="		, str(0)+"mm",
		"ZPosition:="		, "substrate_pp+copper_thickness",
		"XSize:="		, str(size_w_ind)+"mm",
		"YSize:="		, str(max_cell_length)+"mm",
		"ZSize:="		, "copper_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, name_ind,
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
	oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				name_ind
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

def create_ind1(oProject,oEditor,oDesign,name_ind,position_grid_x,size_w_ind,max_cell_length):
	oEditor = oDesign.SetActiveEditor("3D Modeler")
	oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, str(cell_length*position_grid_x+((cell_length-size_w_ind)/2))+"mm",
		"YPosition:="		, str(0)+"mm",
		"ZPosition:="		, "substrate_pp+copper_thickness",
		"XSize:="		, str(size_w_ind)+"mm",
		"YSize:="		, str(max_cell_length)+"mm",
		"ZSize:="		, "copper_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, name_ind,
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
	oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				name_ind
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

def create_indcross1(oProject,oEditor,oDesign,name_ind,position_grid_y,size_w_ind,max_cell_length):
	oEditor = oDesign.SetActiveEditor("3D Modeler")
	oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, str(0)+"mm",
		"YPosition:="		, str(cell_length*position_grid_y+((cell_length-size_w_ind)/2))+"mm",
		"ZPosition:="		, "substrate_pp+copper_thickness",
		"XSize:="		, str(max_cell_length)+"mm",
		"YSize:="		, str(size_w_ind)+"mm",
		"ZSize:="		, "copper_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, name_ind,
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
	oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				name_ind
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


def create_indcross1(oProject,oEditor,oDesign,name_ind,position_grid_y,size_w_ind,max_cell_length):
	oEditor = oDesign.SetActiveEditor("3D Modeler")
	oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, str(0)+"mm",
		"YPosition:="		, str(cell_length*position_grid_y+((cell_length-size_w_ind)/2))+"mm",
		"ZPosition:="		, "substrate_pp+copper_thickness",
		"XSize:="		, str(max_cell_length)+"mm",
		"YSize:="		, str(size_w_ind)+"mm",
		"ZSize:="		, "copper_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, name_ind,
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
	oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				name_ind
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

def create_ind2(oProject,oEditor,oDesign,name_ind,position_grid_x,size_w_ind,max_cell_length):
	oEditor = oDesign.SetActiveEditor("3D Modeler")
	oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, str(cell_length*position_grid_x+((cell_length-size_w_ind)/2))+"mm",
		"YPosition:="		, str(0)+"mm",
		"ZPosition:="		, "copper_thickness+substrate_pp+copper_thickness+substrate_pp+copper_thickness+substrate_thickness",
		"XSize:="		, str(size_w_ind)+"mm",
		"YSize:="		, str(max_cell_length)+"mm",
		"ZSize:="		, "copper_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, name_ind,
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
	oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				name_ind
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

def create_indcross2(oProject,oEditor,oDesign,name_ind,position_grid_y,size_w_ind,max_cell_length):
	oEditor = oDesign.SetActiveEditor("3D Modeler")
	oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, str(0)+"mm",
		"YPosition:="		, str(cell_length*position_grid_y+((cell_length-size_w_ind)/2))+"mm",
		"ZPosition:="		, "copper_thickness+substrate_pp+copper_thickness+substrate_pp+copper_thickness+substrate_thickness",
		"XSize:="		, str(max_cell_length)+"mm",
		"YSize:="		, str(size_w_ind)+"mm",
		"ZSize:="		, "copper_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, name_ind,
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
	oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				name_ind
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

def create_ind3(oProject,oEditor,oDesign,name_ind,position_grid_x,size_w_ind,max_cell_length):
	oEditor = oDesign.SetActiveEditor("3D Modeler")
	oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, str(cell_length*position_grid_x+((cell_length-size_w_ind)/2))+"mm",
		"YPosition:="		, str(0)+"mm",
		"ZPosition:="		, "copper_thickness*3+substrate_pp*2+substrate_thickness+copper_thickness*2+substrate_pp*2",
		"XSize:="		, str(size_w_ind)+"mm",
		"YSize:="		, str(max_cell_length)+"mm",
		"ZSize:="		, "copper_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, name_ind,
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
	oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				name_ind
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

def create_indcross3(oProject,oEditor,oDesign,name_ind,position_grid_y,size_w_ind,max_cell_length):
	oEditor = oDesign.SetActiveEditor("3D Modeler")
	oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, str(0)+"mm",
		"YPosition:="		, str(cell_length*position_grid_y+((cell_length-size_w_ind)/2))+"mm",
		"ZPosition:="		, "copper_thickness*3+substrate_pp*2+substrate_thickness+copper_thickness*2+substrate_pp*2",
		"XSize:="		, str(max_cell_length)+"mm",
		"YSize:="		, str(size_w_ind)+"mm",
		"ZSize:="		, "copper_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, name_ind,
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
	oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				name_ind
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



# create_cap1(
# 	oProject=oProject,
# 	oEditor=oEditor,
# 	oDesign=oDesign,
# 	name_cap="layer1cap1",
# 	position_grid_x=0,
# 	position_grid_y=0,
# 	size_patch=1.5
# )
# create_cap1(
# 	oProject=oProject,
# 	oEditor=oEditor,
# 	oDesign=oDesign,
# 	name_cap="layer1cap2",
# 	position_grid_x=1,
# 	position_grid_y=1,
# 	size_patch=1.5
# )
# create_ind1(
# 	oProject=oProject,
# 	oEditor=oEditor,
# 	oDesign=oDesign,
# 	name_ind="layer2_ind1",
# 	position_grid_x=0,
# 	size_w_ind=0.3945,
# 	max_cell_length=cell_length*2
# )
# create_ind1(
# 	oProject=oProject,
# 	oEditor=oEditor,
# 	oDesign=oDesign,
# 	name_ind="layer2_ind2",
# 	position_grid_x=1,
# 	size_w_ind=0.3945,
# 	max_cell_length=cell_length*2
# )
# create_indcross1(
# 	oProject=oProject,
# 	oEditor=oEditor,
# 	oDesign=oDesign,
# 	name_ind="layer2_indcross1",
# 	position_grid_y=0,
# 	size_w_ind=0.3945,
# 	max_cell_length=cell_length*2
# )
# create_indcross1(
# 	oProject=oProject,
# 	oEditor=oEditor,
# 	oDesign=oDesign,
# 	name_ind="layer2_indcross2",
# 	position_grid_y=1,
# 	size_w_ind=0.3945,
# 	max_cell_length=cell_length*2
# )


generate_local_variable(oProject,oEditor,oDesign)

## Create Layer 1
patch_layer1=1.5
layer1_cap_index=0
for iy in range(unit_cell_y):
	for ix in range(unit_cell_x):
		create_cap1(
			oProject=oProject,
			oEditor=oEditor,
			oDesign=oDesign,
			name_cap="layer1cap"+str(layer1_cap_index),
			position_grid_x=ix,
			position_grid_y=iy,
			size_patch=patch_layer1
		)
		layer1_cap_index = layer1_cap_index+1

## Create Dielectric 1

## Create Layer 2
layer2_ind_index=0
meta_length = cell_length*unit_cell_x

for ix in range(unit_cell_x):
	create_ind1(
		oProject=oProject,
		oEditor=oEditor,
		oDesign=oDesign,
		name_ind="layer2_ind"+str(layer2_ind_index),
		position_grid_x=ix,
		size_w_ind=size_w_ind,
		max_cell_length=meta_length
	)
	layer2_ind_index = layer2_ind_index+1
layer2_indcross_index=0
for iy in range(unit_cell_x):
	create_indcross1(
		oProject=oProject,
		oEditor=oEditor,
		oDesign=oDesign,
		name_ind="layer2_indcross"+str(layer2_indcross_index),
		position_grid_y=iy,
		size_w_ind=size_w_ind,
		max_cell_length=meta_length
	)
	layer2_indcross_index= layer2_indcross_index+1

## Create Dielectric 2


## Create Layer 3 & 5
import csv
file_path = 'D:/Master_NSYSU/CodeRepository_ThisPeriod/zhar_antenna_design/py_helper/2026_1_5_metasurfaceBuilder/zone_xyz_dat_merged.csv'

csv_data = []
with open(file_path, mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert numerical values to appropriate types if necessary
        # For this task, we can keep them as strings first, or try to convert on the fly
        # Let's try converting relevant numeric fields to float/int
        for k, v in row.items():
            try:
                row[k] = float(v) if '.' in v else int(v)
            except ValueError:
                pass # Keep as string if conversion fails
        csv_data.append(row)

# print(f"Loaded {len(csv_data)} rows from {file_path}")
# if csv_data:
#     print("First 5 rows of the loaded data (list of dictionaries):")
#     for i, row in enumerate(csv_data[:5]):
#         print(f"Row {i+1}: {row}")

# print("All rows of the loaded data (list of dictionaries):")
patch_layer1=1.5
layer1_cap_index=0
layer1_cap3_index=0
for i, row in enumerate(csv_data):
	create_cap2(
		oProject=oProject,
		oEditor=oEditor,
		oDesign=oDesign,
		name_cap="layer3cap"+str(layer1_cap_index),
		position_grid_x=row['x'],
		position_grid_y=row['y'],
		size_patch=row['top_length_2_mm']
	)
	layer1_cap_index = layer1_cap_index+1
	create_cap3(
		oProject=oProject,
		oEditor=oEditor,
		oDesign=oDesign,
		name_cap="layer5cap"+str(layer1_cap3_index),
		position_grid_x=row['x'],
		position_grid_y=row['y'],
		size_patch=row['top_length_3_mm']
	)
	layer1_cap3_index = layer1_cap3_index+1
    # print(f"Row {i+1}: {row}")


# patch_layer1=1.5
# layer1_cap_index=0
# for iy in range(unit_cell_y):
# 	for ix in range(unit_cell_x):
# 		create_cap2(
# 			oProject=oProject,
# 			oEditor=oEditor,
# 			oDesign=oDesign,
# 			name_cap="layer3cap"+str(layer1_cap_index),
# 			position_grid_x=ix,
# 			position_grid_y=iy,
# 			size_patch=patch_layer1
# 		)
# 		layer1_cap_index = layer1_cap_index+1

# ## Create Dielectric 3


## Create Layer 4
layer2_ind_index=0
meta_length = cell_length*unit_cell_x

for ix in range(unit_cell_x):
	create_ind2(
		oProject=oProject,
		oEditor=oEditor,
		oDesign=oDesign,
		name_ind="layer4_ind"+str(layer2_ind_index),
		position_grid_x=ix,
		size_w_ind=size_w_ind,
		max_cell_length=meta_length
	)
	layer2_ind_index = layer2_ind_index+1
layer2_indcross_index=0
for iy in range(unit_cell_x):
	create_indcross2(
		oProject=oProject,
		oEditor=oEditor,
		oDesign=oDesign,
		name_ind="layer4_indcross"+str(layer2_indcross_index),
		position_grid_y=iy,
		size_w_ind=size_w_ind,
		max_cell_length=meta_length
	)
	layer2_indcross_index= layer2_indcross_index+1

## Create Dielectric 4

# ## Create Layer 5
# patch_layer1=1.5
# layer1_cap_index=0
# for iy in range(unit_cell_y):
# 	for ix in range(unit_cell_x):
# 		create_cap3(
# 			oProject=oProject,
# 			oEditor=oEditor,
# 			oDesign=oDesign,
# 			name_cap="layer5cap"+str(layer1_cap_index),
# 			position_grid_x=ix,
# 			position_grid_y=iy,
# 			size_patch=patch_layer1
# 		)
# 		layer1_cap_index = layer1_cap_index+1

# ## Create Dielectric 5

## Create Layer 6
layer2_ind_index=0
meta_length = cell_length*unit_cell_x

for ix in range(unit_cell_x):
	create_ind3(
		oProject=oProject,
		oEditor=oEditor,
		oDesign=oDesign,
		name_ind="layer6_ind"+str(layer2_ind_index),
		position_grid_x=ix,
		size_w_ind=size_w_ind,
		max_cell_length=meta_length
	)
	layer2_ind_index = layer2_ind_index+1
layer2_indcross_index=0
for iy in range(unit_cell_x):
	create_indcross3(
		oProject=oProject,
		oEditor=oEditor,
		oDesign=oDesign,
		name_ind="layer6_indcross"+str(layer2_indcross_index),
		position_grid_y=iy,
		size_w_ind=size_w_ind,
		max_cell_length=meta_length
	)
	layer2_indcross_index= layer2_indcross_index+1
