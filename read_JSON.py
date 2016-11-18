import json


def read_JSON_data(filename):
    try:
        with open(filename, 'r') as f:
            JSON_dict = json.load(f)
    except FileNotFoundError:
        print("File was not found")
        raise FileNotFoundError

    try:
        c = float(JSON_dict.get("c"))
        fs = float(JSON_dict.get("fs"))
        axial_samples = int(JSON_dict.get("axial_samples"))
        beam_spacing = float(JSON_dict.get("beam_spacing"))
        num_beams = int(JSON_dict.get("num_beams"))
    except TypeError:
        print('One of the expected values was not found')
        raise TypeError
    except ValueError:
        print('One of the expected values is not listed as an integer')
        raise ValueError

    return (c, fs, axial_samples, beam_spacing, num_beams)
