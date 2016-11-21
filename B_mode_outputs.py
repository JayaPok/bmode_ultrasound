import matplotlib.pyplot as plt
import logging


def image_plot(B_mode_array, beam_spacing, axial_samples, num_beams, f_s, c):
    """Calculate Lateral distance and depth of image in meters using data
    from JSON file and display file using matplotlib

    :param B_mode_array: completed 2D numpy array of
     B-mode data that has undergone all image processing
    :param beam_spacing: distance between beams in meters
    :param axial_samples: # of samples in the axial direction
    :param num_beams: number of beams
    :param f_s: sampling frequency in Hz
    :param c: speed of sound
    :return: None
    """
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


def image_save(image_filename, B_mode_array, beam_spacing,
               axial_samples, num_beams, f_s, c):
    """Save B-mode image under specified file name

    :param image_filename: User specified filename to save B-mode image to
    :param B_mode_array: completed 2D numpy array of
     B-mode data that has undergone all image processing
    :param beam_spacing: distance between beams in meters
    :param axial_samples:  # of samples in the axial direction
    :param num_beams: number of beams
    :param f_s: sampling frequency in Hz
    :param c: speed of sound
    :return: None
    """

    try:
        lateral_distance = beam_spacing * num_beams
        depth_distance = c * axial_samples / f_s / 2
        extent_array = [0, lateral_distance, depth_distance, 0]
        plt.imshow(B_mode_array, aspect='auto',
                   extent=extent_array, cmap='Greys_r')
        plt.title('B-mode Ultrasound Image')
        plt.xlabel('Depth (m)')
        plt.ylabel('Distance (m)')
        plt.savefig(image_filename)
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
