import json


def read_JSON_data(filename):

    with open(filename, 'r') as f:
        JSON_dict = json.load(f)

    c = JSON_dict.get("c")
    fs = JSON_dict.get("fs")
    axial_samples = JSON_dict.get("axial_samples")
    beam_spacing = JSON_dict.get("beam_spacing")
    num_beams = JSON_dict.get("num_beams")

    return (c, fs, axial_samples, beam_spacing, num_beams)
