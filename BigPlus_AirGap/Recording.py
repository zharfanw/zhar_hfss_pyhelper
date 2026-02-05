# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2024.1.0
# 6:21:47  Feb 04, 2026
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.NewProject()
oProject.InsertDesign("HFSS", "HFSSDesign1", "HFSS Terminal Network", "")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
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
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "0mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "1mm",
		"YSize:="		, "1mm",
		"ZSize:="		, "0.2mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box1",
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
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.AssignMaterial(
	[
		"NAME:Selections",
		"AllowRegionDependentPartSelectionForPMLCreation:=", True,
		"AllowRegionSelectionForPMLCreation:=", True,
		"Selections:="		, "Box1"
	], 
	[
		"NAME:Attributes",
		"MaterialValue:="	, "\"Rogers RT/duroid 5880 (tm)\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "nan ",
		"ReferenceTemperature:=", "nan ",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Box1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "substrate_lay1_"
				]
			]
		]
	])
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
					"NAME:cell_length",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "3mm"
				],
				[
					"NAME:cell_width",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "3mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"substrate_lay1_:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "absolute_x",
					"Y:="			, "absolute_y",
					"Z:="			, "0mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"substrate_lay1_:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "cell_length"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"substrate_lay1_:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:YSize",
					"Value:="		, "cell_width"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"substrate_lay1_:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:ZSize",
					"Value:="		, "subsrate_thickness"
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0.2mm",
		"YPosition:="		, "0.4mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "2.2mm",
		"YSize:="		, "2.4mm",
		"ZSize:="		, "0.2mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box1",
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
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.AssignMaterial(
	[
		"NAME:Selections",
		"AllowRegionDependentPartSelectionForPMLCreation:=", True,
		"AllowRegionSelectionForPMLCreation:=", True,
		"Selections:="		, "Box1"
	], 
	[
		"NAME:Attributes",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "nan ",
		"ReferenceTemperature:=", "nan ",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Box1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "copper_lay1_"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"copper_lay1_:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "absolute_x",
					"Y:="			, "absolute_y",
					"Z:="			, "subsrate_thickness"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"copper_lay1_:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "absolute_x+(cell_length/2)-(w_ind/2)",
					"Y:="			, "absolute_y +(cell_length/2)-(the_L/2)",
					"Z:="			, "subsrate_thickness"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"copper_lay1_:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "w_ind"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"copper_lay1_:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:YSize",
					"Value:="		, "the_L"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"copper_lay1_:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:ZSize",
					"Value:="		, "copper_thickness"
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "copper_lay1_"
	])
oEditor.Paste()
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"copper_lay1_1:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "absolute_x+(cell_length/2)-(the_L/2)",
					"Y:="			, "absolute_y +(cell_length/2)-(w_ind/2)",
					"Z:="			, "subsrate_thickness"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"copper_lay1_1:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "the_L"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"copper_lay1_1:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:YSize",
					"Value:="		, "w_ind"
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "copper_lay1_,copper_lay1_1"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False,
		"TurnOnNBodyBoolean:="	, True
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"copper_lay1_"
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
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"substrate_lay1_"
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
oEditor.CreateGroup(
	[
		"NAME:GroupParameter",
		"ParentGroupID:="	, "Model",
		"Parts:="		, "substrate_lay1_,copper_lay1_",
		"SubmodelInstances:="	, "",
		"Groups:="		, ""
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Attributes",
			[
				"NAME:PropServers", 
				"_lay1_Group"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "uc_1"
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "uc_1"
	])
oEditor.Paste()
oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "uc_2",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "3mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "0mm"
	])
oProject.SaveAs("D:\\Master_NSYSU\\CodeRepository_ThisPeriod\\zhar_antenna_design\\HFSS_AntennaDesign\\AntennaLensArray\\BigPlus_airgap\\Project8.aedt", True)
