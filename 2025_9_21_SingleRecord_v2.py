# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2024.1.0
# 14:33:10  Sep 21, 2025
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("AntennaLensArray_Rect")
oProject.InsertDesign("HFSS", "HFSSDesign1", "HFSS Terminal Network", "")
oDesign = oProject.SetActiveDesign("AntennaLensArray")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "BottomRing,BottomRect,Substrate_Mid,UpperRing,UpperRect"
	])
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Paste()
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"BottomRect:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "xorgUc+(xlenUc/2)-(top_length/2)+3",
					"Y:="			, "yorgUc+(ylenUc/2)-(top_length/2)+3",
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
				"BottomRect:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "xorgUc+(xlenUc/2)-(top_length/2)+3mm",
					"Y:="			, "yorgUc+(ylenUc/2)-(top_length/2)+3mm",
					"Z:="			, "0mm"
				]
			]
		]
	])
