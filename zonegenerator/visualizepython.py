import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    csv_path = './zone_xyz_33x33.csv'
    out_path = './zone_xyz_33x33_tiles.png'
    origin = 'lower'

    df = pd.read_csv(csv_path)
    if not {'x', 'y', 'zone'}.issubset(df.columns):
        raise ValueError('CSV must contain x, y, zone columns.')

    grid = df.pivot(index='y', columns='x', values='zone')

    plt.figure(figsize=(6, 6))
    ax = plt.gca()
    plt.imshow(grid.values, origin=origin, interpolation='nearest')
    plt.colorbar(label='zone')
    plt.title('Zone Map (x,y)')
    plt.xlabel('x')
    plt.ylabel('y')
    x_count = grid.shape[1]
    y_count = grid.shape[0]
    ax.set_xticks(np.arange(-0.5, x_count, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, y_count, 1), minor=True)
    ax.grid(which='minor', linestyle='-', linewidth=0.5)
    ax.tick_params(which='minor', bottom=False, left=False)
    plt.tight_layout()

    plt.savefig(out_path, dpi=150)
    plt.show()


if __name__ == '__main__':
    main()
