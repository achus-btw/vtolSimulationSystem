import numpy as np
import numba


class bogey:
    pos = np.array([0, 0, 0])

    # needs
    #  1-physics object
    #  2-aerodynamics object
    #  3-rotor object
    #  4-controller object
    #  5-rendering
    def __init__(self, initialPosition: np.ndarray):
        pos = initialPosition
