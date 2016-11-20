from B_mode_image_creation import array_filtering,\
    logarithmic_compression, equalization
from read_RFdata import RF_bars, read_RF
import numpy as np
from scipy import signal
from skimage import data, img_as_float, exposure


def test_array_filtering():
    a = read_RF('rfdat.bin', 1556, 256)
    b = RF_bars(a, 256)
    c = b[0:2]
    data_filtered = array_filtering(c)
    assert len(signal.find_peaks_cwt(data_filtered[:, 0],
                                     np.arange(1, 500))) < len(
        signal.find_peaks_cwt(c[0], np.arange(1, 500)))
    assert len(signal.find_peaks_cwt(data_filtered[:, 1],
                                     np.arange(1, 500))) < len(
        signal.find_peaks_cwt(c[1], np.arange(1, 500)))


def test_logarithmic_compression():
    sample_points = np.transpose([np.array([1, 2, 3, 4, 5]),
                                  np.array([6, 7, 8, 9, 10]),
                                  np.array([11, 12, 13, 14, 15])])
    log_RFarray_filtered = np.round(logarithmic_compression(sample_points), 2)
    assert np.any(log_RFarray_filtered) == np.any(np.round(np.log10(
        np.transpose([np.array([1, 2, 3, 4, 5]), np.array([6, 7, 8, 9, 10]),
                      np.array([11, 12, 13, 14, 1512])])), 2))


def test_equalization():
    sample_points_eq = np.transpose([np.array([1, 2, 3, 4, 5]),
                                     np.array([6, 7, 8, 9, 10]),
                                     np.array([11, 12, 13, 14, 15])])
    RFarray_equalized = np.round(equalization(sample_points_eq), 2)
    assert np.any(RFarray_equalized) == np.any(np.transpose(
        [np.array([0.2, 0.4, 0.6, 0.8, 0.1]),
         np.array([0.2, 0.4, 0.6, 0.8, 1]),
         np.array([0, 0, 0, 0, 0])]))
