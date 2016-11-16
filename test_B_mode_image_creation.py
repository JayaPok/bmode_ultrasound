from B_mode_image_creation import array_filtering
from read_RFdata import RF_bars, read_RF
import numpy as np
from scipy import signal


def test_array_filtering():
    a = read_RF('rfdat.bin')
    b = RF_bars(a, 256)
    c = b[0:2]
    data_filtered = array_filtering(c)
    assert len(signal.find_peaks_cwt(data_filtered[:, 0], np.arange(1, 500))) < len(
        signal.find_peaks_cwt(c[0], np.arange(1, 500)))
    assert len(signal.find_peaks_cwt(data_filtered[:, 1], np.arange(1, 500))) < len(
        signal.find_peaks_cwt(c[1], np.arange(1, 500)))
