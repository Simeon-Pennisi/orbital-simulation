import numpy as np

from constants import G

def gravitational_force(position_i, position_j, mass_i, mass_j):
    displacement = position_j - position_i
    distance = np.linalg.norm(displacement)

    if distance == 0:
        raise ValueError("Distance between bodies cannot be zero.")
    
    direction = displacement / distance
    force_magnitude = G * mass_i * mass_j / distance**2

    return force_magnitude * direction
