# ----------------------------------------------
# HFSS / AEDT script
# Create separate AEDT files for airgap = 0.9, 1.0, 1.1 mm
# ----------------------------------------------
import os
import ScriptEnv

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

# =========================================================
# USER SETTINGS
# =========================================================
base_project_path = r"D:\Master_NSYSU\CodeRepository_ThisPeriod\zhar_antenna_design\HFSS_AntennaDesign\AntennaLensArray\BigPlusAntenna5Layers_30x30"
base_project_name = "BigPlusAntenna5Layer_30x30_Single"
design_name = "HFSSDesign1"
output_dir = r"D:\HFSS_Projects\airgap_variants"

sub_h_mm = 0.127
airgap_list_mm = [0.9, 1.0, 1.1]
pcb_list = ["pcb2", "pcb3", "pcb4", "pcb5"]

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# =========================================================
# Helper: update local variable
# =========================================================
def set_local_variable(oDesign, var_name, var_value):
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
                    "NAME:ChangedProps",
                    [
                        "NAME:" + var_name,
                        "Value:=", var_value
                    ]
                ]
            ]
        ]
    )

# =========================================================
# Main loop
# =========================================================
for airgap_mm in airgap_list_mm:

    # Always reopen base project cleanly
    # oDesktop.OpenProject(base_project_path)
    
    oProject_base = oDesktop.SetActiveProject(base_project_name)

    tag = str(airgap_mm).replace(".", "p")
    new_project_name = base_project_name + "_ag" + tag
    new_project_path = os.path.join(output_dir, new_project_name + ".aedt")

    # Save base project as a new variant
    oProject_base.SaveAs(new_project_path, True)

    # After SaveAs, get the active project again
    oProject = oDesktop.GetActiveProject()
    oDesign = oProject.SetActiveDesign(design_name)
    oEditor = oDesign.SetActiveEditor("3D Modeler")

    pitch_mm = sub_h_mm + airgap_mm

    # Assume variables sub_h, airgap, pitch_z already exist in base project.
    set_local_variable(oDesign, "subsrate_thickness",  str(sub_h_mm) + "mm")
    set_local_variable(oDesign, "airgap", str(airgap_mm) + "mm")
    # set_local_variable(oDesign, "pitch_z", str(pitch_mm) + "mm")

    # Move relative from clean base geometry
    for i, pcb_name in enumerate(pcb_list, start=1):
        z_mm = i * pitch_mm

        oEditor.Move(
            [
                "NAME:Selections",
                "Selections:=", pcb_name,
                "NewPartsModelFlag:=", "Model"
            ],
            [
                "NAME:TranslateParameters",
                "TranslateVectorX:=", "0mm",
                "TranslateVectorY:=", "0mm",
                "TranslateVectorZ:=", str(z_mm) + "mm"
            ]
        )

    oProject.Save()

    # Close the variant before next loop
    oDesktop.CloseProject(oProject.GetName())

print("Done.")