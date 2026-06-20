import numpy as np

from constants import MASS, R0, V0
from physics import gravitational_force

def integrate_earth_sun(tmax, dt=1e-3):
    times = np.arange(0, tmax, dt)

    r_earth = R0["earth"].copy()
    v_earth = V0["earth"].copy()
    r_sun = R0["sun"].copy()

    earth_positions = [r_earth.copy()]

    for _ in times:
        force = gravitational_force(
            r_earth,
            r_sun,
            MASS["earth"],
            MASS["sun"]
        )

        acceleration = force / MASS["earth"]

        r_earth = r_earth + v_earth * dt
        v_earth = v_earth + acceleration * dt

    return np.array(earth_positions)

