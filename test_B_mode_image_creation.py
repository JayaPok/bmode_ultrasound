from B_mode_image_creation import array_filtering, logarithmic_compression
from read_RFdata import RF_bars, read_RF
import numpy as np
from scipy import signal


def test_array_filtering():
    a = read_RF('rfdat.bin', 1556, 256)
    b = RF_bars(a, 256)
    c = b[0:2]
    data_filtered = array_filtering(c)
    assert len(signal.find_peaks_cwt(data_filtered[:, 0], np.arange(1, 500))) < len(
        signal.find_peaks_cwt(c[0], np.arange(1, 500)))
    assert len(signal.find_peaks_cwt(data_filtered[:, 1], np.arange(1, 500))) < len(
        signal.find_peaks_cwt(c[1], np.arange(1, 500)))


def test_logarithmic_compression():
    sample_points = np.transpose([np.array([1, 2, 3, 4, 5]), np.array([6, 7, 8, 9, 10]),
                                  np.array([11, 12, 13, 14, 15])])
    log_RFarray_filtered = np.round(logarithmic_compression(sample_points), 2)
    assert np.any(log_RFarray_filtered) == np.any(np.transpose([np.array([0, 0.3, 0.48, 0.6, 0.7]),
                                                                np.array([0.78, 0.85, 0.9, 0.95, 1]),
                                                                np.array([1.04, 1.08, 1.11, 1.15, 1.18])]))
