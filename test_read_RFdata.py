from read_RFdata import read_RF, RF_bars
import numpy as np


def test_read_RFdata():
    bin_data = read_RF('test.bin')
    assert bin_data == np.array([770])


def test_RF_bars():

    sample_points = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    sample_split = RF_bars(sample_points, 3)
    assert np.any(sample_split) == np.any([np.array([1, 2, 3, 4, 5]), np.array([6, 7, 8, 9, 10]), np.array([11, 12, 13, 14, 15])])
