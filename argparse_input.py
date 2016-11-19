import argparse as ap


def parse_cli():

    par = ap.ArgumentParser(formatter_class=ap.ArgumentDefaultsHelpFormatter)

    par.add_argument("--j",
                     dest="JSON_filename",
                     default="bmode.json",
                     help="input JSON data File Name")

    par.add_argument("--r",
                     dest="RF_data_filename",
                     default="rfdat.bin",
                     help="input RF Data file name")

    par.add_argument("--i",
                     dest="image_filename",
                     default="bmode.png",
                     help="input filename to save image to (include file format)")

    par.add_argument("--display",
                     dest="display",
                     help="Input True to display B-mode image using matplotlib and False to not display image",
                     default=False
                     )

    par.add_argument("--save",
                     dest="save",
                     default=True,
                     help="Input True to save B-mode image and False to not save")

    args = par.parse_args()

    return args


def main_args():

    args = parse_cli()
    JSON_filename = args.JSON_filename
    RF_data_filename = args.RF_data_filename
    image_filename = args.image_filename
    display = args.display
    save = args.save

    return (JSON_filename, RF_data_filename, image_filename, display, save)
