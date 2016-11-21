import numpy as np
from statsmodels.nonparametric.smoothers_lowess import lowess
from skimage import data, img_as_float, exposure
import logging


def array_filtering(rfdata_bars):
    """Run envelope detection on individual beams using a lowess filter of a 2D numpy array of RF data

    :param rfdata_bars: 2D array of RF data of size
    :return: RF_array_filtered: 2D numpy array of data that has undergone envelope detection
    """
    RF_array_abs = np.absolute(rfdata_bars)
    RF_array_T = np.transpose(RF_array_abs)
    RF_array_filtered = np.empty([len(RF_array_T), len(RF_array_T[0])])
    x_data = np.array(range(len(RF_array_T)))
    for i in range(len(RF_array_T[0])):
        filtered = lowess(RF_array_T[:, i], x_data, frac=0.05)
        RF_array_filtered[:, i] = filtered[:, 1]
    logging.debug("RF_data has undergone envelope detection")
    return RF_array_filtered


def logarithmic_compression(RF_array_filtered):
    """Run logarithmic compression on a 2D numpy array of RF data

    :param RF_array_filtered: 2D numpy array of data that has undergone envelope detection
    :return: log_RFarray_filtered: 2D numpy array of data that has
    undergone logarithmic compression and envelope detection
    """
    log_RFarray_filtered = np.empty([len(RF_array_filtered),
                                     len(RF_array_filtered[0])])
    for i in range(len(RF_array_filtered[0])):
        log_RFarray_filtered[:, i] = np.log10(RF_array_filtered[:, i])
    logging.debug("RF_data has undergone logarithmic compression")
    return log_RFarray_filtered


def equalization(log_RFarray_filtered):
    """"Run histogram equalization on a 2D array of RF data that has undergone
    envelope detection and logarithmic compression

    :param log_RFarray_filtered: 2D numpy array of data that has
     undergone logarithmic compression and envelope detection
    :return: B_mode_array: completed 2D numpy array of B-mode data that has undergone all image processing
    """
    B_mode_array = np.empty([len(log_RFarray_filtered), len(log_RFarray_filtered[0])])
    for i in range(len(log_RFarray_filtered[0])-1):
        ind = np.where(~np.isnan(log_RFarray_filtered[:, i]))[0]
        first, last = ind[0], ind[-1]
        log_RFarray_filtered[:, i][:first] =\
            log_RFarray_filtered[:, i][first]
        log_RFarray_filtered[:, i][last + 1:] =\
            log_RFarray_filtered[:, i][last]
        B_mode_array[:, i] =\
            exposure.equalize_hist(log_RFarray_filtered[:, i])
    logging.debug("RF_data has undergone histogram equalization")
    return B_mode_array
