import matplotlib.pyplot as plt

# Contoh data: matriks 10x10
data = [[(i+j) for j in range(10)] for i in range(10)]

fig, ax = plt.subplots()

# Tampilkan data sebagai tile (heatmap)
cax = ax.imshow(data, origin='lower', cmap='viridis')

# Tambahkan colorbar
cbar = fig.colorbar(cax, ax=ax)
cbar.set_label("Value")

# Tambahkan label axis
ax.set_xlabel("X index")
ax.set_ylabel("Y index")
ax.set_title("Tile Plot with Colorbar")

plt.show()
