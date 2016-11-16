import numpy as np
from statsmodels.nonparametric.smoothers_lowess import lowess


def array_filtering(RF_array):
    RF_array_abs = np.absolute(RF_array)
    RF_array_T = np.transpose(RF_array_abs)
    RF_array_filtered = np.empty([len(RF_array_T), len(RF_array_T[0])])
    x_data = np.array(range(len(RF_array_T)))
    for i in range(len(RF_array_T[0])):
        filtered = lowess(RF_array_T[:, i], x_data, frac=0.05)
        RF_array_filtered[:, i] = filtered[:, 1]
    return RF_array_filtered
