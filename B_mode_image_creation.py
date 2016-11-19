import numpy as np
from statsmodels.nonparametric.smoothers_lowess import lowess
from skimage import data, img_as_float, exposure


def array_filtering(RF_array):
    RF_array_abs = np.absolute(RF_array)
    RF_array_T = np.transpose(RF_array_abs)
    RF_array_filtered = np.empty([len(RF_array_T), len(RF_array_T[0])])
    x_data = np.array(range(len(RF_array_T)))
    for i in range(len(RF_array_T[0])):
        filtered = lowess(RF_array_T[:, i], x_data, frac=0.05)
        RF_array_filtered[:, i] = filtered[:, 1]
    return RF_array_filtered


def logarithmic_compression(RF_array_filtered):
    log_RFarray_filtered = np.empty([len(RF_array_filtered), len(RF_array_filtered[0])])
    for i in range(len(RF_array_filtered[0])):
        log_RFarray_filtered[:, i] = np.log10(RF_array_filtered[:, i])
    return log_RFarray_filtered

def equalization(log_RFarray_filtered):
    RFarray_equalized = np.empty([len(log_RFarray_filtered), len(log_RFarray_filtered[0])])
    for i in range(len(log_RFarray_filtered[0])-1):
    	ind = np.where(~np.isnan(log_RFarray_filtered[:, i]))[0]
    	first, last = ind[0], ind[-1]
    	log_RFarray_filtered[:, i][:first] = log_RFarray_filtered[:, i][first]
    	log_RFarray_filtered[:, i][last + 1:] = log_RFarray_filtered[:, i][last]
    	RFarray_equalized[:, i] = exposure.equalize_hist(log_RFarray_filtered[:, i])
    return RFarray_equalized

