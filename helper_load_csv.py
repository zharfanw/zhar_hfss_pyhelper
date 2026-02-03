import csv
from dataclasses import dataclass, field
from typing import Dict, List
import matplotlib.pyplot as plt

# # Definisi struct
# @dataclass
# class RowData:
#     frequency: float
#     dimensi: Dict[str, float] = field(default_factory=dict)
#     ang_deg: float = 0.0

class RowData(object):
    def __init__(self, frequency, dimensi, ang_deg):
        self.frequency = float(frequency)
        self.dimensi = dimensi
        self.ang_deg = float(ang_deg)

def helper_load_csv(filename: str, delimiter: str = ',', visualize: bool = False) -> List[RowData]:
    rows: List[RowData] = []

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        header = next(reader)  # ambil header
        clean_header = [h.split(" ")[0] for h in header]

        # cari index kolom
        freq_idx = 0
        ang_idx  = len(header) - 1
        dimensi_headers = clean_header[1:ang_idx]  # kolom tengah = dimensi

        for r in reader:
            frequency = float(r[freq_idx])
            ang_deg   = float(r[ang_idx])

            # ambil semua dimensi → dict
            dimensi_dict = {}
            for i, col_name in enumerate(dimensi_headers, start=1):
                dimensi_dict[col_name] = float(r[i])

            row = RowData(frequency=frequency, dimensi=dimensi_dict, ang_deg=ang_deg)
            rows.append(row)

    # Jika minta visualisasi
    if visualize:
        # Contoh: ambil dimensi pertama untuk x-axis
        if dimensi_headers:
            x_vals = [row.dimensi[dimensi_headers[0]] for row in rows]
            y_vals = [row.frequency for row in rows]
            z_vals = [row.ang_deg for row in rows]

            plt.figure()
            sc = plt.scatter(x_vals, z_vals, c=y_vals, cmap="viridis")
            plt.colorbar(sc, label="Phase (deg)")
            plt.xlabel(dimensi_headers[0])
            plt.ylabel("Phase (deg)")
            plt.title("Dimension")
            plt.grid(True)
            plt.show()

    return rows


# =======================
# Contoh penggunaan
# =======================
if __name__ == "__main__":
    data = helper_load_csv("data.csv", delimiter=",", visualize=True)
    for row in data:
        print(row)
