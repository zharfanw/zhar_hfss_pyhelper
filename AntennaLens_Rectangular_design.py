# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2024.1.0
# 13:12:11  Sep 21, 2025
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")



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


generateUnitCell(oDesign,oEditor,0,0,3,3,0.1,0)
for i in range(1, 14):
    generateUnitCell(oDesign,oEditor,3*i,3*i,3,3,0.1*i,i)
