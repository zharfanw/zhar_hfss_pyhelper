
'''
with assumption that csv data contains like this
------ csv data ----- 
"Freq [GHz]","top_length [mm]","ang_deg(S(FloquetPort2:1,FloquetPort1:1)) [deg]"
38,0.1,-152.898092996509
38,0.2,-151.963572386869
38,0.3,-151.750544047922
------ csv data -----
'''

import csv
from dataclasses import dataclass, field
from typing import Dict, Any, List
import matplotlib.pyplot as plt

# Definisi struct
@dataclass
class RowData:
    frequency: float
    dimensi: Dict[str, float] = field(default_factory=dict)
    ang_deg: float = 0.0

filename = "data.csv"
const_del = ','
rows = []

with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=const_del)
    header = next(reader)  # skip baris header (kalau ada)
    # Bersihkan header → ambil bagian sebelum spasi
    clean_header = [h.split(" ")[0] for h in header]

    # cari index kolom
    freq_idx = 0
    ang_idx  = len(header) - 1
    dimensi_headers = clean_header[1:ang_idx]  # kolom di tengah dianggap dimensi

    for r in reader:
        frequency = float(r[freq_idx])
        ang_deg   = float(r[ang_idx])

        # ambil semua dimensi jadi dict
        dimensi_dict = {}
        for i, col_name in enumerate(dimensi_headers, start=1):
            dimensi_dict[col_name] = float(r[i])

        row = RowData(frequency=frequency, dimensi=dimensi_dict, ang_deg=ang_deg)
        rows.append(row)

# Contoh akses
for row in rows:
    print(f"f={row.frequency} Hz, dim={row.dimensi}, ang={row.ang_deg}°")

# # Ambil data untuk plotting
# freqs   = [row.frequency for row in rows]
# dimensi = [row.dimensi for row in rows]
# ang_deg = [row.ang_deg for row in rows]

# # Plot 1: dimensi vs and_deg
# plt.figure()
# plt.plot(dimensi, ang_deg, marker='o')
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Dimensi")
# plt.title("Frequency vs Dimensi")
# plt.grid(True)

# plt.show()