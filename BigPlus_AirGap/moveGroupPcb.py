# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2024.1.0
# 10:09:51  Feb 22, 2026
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("AntennaLensArrayv3_001insub")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "pcb2",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "1.254mm"
	])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "pcb3",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "2.508mm"
	])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "pcb4",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "3.762mm"
	])


oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "pcb5",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "5.016mm"
	])
