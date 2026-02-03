import csv

def matrix_to_xyz_csv(
    input_csv="zone_map_33x33.csv",
    output_csv="zone_xyz_33x33.csv"
):
    # Read matrix
    with open(input_csv, "r") as f:
        reader = csv.reader(f)
        Z = [list(map(int, row)) for row in reader]

    ny = len(Z)
    nx = len(Z[0])

    # Write x,y,zone
    with open(output_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y", "zone"])  # header

        for y in range(ny):
            for x in range(nx):
                writer.writerow([x, y, Z[y][x]])

    print(f"✅ Generated {output_csv} ({nx*ny} rows)")


# RUN
matrix_to_xyz_csv()
