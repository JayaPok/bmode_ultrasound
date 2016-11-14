import numpy as np


def read_RF(filename):
    rf_data = np.array(np.fromfile(filename, dtype='uint16', count=-1, sep=""))
    return rf_data


def RF_bars(rf_data, num_beams):
    rfdata_bars = np.split(rf_data, num_beams)
    return rfdata_bars
