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
        # force between two bodies
        force = gravitational_force(
            r_earth,
            r_sun,
            MASS["earth"],
            MASS["sun"]
        )

        acceleration = force / MASS["earth"]

        r_earth = r_earth + v_earth * dt
        v_earth = v_earth + acceleration * dt

        earth_positions.append(r_earth.copy())

    return np.array(earth_positions)

# def integrate_moon_earth(tmax, dt=1e-3):
#     times = np.arange(0, tmax, dt)

#     r_moon = R0["moon"].copy()
#     v_moon = V0["moon"].copy()
#     r_earth = R0["earth"].copy()

#     moon_positions = [r_moon.copy()]

#     for _ in times:
#         # force between two bodies
#         force = gravitational_force(
#             r_moon,
#             r_earth,
#             MASS["moon"],
#             MASS["earth"]
#         )

#         acceleration = force / MASS["moon"]

#         r_moon = r_moon + v_moon * dt
#         v_moon = v_moon + acceleration * dt

#         moon_positions.append(r_moon.copy())

#     return np.array(moon_positions)

def integrate_earth_moon_sun(tmax, dt=1e-3):
    times = np.arange(0, tmax, dt)

    r_sun = R0["sun"].copy()

    r_earth = R0["earth"].copy()
    v_earth = V0["earth"].copy()

    r_moon = R0["moon"].copy()
    v_moon = V0["moon"].copy()

    earth_positions = [r_earth.copy()]
    moon_positions = [r_moon.copy()]

    for _ in times:
        force_earth_from_sun = gravitational_force(
            r_earth,
            r_sun,
            MASS["earth"],
            MASS["sun"]
        )

        force_earth_from_moon = gravitational_force(
            r_earth,
            r_moon,
            MASS["earth"],
            MASS["moon"]
        )

        force_moon_from_sun = gravitational_force(
            r_moon,
            r_sun,
            MASS["moon"],
            MASS["sun"]
        )

        force_moon_from_earth = gravitational_force(
            r_moon,
            r_earth,
            MASS["moon"],
            MASS["earth"]
        )

        earth_acceleration = (
            force_earth_from_sun + force_earth_from_moon
        ) / MASS["earth"]

        moon_acceleration = (
            force_moon_from_sun + force_moon_from_earth
        ) / MASS["moon"]

        r_earth = r_earth + v_earth * dt
        r_moon = r_moon + v_moon * dt

        v_earth = v_earth + earth_acceleration * dt
        v_moon = v_moon + moon_acceleration * dt

        earth_positions.append(r_earth.copy())
        moon_positions.append(r_moon.copy())

    return np.array(earth_positions), np.array(moon_positions)
