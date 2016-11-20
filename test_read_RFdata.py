from read_RFdata import read_RF, RF_bars, MissingDataError, NotBinaryFileError
import numpy as np
import pytest


def test_read_RFdata():
    bin_data = read_RF('test.bin', 1, 1)
    assert bin_data == np.array([770])


def test_RF_bars():

    sample_points = np.array([1, 2, 3, 4, 5, 6, 7,
                              8, 9, 10, 11, 12, 13, 14, 15])
    sample_split = RF_bars(sample_points, 3)
    assert np.any(sample_split) == np.any([np.array([1, 2, 3, 4, 5]),
                                           np.array([6, 7, 8, 9, 10]),
                                           np.array([11, 12, 13, 14, 15])])


def test_read_RF_data_missing_file():
    with pytest.raises(FileNotFoundError):
        read_RF('apple.dat', 10, 10)


def test_read_RF_data_missing_data():
    with pytest.raises(MissingDataError):
        read_RF('test.bin', 10, 10)


def test_read_RF_data_wrong_data_type():
    with pytest.raises(NotBinaryFileError):
        read_RF('bmode.json', 1556, 256)
