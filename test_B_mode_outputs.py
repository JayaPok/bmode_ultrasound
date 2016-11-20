from B_mode_outputs import image_save, image_plot
import numpy as np
import os
import pytest
import matplotlib.pyplot as plt

B_mode_array = np.absolute(np.empty([5, 5]))


# def test_image_plot():
#     output = image_plot(B_mode_array, 10, 100, 5, 100, 1000)
#     plt.close()
#     assert output == [0, 50, 500, 0]

def test_image_save():
    assert not os.path.isfile('bmode.png')
    image_save('bmode.png', B_mode_array)
    assert os.path.isfile('bmode.png')
    os.remove('bmode.png')


def test_image_save_wrong_type():
    with pytest.raises(ValueError):
        image_save('bmode.bmp', B_mode_array)
