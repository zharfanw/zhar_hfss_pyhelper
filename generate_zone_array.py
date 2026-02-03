import math
import numpy as np
import matplotlib.pyplot as plt

# =========================
# CONFIG (all in mm, Hz)
# =========================
xlen_uc_mm = 2.37
ylen_uc_mm = 2.37

xnum_uc = 20
ynum_uc = 20

f0_hz = 38e9

# focal distance (mm)
foc_z_mm = 30 # NOTE: 1 cm = 10 mm

# Lens aperture size (mm)
aperture_x_mm = xnum_uc * xlen_uc_mm
aperture_y_mm = ynum_uc * ylen_uc_mm

# focal point position in XY (mm) -> center of aperture
foc_x_mm = aperture_x_mm / 2.0
foc_y_mm = aperture_y_mm / 2.0


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

    # return wrap_deg_sym(phase_deg) if wrap else phase_deg
    return phase_deg


# =========================
# BUILD GRID
# =========================
phase_map = np.zeros((ynum_uc, xnum_uc), dtype=float)
r_map = np.zeros((ynum_uc, xnum_uc), dtype=float)

unitcell_profile = []
idx = 0

for iy in range(ynum_uc):
    y_org = iy * ylen_uc_mm
    c_y = y_org + (ylen_uc_mm / 2.0)

    for ix in range(xnum_uc):
        x_org = ix * xlen_uc_mm
        c_x = x_org + (xlen_uc_mm / 2.0)

        r_xy = math.sqrt((foc_x_mm - c_x)**2 + (foc_y_mm - c_y)**2)
        ph_deg = phase_from_r_mm(r_xy, foc_z_mm, f0_hz, wrap=True)

        r_map[iy, ix] = r_xy
        phase_map[iy, ix] = ph_deg

        unitcell_profile.append({
            "index": idx,
            "x_index": ix,
            "y_index": iy,
            "x_org_uc_mm": x_org,
            "y_org_uc_mm": y_org,
            "c_x_mm": c_x,
            "c_y_mm": c_y,
            "r_xy_mm": r_xy,
            "phase_deg": ph_deg
        })
        idx += 1

# =========================
# OPTIONAL: print a few rows only (avoid spam)
# =========================
print("First 10 unit cells:")
for row in unitcell_profile[:10]:
    print(row)

print("\nCenter cell phase:", phase_map[ynum_uc//2, xnum_uc//2], "deg")
print("Corner cell phase:", phase_map[0, 0], "deg")


# =========================
# VISUALIZATION
# =========================
fig1, ax1 = plt.subplots()
im1 = ax1.imshow(r_map, origin="lower", cmap="plasma")
cbar1 = fig1.colorbar(im1, ax=ax1)
cbar1.set_label("r_xy [mm]")
ax1.set_xlabel("X index (column)")
ax1.set_ylabel("Y index (row)")
ax1.set_title("Distance r_xy from cell center to focal projection (mm)")

fig2, ax2 = plt.subplots()
im2 = ax2.imshow(phase_map, origin="lower", cmap="plasma", vmin=-180, vmax=180)
cbar2 = fig2.colorbar(im2, ax=ax2)
cbar2.set_label("Phase [deg] (wrapped to [-180, 180))")
ax2.set_xlabel("X index (column)")
ax2.set_ylabel("Y index (row)")
ax2.set_title("Phase Distribution (Transmitarray/Lens)")

plt.show()
