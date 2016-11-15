from B_mode_image_creation import envelope_detection
import numpy as np


def test_envelope_detection():
    data_a = [np.array([1, -2, 3, 4, 5]), np.array([6, 7, -8, 9, -10]), np.array([11, -12, 13, 14, -15])]
    a = envelope_detection(data_a, 3)
    assert np.any(a) == np.any([np.array([1.5, 2, 3, 4, 4.5]), np.array([6.5, 7, 8, 9, 9.5]),
                                np.array([11.5, 12, 13, 14, 14.5])])
