# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2024.1.0
# 13:12:11  Sep 21, 2025
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")

def generateUnitCell(oDesign,oEditor,xorgUc,yorgUc,index):
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
            "XPosition:="		, str(xorgUc)+"mm"+"+(xlenUc/2)-(top_length/2)",
            "YPosition:="		, str(yorgUc)+"mm"+"+(ylenUc/2)-(top_length/2)",
            "ZPosition:="		, "0mm",
            "XSize:="		, "top_length",
            "YSize:="		, "top_length",
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
            "XPosition:="		, str(xorgUc)+"mm"+"+(xlenUc/2)-(top_length/2)",
            "YPosition:="		, str(yorgUc)+"mm"+"+(ylenUc/2)-(top_length/2)",
            "ZPosition:="		, "substrate_thickness+cond_thickness",
            "XSize:="		, "top_length",
            "YSize:="		, "top_length",
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
oProject = oDesktop.SetActiveProject("AntennaLensArray_Rect")
oProject.InsertDesign("HFSS", "AntennaGeneratedByPy", "HFSS Terminal Network", "")
oDesign = oProject.SetActiveDesign("AntennaGeneratedByPy")
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
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0.2mm",
		"YPosition:="		, "0.2mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "0.6mm",
		"YSize:="		, "0.6mm",
		"ZSize:="		, "0.2mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "BottomRing",
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
		"Selections:="		, "BottomRing"
	], 
	[
		"NAME:Attributes",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "nan ",
		"ReferenceTemperature:=", "nan ",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", True,
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
				"BottomRing"
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
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"BottomRing:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "xlenUc"
				],
				[
					"NAME:YSize",
					"Value:="		, "ylenUc"
				],
				[
					"NAME:Position",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "0mm"
				],
				[
					"NAME:ZSize",
					"Value:="		, "cond_thickness"
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "outer_ring_width/2",
		"YPosition:="		, "outer_ring_width/2",
		"ZPosition:="		, "0mm",
		"XSize:="		, "xlenUc-outer_ring_width",
		"YSize:="		, "ylenUc-outer_ring_width",
		"ZSize:="		, "cond_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "BottomRingTool",
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
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "BottomRing",
		"Tool Parts:="		, "BottomRingTool"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False,
		"TurnOnNBodyBoolean:="	, True
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "(xlenUc/2)-(top_length/2)",
		"YPosition:="		, "(ylenUc/2)-(top_length/2)",
		"ZPosition:="		, "0mm",
		"XSize:="		, "top_length",
		"YSize:="		, "top_length",
		"ZSize:="		, "cond_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "BottomRect",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, False,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
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
				"BottomRect"
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
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "0mm",
		"ZPosition:="		, "cond_thickness",
		"XSize:="		, "xlenUc",
		"YSize:="		, "ylenUc",
		"ZSize:="		, "substrate_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Subtrate_",
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
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Subtrate_"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Material Appearance",
					"Value:="		, True
				],
				[
					"NAME:Transparent",
					"Value:="		, 0.75
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
		"ZPosition:="		, "substrate_thickness+cond_thickness",
		"XSize:="		, "xlenUc",
		"YSize:="		, "xlenUc",
		"ZSize:="		, "cond_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "UpperRing",
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
		"XPosition:="		, "outer_ring_width/2",
		"YPosition:="		, "outer_ring_width/2",
		"ZPosition:="		, "substrate_thickness+cond_thickness",
		"XSize:="		, "xlenUc-outer_ring_width",
		"YSize:="		, "ylenUc-outer_ring_width",
		"ZSize:="		, "cond_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "UpperRingTool",
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
		"Blank Parts:="		, "UpperRing",
		"Tool Parts:="		, "UpperRingTool"
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
				"UpperRing"
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
		"XPosition:="		, "(xlenUc/2)-(top_length/2)",
		"YPosition:="		, "(ylenUc/2)-(top_length/2)",
		"ZPosition:="		, "substrate_thickness+cond_thickness",
		"XSize:="		, "top_length",
		"YSize:="		, "top_length",
		"ZSize:="		, "cond_thickness"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "UpperRect",
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
				"UpperRect"
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

generateUnitCell(oDesign,oEditor,3,3,2)