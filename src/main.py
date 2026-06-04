import numpy as np
import matplotlib.pyplot as plt

# Units:
# distance = AU
# time = years
# mass = solar masses

G = 4 * np.pi**2  # Gravitational constant in these units

MASS = {
    'Sun': 1.0,
    'Earth': 3.003e-6,
    'Moon': 3.694e-8
}

R0 = {
    "Sun": np.array([0.0, 0.0, 0.0]),
    "earth": np.array([9.978977040419635e-01, 6.586825681892025e-02, -6.320430920521123e-06]),
    "moon": np.array([9.956768547953816e-01, 6.676030485840675e-02, 1.641093070596718e-04]),
}

V0 = {
    "Sun": np.array([0.0, 0.0, 0.0]),
    "earth": np.array([-4.70015711e-01, 6.25165839e00, -3.40817831e-04]),
    "moon": np.array([-0.55065949, 6.03534661, 0.01111456]),
}

def gravitational_force(position_i, position_j, mass_i, mass_j):
    """
    Return the gravitational force on body i due to body j.
    """
    displacement = position_j - position_i
    distance = np.linalg.norm(displacement)

    if distance == 0:
        raise ValueError("Two bodies cannot occupy the same position.")
    
    direction = displacement / distance
    force_magnitude = G * mass_i * mass_j / distance**2

    return force_magnitude * direction

def integrate_earth_sun(tmax, dt=1e-3):
    """
    Simulate Earth orbiting a fixed Sun.
    """
    times = np.arange(0, tmax, dt)
    
    r_earth = R0['earth'].copy()
    v_earth = V0['earth'].copy()
    r_sun = R0['Sun'].copy()

    earth_positions = [r_earth.copy()]

    for _ in times:
        force = gravitational_force(
            r_earth, 
            r_sun, 
            MASS['Earth'], 
            MASS['Sun']
        )

        acceleration = force / MASS['Earth']

        r_earth = r_earth + v_earth * dt
        v_earth = v_earth + acceleration * dt

        earth_positions.append(r_earth.copy())

    return np.array(earth_positions)

def plot_trajectory(positions, filename):
    """
    Plot x-y trajectory and save to file.
    """
    plt.figure()
    plt.plot(positions[:, 0], positions[:, 1])
    plt.xlabel("X Position (AU)")
    plt.ylabel("Y Position (AU)")
    plt.gca().set_aspect('equal')
    plt.title("Earth Orbit Around Fixed Sun")
    # plt.axis("equal")
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    earth_positions = integrate_earth_sun(tmax=1.0, dt=1e-3)

    print(earth_positions[:10])  # Print the first 100 positions for verification
    print(earth_positions.shape)  # Print the shape of the positions array
    
    plot_trajectory(earth_positions, "earth_only_orbit.png")
    print("Saved plot to earth_only_orbit.png")
    