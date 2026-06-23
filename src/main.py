from simulation import integrate_earth_sun, integrate_earth_moon_sun
from visualization import plot_trajectory

if __name__ == "__main__":
    earth_positions = integrate_earth_sun(tmax=1, dt=1e-3)

    print("Earth-Sun simulation:")
    print(earth_positions[:10])
    print(earth_positions.shape)

    plot_trajectory(earth_positions, "orbit_earth_only.png")
    print("Saved plot to orbit_earth_only.png")

    earth_positions, moon_positions = integrate_earth_moon_sun(tmax=1, dt=1e-3)

    print("Earth-Moon-Sun simulation:")
    print("Earth:", earth_positions.shape)
    print("Moon:", moon_positions.shape)

    plot_trajectory(earth_positions, "orbit_earth_moon_earth.png")
    plot_trajectory(moon_positions, "orbit_earth_moon_moon.png")

    print("Saved Earth and Moon plots")
