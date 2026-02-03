import numpy as np
import matplotlib.pyplot as plt
try:
    import imageio.v2 as imageio
    HAVE_IMAGEIO = True
except ImportError:
    HAVE_IMAGEIO = False

# =========================
# USER INPUTS
# =========================
f0 = 38e9
c0 = 299792458.0
omega0 = 2*np.pi*f0

cell_mm = 2.367
cell = cell_mm * 1e-3
os = 4
dy = dz = cell / os
dt = 0.99 / (c0*np.sqrt((1/dz**2) + (1/dy**2)))  # CFL

# 1D line zone along y (length 33)
zone_line = np.array([9,9,9,9,8,8,8,8,7,7,6,6,5,5,4,3,2,1,2,3,4,5,5,6,6,7,7,8,8,8,9,9,9])
Ny_cell = len(zone_line)
Ny = Ny_cell * os   # EXACT match
z_length_m = 0.05
Nz = int(np.ceil(z_length_m / dz)) + 1
nSteps = 2800

z_src = 25
z_ms  = 95
z_ms = min(z_ms, Nz - 1)
z_src = min(z_src, z_ms - 1)

# Recording
save_gif = True
gif_path = './fdtd_animation.gif'
gif_every = 25
gif_frame_duration = 0.04

# Given phase (deg) per zone from data
zone_phase_deg = {
    1: -154.633999,
    2: -158.859686,
    3: -162.243396,
    4: -162.370422,
    5: -163.011345,
    6: -163.045103,
    7: -164.109986,
    8: -206.003099,
    9: -218.479861,
}

# =========================
# ZONE -> PHASE (lookup)
# =========================
phi_cell_deg = np.array([zone_phase_deg[int(z)] for z in zone_line])

# Wrap phase into [0,360) for delay usage
phi_cell_deg_wrapped = np.mod(phi_cell_deg, 360.0)
phi_cell_rad = np.deg2rad(phi_cell_deg_wrapped)

# Upsample to FDTD grid
phi_y = np.repeat(phi_cell_rad, os)
assert len(phi_y) == Ny

# Phase -> time delay steps
tau_y = phi_y / omega0
Nd_y = np.rint(tau_y / dt).astype(int)
Nd_y = np.clip(Nd_y, 0, None)
maxD = int(Nd_y.max())

print(f"max delay steps = {maxD}")

# Plot phase profile (deg)
y_mm = (np.arange(Ny) - (Ny-1)/2) * (dy*1e3)
plt.figure()
plt.plot(y_mm, np.rad2deg(phi_y))
plt.title("Applied phase profile (wrapped deg)")
plt.xlabel("y (mm)")
plt.ylabel("phase (deg)")
plt.grid(True)
plt.tight_layout()
plt.show()

# =========================
# FDTD ARRAYS (TEz)
# =========================
Ez = np.zeros((Nz, Ny), dtype=np.float32)
Hy = np.zeros((Nz-1, Ny), dtype=np.float32)
Hx = np.zeros((Nz, Ny-1), dtype=np.float32)

mu0 = 4e-7*np.pi
eps0 = 1/(mu0*c0**2)
Ce = dt/eps0
Ch = dt/mu0

# Simple sponge absorber
sz = np.ones(Nz, dtype=np.float32)
sy = np.ones(Ny, dtype=np.float32)
pad_z = 30
pad_y = max(8, int(0.12*Ny))
for i in range(pad_z):
    d = (i+1)/pad_z
    sz[i] *= (1 - 0.22*d*d)
    sz[-1-i] *= (1 - 0.22*d*d)
for j in range(pad_y):
    d = (j+1)/pad_y
    sy[j] *= (1 - 0.22*d*d)
    sy[-1-j] *= (1 - 0.22*d*d)
Sponge = sz[:,None] * sy[None,:]

# Source (smooth sinusoid)
t = np.arange(nSteps)*dt
ramp = 1 - np.exp(-(t/(12/f0))**2)
src = (ramp * np.sin(omega0*t)).astype(np.float32)

# Metasurface delay buffers
buf = np.zeros((Ny, maxD+1), dtype=np.float32)
ptr = np.zeros(Ny, dtype=np.int32)

# Visualization with mm axes
z_mm = np.arange(Nz) * (dz*1e3)
plt.ion()
fig, ax = plt.subplots(figsize=(9,5))
im = ax.imshow(Ez.T, origin="lower", aspect="auto",
               extent=[z_mm.min(), z_mm.max(), y_mm.min(), y_mm.max()],
               vmin=-0.3, vmax=0.3, cmap="RdBu")
ax.set_xlabel("z (mm)")
ax.set_ylabel("y (mm)")
plt.colorbar(im, ax=ax, label="Ez (a.u.)")
plt.tight_layout()

gif_writer = None
if save_gif and HAVE_IMAGEIO:
    gif_writer = imageio.get_writer(gif_path, mode='I', duration=gif_frame_duration)

# =========================
# MAIN LOOP
# =========================
for n in range(nSteps):
    Hx -= (Ch/dy) * (Ez[:,1:] - Ez[:,:-1])
    Hy += (Ch/dz) * (Ez[1:,:] - Ez[:-1,:])

    curlH = np.zeros_like(Ez)
    curlH[1:-1,1:-1] = (Hy[1:,1:-1]-Hy[:-1,1:-1])/dz - (Hx[1:-1,1:]-Hx[1:-1,:-1])/dy
    Ez[1:-1,1:-1] += Ce * curlH[1:-1,1:-1]

    Ez[z_src, :] += src[n]

    incoming = Ez[z_ms-1, :].copy()
    if maxD > 0:
        buf[np.arange(Ny), ptr] = incoming
        read_idx = (ptr - Nd_y) % (maxD + 1)
        Ez[z_ms, :] = buf[np.arange(Ny), read_idx]
        ptr = (ptr + 1) % (maxD + 1)
    else:
        Ez[z_ms, :] = incoming

    Ez *= Sponge

    if n % 25 == 0:
        im.set_data(Ez.T)
        ax.set_title(f"Ez field step {n} | metasurface z={z_ms*dz*1e3:.1f} mm")
        plt.pause(0.001)
        if save_gif and n % gif_every == 0:
            fig.canvas.draw()
            w, h = fig.canvas.get_width_height()
            if hasattr(fig.canvas, "tostring_rgb"):
                frame = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8).reshape(h, w, 3)
            elif hasattr(fig.canvas, "buffer_rgba"):
                frame = np.frombuffer(fig.canvas.buffer_rgba(), dtype=np.uint8).reshape(h, w, 4)[:, :, :3]
            else:
                frame = np.frombuffer(fig.canvas.tostring_argb(), dtype=np.uint8).reshape(h, w, 4)[:, :, 1:]
            if gif_writer is not None:
                gif_writer.append_data(frame)

plt.ioff()
plt.show()

if save_gif:
    if gif_writer is not None:
        gif_writer.close()
        print(f"Saved GIF: {gif_path}")
    elif not HAVE_IMAGEIO:
        print("imageio not available; install imageio to save GIF.")
