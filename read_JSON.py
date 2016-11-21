import json
import logging


def read_JSON_data(JSON_filename):
    """Import and read JSON file to determine speed of sound,
    sampling frequency, axial samples, beam spacing, and number of beams

    :param JSON_filename: User specified JSON file for ultrasound image data
    :return: c: speed of sound
    :return: fs: sampling frequency in Hz
    :return: axial_samples: # of samples in the axial direction
    :return: beam_spacing: distance between beams in meters
    :return: num_beams: number of beams
    """
    try:
        with open(JSON_filename, 'r') as f:
            JSON_dict = json.load(f)
            logging.debug("JSON file opened")
    except FileNotFoundError:
        print("File was not found")
        logging.error("File was not found")
        raise FileNotFoundError

    try:
        c = float(JSON_dict.get("c"))
        fs = float(JSON_dict.get("fs"))
        axial_samples = int(JSON_dict.get("axial_samples"))
        beam_spacing = float(JSON_dict.get("beam_spacing"))
        num_beams = int(JSON_dict.get("num_beams"))
        logging.info("speed of sound (meters/sec) = " + str(c))
        logging.info("sampling frequency = " + str(fs))
        logging.info("number of axial samples = " + str(axial_samples))
        logging.info("beam spacing (in meters) = " + str(beam_spacing))
        logging.info("number of beams = " + str(num_beams))
    except TypeError:
        print('One of the expected values was not found')
        logging.error("One of the expected values is missing")
        raise TypeError
    except ValueError:
        print('One of the expected values is not listed as an integer')
        logging.error("One of the expected values is not listed as a number")
        raise ValueError

    return (c, fs, axial_samples, beam_spacing, num_beams)
