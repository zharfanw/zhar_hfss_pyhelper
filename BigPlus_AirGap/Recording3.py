# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2024.1.0
# 7:24:09  Feb 05, 2026
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project8")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "uc_2"
	])
oEditor.Paste()
oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "uc_3",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "3mm",
		"TranslateVectorY:="	, "3mm",
		"TranslateVectorZ:="	, "0mm"
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"copper_lay1_4:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "2mm"
				]
			]
		]
	])
