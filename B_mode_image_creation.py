import numpy as np


def envelope_detection(RF_array, n):
    RF_array_enveloped = np.empty([len(RF_array), len(RF_array[0])])
    RF_array_rectified = np.absolute(RF_array)
    for i in range(len(RF_array_rectified)):
        for j in range(len(RF_array_rectified[0])):
            if j < ((n-1) / 2):
                mov_avg = np.mean(RF_array_rectified[i][:(j + 1 + ((n-1) / 2))])
            elif j > (len(RF_array[0]) - 1 - ((n-1)/2)):
                mov_avg = np.mean(RF_array_rectified[i][j-2:])
            else:
                mov_avg = np.mean(RF_array_rectified[i][j - 2:j + 2])
            RF_array_enveloped[i][j] = mov_avg
    return (RF_array_enveloped)
