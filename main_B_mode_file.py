from read_JSON import read_JSON_data
from read_RFdata import read_RF, RF_bars
from B_mode_image_creation import array_filtering, logarithmic_compression, equalization
from B_mode_outputs import image_save, image_plot
from argparse_input import main_args
import logging


if __name__ == "__main__":

    JSON_filename, RF_data_filename, image_filename, display, save = main_args()

    logging.basicConfig(filename='Logging_file.log',
                        filemode='w', level=logging.DEBUG,
                        format='%(asctime)s %(message)s')

    c, fs, axial_samples, beam_spacing, num_beams = read_JSON_data(JSON_filename)
    rf_data = read_RF(RF_data_filename, axial_samples, num_beams)
    rf_data_bars = RF_bars(rf_data, num_beams)
    rf_array_filtered = array_filtering(rf_data_bars)
    log_rf_array_filtered = logarithmic_compression(rf_array_filtered)
    RFarray_equalized = equalization(log_rf_array_filtered)
    if save:
        image_save(image_filename, RFarray_equalized)
    if display:
        image_plot(RFarray_equalized, beam_spacing, axial_samples, num_beams, fs, c)
