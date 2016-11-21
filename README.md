This project, "B-mode Ultrasound Imaging", takes in a binary radiofrequency (RF) ultrasound data file and a JSON text file containing RF data parameters, and returns a B-mode image represented by the RF data. The image is saved in the form of a PNG file which the user can input a desired file name.

How to Use:
1. Run the main_B_mode_file.py to run the program with the default data files and values
2. Can additionaly type the following optional inputs
--j (JSON filename, string) for entering custom JSON file
--r (Radio Frequency data filename) for entering custom RF binary data file
--i (image filename) for entering custom filename to save B-mode image to
--display (True or False) for showing the B-mode image
--save (True or False) for saving the B-mode image under the filename provided above with the optinal input argument --i

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
6. scikit-image - enables histogram equalization
7. logging - allows for logging of information with timestamps into the Logging_file.txt file
8. os - allows for using operating system dependent functionaity