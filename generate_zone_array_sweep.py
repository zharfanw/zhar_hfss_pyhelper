import math
import numpy as np
import matplotlib.pyplot as plt

# =========================
# CONFIG (all in mm, Hz)
# =========================
xlen_uc_mm = 3.0
ylen_uc_mm = 3.0

xnum_uc = 20
ynum_uc = 20

f0_hz = 38e9

# Sweep for focal distance (mm)
foc_z_start_mm = 60.0
foc_z_stop_mm = 100.0
foc_z_step_mm = 4.0

# Lens aperture size (mm)
aperture_x_mm = xnum_uc * xlen_uc_mm
aperture_y_mm = ynum_uc * ylen_uc_mm

# focal point position in XY (mm) -> center of aperture
foc_x_mm = aperture_x_mm / 2.0
foc_y_mm = aperture_y_mm / 2.0

# Plot settings
PLOT_EACH = True

# =========================
# HELPERS
# =========================
def wrap_deg_sym(deg: float) -> float:
    """Wrap phase to [-180, 180) degrees"""
    return (deg + 180.0) % 360.0 - 180.0

def lambda0_mm(f_hz: float) -> float:
    c = 299_792_458.0  # m/s
    return (c / f_hz) * 1000.0  # mm

def phase_from_r_mm(r_xy_mm: float, f_mm: float, f_hz: float, wrap=True) -> float:
    """
    r_xy_mm: radial distance from cell center to focal projection on aperture plane (mm)
    f_mm: focal distance along z (mm)
    phase = k0 * (sqrt(r^2 + f^2) - f)
    """
    lam_mm = lambda0_mm(f_hz)
    k0 = 2.0 * math.pi / lam_mm  # rad/mm

    delta_L = math.sqrt(r_xy_mm**2 + f_mm**2) - f_mm  # mm
    phase_rad = k0 * delta_L
    phase_deg = math.degrees(phase_rad)

    return wrap_deg_sym(phase_deg) if wrap else phase_deg


def build_phase_map(foc_z_mm: float):
    phase_map = np.zeros((ynum_uc, xnum_uc), dtype=float)
    r_map = np.zeros((ynum_uc, xnum_uc), dtype=float)

    for iy in range(ynum_uc):
        y_org = iy * ylen_uc_mm
        c_y = y_org + (ylen_uc_mm / 2.0)

        for ix in range(xnum_uc):
            x_org = ix * xlen_uc_mm
            c_x = x_org + (xlen_uc_mm / 2.0)

            r_xy = math.sqrt((foc_x_mm - c_x) ** 2 + (foc_y_mm - c_y) ** 2)
            ph_deg = phase_from_r_mm(r_xy, foc_z_mm, f0_hz, wrap=True)

            r_map[iy, ix] = r_xy
            phase_map[iy, ix] = ph_deg

    return r_map, phase_map


def main():
    sweep_foc_z_mm = list(
        np.arange(foc_z_start_mm, foc_z_stop_mm + 0.5 * foc_z_step_mm, foc_z_step_mm)
    )

    print("Sweep foc_z_mm:", sweep_foc_z_mm)

    for foc_z_mm in sweep_foc_z_mm:
        r_map, phase_map = build_phase_map(foc_z_mm)

        center_phase = phase_map[ynum_uc // 2, xnum_uc // 2]
        corner_phase = phase_map[0, 0]
        print(
            f"foc_z_mm={foc_z_mm:.2f} -> center={center_phase:.2f} deg, corner={corner_phase:.2f} deg"
        )

        if PLOT_EACH:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

            im1 = ax1.imshow(r_map, origin="lower", cmap="plasma")
            fig.colorbar(im1, ax=ax1, label="r_xy [mm]")
            ax1.set_xlabel("X index (column)")
            ax1.set_ylabel("Y index (row)")
            ax1.set_title(f"r_xy (foc_z={foc_z_mm:.2f} mm)")

            im2 = ax2.imshow(phase_map, origin="lower", cmap="plasma", vmin=-180, vmax=180)
            fig.colorbar(im2, ax=ax2, label="Phase [deg]")
            ax2.set_xlabel("X index (column)")
            ax2.set_ylabel("Y index (row)")
            ax2.set_title(f"Phase (foc_z={foc_z_mm:.2f} mm)")

    plt.show()


if __name__ == "__main__":
    main()