import csv
import numpy as np
import re
from typing import Dict, Tuple

def _sanitize(name: str) -> str:
    """
    Ubah 'top_length [mm]' -> 'top_length_mm', hilangkan tanda kurung/bracket,
    spasi jadi underscore, huruf kecil semua.
    """
    # gabungkan unit di []/() tanpa spasi
    name = re.sub(r'[\[\(]\s*([^\]\)]+)\s*[\]\)]', r'_\1', name)
    # hapus karakter selain alfanumerik, underscore, dan titik
    name = re.sub(r'[^0-9a-zA-Z_\.]+', '_', name)
    # rapikan underscore ganda
    name = re.sub(r'__+', '_', name).strip('_')
    return name.lower()

def read_metasurface_csv(
    filename: str,
    delimiter: str = ','
) -> Tuple[np.ndarray, Dict[str, np.ndarray], np.ndarray, Dict[str, str]]:
    """
    Membaca CSV:
      - kolom pertama -> frequency (np.ndarray of float)
      - kolom terakhir -> ang_deg (np.ndarray of float)
      - kolom tengah -> dims dict: {<nama_header_asli>: array}, dan juga
        dapat diakses via nama yg sudah disanitasi (key gandanya).
    Return:
      frequency, dims, ang_deg, name_map
        - name_map: peta {sanitized_name: original_header} untuk lookup balik.
    """
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=delimiter)
        headers = next(reader)
        if len(headers) < 3:
            raise ValueError("Minimal harus ada 3 kolom: freq, >=1 dimensi, ang_deg")

        # indeks
        i_freq = 0
        i_ang  = len(headers) - 1
        dim_indices = list(range(1, i_ang))

        # siapkan penampung
        cols = [[] for _ in headers]
        for r in reader:
            if not r or all(cell.strip()=='' for cell in r):
                continue
            for i, val in enumerate(r):
                try:
                    cols[i].append(float(val))
                except ValueError:
                    # jika ada string (mis. 'NaN' non-standar), tetap coba paksa ke float via replace
                    v = val.replace(' ', '')
                    cols[i].append(float(v))
        # ubah ke numpy
        arrs = [np.array(c, dtype=float) for c in cols]

    frequency = arrs[i_freq]
    ang_deg   = arrs[i_ang]

    # bangun dims dict (dua kunci per kolom: asli & sanitized)
    dims: Dict[str, np.ndarray] = {}
    name_map: Dict[str, str] = {}
    for i in dim_indices:
        orig = headers[i]
        san  = _sanitize(orig)
        # simpan dengan kunci header asli
        dims[orig] = arrs[i]
        # juga simpan kunci sanitized jika belum ada atau menunjuk ke header sama
        if san not in dims:
            dims[san] = arrs[i]
            name_map[san] = orig  # untuk tahu baliknya

    return frequency, dims, ang_deg, name_map
