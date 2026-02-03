
import math

## Measurement in mm

# # Terminology
# uC = Unit cell
# xlenUc = Length of unit cell in X-axis
# ylenUc = Length of unit cell in Y-axis
# xorgUc = offset between origin of unit cell from global origin
# yorgUc = offset between origin of unit cell from global origin
# cUc = center of unit cell
# rUc = length between center of unit-cell to focal-point
# phuC = designed phase for unit cell

# define dimension of Unit Cell
xlenUc = 3
ylenUc = 3

# define Antenna array profile
xnumUc = 13
ynumUc = 13

# f_0 = 38GHz, alpha_0 = 7.80mm,
# define focal-point
foc_x = (xnumUc*xlenUc)/2
foc_y = (ynumUc*ylenUc)/2
foc_z = 13 # 1cm
f_0 = 38e9 # 38GHz

# =========================
# Wrap untuk RADIAN
# =========================
def wrap_rad_pos(rad):
    """Wrap ke [0, 2π)"""
    return rad % (2*math.pi)

def wrap_rad_sym(rad):
    """Wrap ke [-π, π)"""
    return (rad + math.pi) % (2*math.pi) - math.pi

# =========================
# Wrap untuk DEGREE
# =========================
def wrap_deg_pos(deg):
    """Wrap ke [0, 360)"""
    return deg % 360

def wrap_deg_sym(deg):
    """Wrap ke [-180, 180)"""
    return (deg + 180) % 360 - 180


def generate_alpha(f_0):
    c=3e8 # 300 x 10^6 m/s
    alpha_0 = c/f_0
    return alpha_0
def generate_alpha_mm(f_0):
    alpha_0_mm = generate_alpha(f_0)*1000
    return alpha_0_mm

def generate_phase(dist_uc_to_focal,dist_ant_to_docal,f_0):
    alpha_0 = generate_alpha_mm(f_0)
    temp_form = math.sqrt(dist_uc_to_focal**2+dist_ant_to_docal**2)
    phase_rad = (2*math.pi/alpha_0)*(temp_form-dist_ant_to_docal)
    return phase_rad

def generate_phase_deg(dist_uc_to_focal,dist_ant_to_docal,f_0):
    phase_rad = generate_phase(dist_uc_to_focal,dist_ant_to_docal,f_0)
    return math.degrees(phase_rad)

# discretize data


# bangun profil unit-cell (2D grid)
unitcell_profile = []
current_index = 0
current_xorgUc = 0
current_yorgUc = 0

for_viz = []
for_viz_phase = []
for iy in range(ynumUc):
    current_xorgUc = 0

    curr_x = []
    curr_x_phase = []
    for ix in range(xnumUc):
        cUcx = current_xorgUc+(xlenUc/2)
        cUcy = current_yorgUc+(ylenUc/2)
        rUc = math.sqrt(math.pow(foc_x-cUcx,2)+math.pow(foc_y-cUcy,2))

        # phase_uc
        phase_Uc = generate_phase_deg(rUc,foc_z,f_0)
        phase_Uc = wrap_deg_sym(phase_Uc)
        
        # Generate Single Profile
        # rUc = math.sqrt()
        unitcell_profile.append({
            "index" : current_index,
            "x_index":ix,
            "y_index":iy,    
            "x_org_uc":current_xorgUc,
            "y_org_uc":current_yorgUc,
            "r_Uc":rUc,
            "phase_Uc":phase_Uc
        })
        current_index = current_index+1
        current_xorgUc = current_xorgUc + xlenUc

        curr_x.append(rUc)
        curr_x_phase.append(phase_Uc)
    for_viz.append(curr_x)
    for_viz_phase.append(curr_x_phase)
    current_yorgUc = current_yorgUc + ylenUc
    

# tampilkan hasil
for row in unitcell_profile:
    print(row)

# Visualization only
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# Plot tile
cax = ax.imshow(for_viz, origin='lower', cmap='plasma')

# Tambah colorbar
cbar = fig.colorbar(cax, ax=ax)
cbar.set_label("distance[mm]")

# Label axis
ax.set_xlabel("X index (column)")
ax.set_ylabel("Y index (row)")
ax.set_title("Distance between Unit-cell to focal Point[mm] Tile Plot")

fig2, ax2 = plt.subplots()
# Plot tile
cax2 = ax2.imshow(for_viz_phase, origin='lower', cmap='plasma')

# Tambah colorbar
cbar2 = fig2.colorbar(cax2, ax=ax2)
cbar2.set_label("Phase[deg]")

# Label axis
ax2.set_xlabel("X index (column)")
ax2.set_ylabel("Y index (row)")
ax2.set_title("Phase Distribution on Tile Plot")

plt.show()