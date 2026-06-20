from simulation import integrate_earth_sun
from visualization import plot_trajectory

if __name__ == "__main__":
    print(earth_positions[:10])
    print(earth_positions.shape)

    plot_trajectory(earth_positions, "orbit_earth_only.png")
    print("Saved plot to orbit_earth_only.png")