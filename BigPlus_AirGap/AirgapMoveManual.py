# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2024.1.0
# 10:09:51  Feb 22, 2026
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("BigPlusAntenna5Layer_30x30_Single")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")


pcb_thickness=0.035
sub_h=1.575+pcb_thickness
airgap=0

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
		"TranslateVectorZ:="	, str(sub_h*1+airgap*1)+"mm"
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
		"TranslateVectorZ:="	, str(sub_h*2+airgap*2)+"mm"
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
		"TranslateVectorZ:="	, str(sub_h*3+airgap*3)+"mm"
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
		"TranslateVectorZ:="	, str(sub_h*4+airgap*4)+"mm"
	])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "pcb6",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, str(sub_h*4+airgap*4)+"mm"
	])
