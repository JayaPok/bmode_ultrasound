from read_JSON import read_JSON_data


def test_read_JSON_data():
    c, fs, axial_samples, beam_spacing, num_beams = read_JSON_data('bmode.JSON')
    assert c == 1540
    assert fs == 40000000
    assert axial_samples == 1556
    assert beam_spacing == 0.00011746274509803921
    assert num_beams == 256
