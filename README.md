This project, "B-mode Ultrasound Imaging", takes in a binary radiofrequency (RF) ultrasound data file and a JSON text file containing RF data parameters, and returns a B-mode image represented by the RF data. The image is saved in the form of a PNG file which the user can input a desired file name.

How to Use:
1. Run the main_B_mode_file.py to run the program with the default data files and values
2. Can additionaly type --j (filename) for entering custom JSON file, --r (filename) for entering custom RF binary data file, --i (filename) for entering filename to save image to, --display "display" for showing the B-mode image, --save "save" for saving the B-mode image

Contributers:
Aniruddh Prakash, Jaya Pokuri

Project License: 
See LICENSE.txt file

Packages Utilized:
1. argparse - enables user to enter custom specifications upon running
2. numpy - utilize MATLAB commands and features in the python environment
3. pytest - allows for testing exceptions and errors in test cases
4. statsmodels - enables envelope detection with lowess filters
5. matplotlib - enables plotting and showing of B-mode image to user
6. skimage - enables histogram equalization
7. logging - allows for logging of information with timestamps into the Logging_file.txt file