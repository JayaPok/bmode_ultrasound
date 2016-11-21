import numpy as np
import logging


class MissingDataError(Exception):
    pass


class NotBinaryFileError(Exception):
    pass


def read_RF(RF_data_filename, axial_samples, num_beams):
    """

    :param RF_data_filename: User specified binary file containing RF data
    :param axial_samples: # of samples in the axial direction
    :param num_beams: number of beams
    :return: rf_data: imported radio frequency data as a
     single array of integers
    """
    try:
        f = open(RF_data_filename, "rb")
    except FileNotFoundError:
        print("File was not found")
        logging.error("File was not found")
        raise FileNotFoundError

    try:
        rf_data = np.fromfile(RF_data_filename, dtype='int16', count=-1)

        textchars = bytearray({7, 8, 9, 10, 12, 13, 27} |
                              set(range(0x20, 0x100)) - {0x7f})
        is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))

        if is_binary_string(open(RF_data_filename, 'rb').read(1024)) == False:
            raise NotBinaryFileError
        if axial_samples*num_beams != len(rf_data):
            raise MissingDataError
        logging.debug("RF_data has been split into rows")
        return rf_data
    except MissingDataError:
        print('Not enough data values available.')
        logging.error("Not enough data values available.")
        raise
    except NotBinaryFileError:
        print('Not a binary file, please input a binary file.')
        logging.error("Not a binary file, please input a binary file.")
        raise


def RF_bars(rf_data, num_beams):
    """Split radio frequency array into an array or arrays of correct size

    :param rf_data: imported radio frequency data as a single array of integers
    :param num_beams: number of beams
    :return: rfdata_bars: 2D array of RF data of size (number
     of beams by number of axial samples)
    """
    rfdata_bars = np.split(rf_data, num_beams)
    logging.debug("RF_data has been split into rows")
    return rfdata_bars
