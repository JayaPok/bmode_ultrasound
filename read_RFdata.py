import numpy as np
import logging


def read_RF(filename):
    rf_data = np.fromfile(filename, dtype='int16', count=-1)
    logging.debug("Binary file of RF_data has been read")
    return rf_data


def RF_bars(rf_data, num_beams):
    rfdata_bars = np.split(rf_data, num_beams)
    logging.debug("RF_data has been split into rows")
    return rfdata_bars
