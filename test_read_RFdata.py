from read_RFdata import read_RF

def test_read_RFdata():
	import numpy as np
	
	bin_data = read_RF('test.bin')

	assert bin_data == np.array([770])
