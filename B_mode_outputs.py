import matplotlib.pyplot as plt
import logging


def image_plot(B_mode_array, beam_spacing, axial_samples, num_beams, f_s, c):
    lateral_distance = beam_spacing * num_beams
    depth_distance = c * axial_samples / f_s / 2
    extent_array = [0, lateral_distance, depth_distance, 0]
    logging.info("Total Lateral Distance of image is " +
                 str(lateral_distance) + "meters")
    logging.info("Total Depth of image is " +
                 str(depth_distance) + "meters")
    plt.imshow(B_mode_array, aspect='auto',
               extent=extent_array, cmap='Greys_r')
    plt.title('B-mode Ultrasound Image')
    plt.xlabel('Depth (m)')
    plt.ylabel('Distance (m)')
    logging.debug("B-mode Ultrasound Image is plotted using matplotlib")
    plt.show()
    return extent_array


def image_save(image_filename, B_mode_array):
    try:
        plt.imsave(image_filename, B_mode_array, cmap='Greys_r')
        logging.debug("Image is saved under the filename: " + image_filename)
    except IOError:
        print('There is no more space, please delete something'
              ' on your hard-drive')
        logging.error("There is no space left on harddrive")
        raise IOError
    except ValueError:
        print('You used an nsupported file format. eps, jpeg,'
              ' jpg, pdf, pgf, png, ps, raw, rgba,'
              ' svg, svgz, tif, tiff are supported')
        logging.error("Attempted and failed to save using an"
                      " unsupported filetype")
        raise ValueError
