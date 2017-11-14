from PIL import Image
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import re
SUB_WINDOW_SIZE_X=24 
SUB_WINDOW_SIZE_Y=24 

############
## COLOUR ##
############
colour_img_list = glob.glob('../24x24/color/*.jpg') 
if not(os.path.isdir('../24x24/grey')):
	os.mkdir('../24x24/grey')
if not(os.path.isdir('../24x24/normalized')):
	os.mkdir('../24x24/normalized')

for colour_img in colour_img_list:

	colour_img_obj = Image.open(colour_img)
	matchObj = re.match(r'../24x24/color\\(.*).jpg', colour_img)
	if matchObj:
		img_name = matchObj.group(1) 
		print img_name
	else:
		print "Error: file does not exists"	
		exit(1)

	##########
	## GREY ##
	##########
	# Convert to 8 bit grey scale img
	grey_img = colour_img_obj.convert("L")
	grey_img.save('../24x24/grey/grey_'+img_name+'.jpg')
	# Convert img to list
	grey_pixel_list = list(grey_img.getdata())
	# Convert list to numpy array
	grey_pixel_array = np.array(grey_pixel_list, dtype=float)
	# Turn 1D numpy array to 2D numpy array
	grey_pixel_array = grey_pixel_array.reshape(SUB_WINDOW_SIZE_Y, SUB_WINDOW_SIZE_X)  
	#print grey_pixel_array 

	#####################
	## GREY NORMALIZED ##
	#####################
	# Normalize mean and variance numpy array
	grey_pixel_array_scaled = preprocessing.scale(grey_pixel_array)
	# Rescale so the normalized imgs are viewable	
	myscaler = MinMaxScaler((0, 255))
	myscaler.fit(grey_pixel_array_scaled) 
	grey_normalized_rescaled = myscaler.transform(grey_pixel_array_scaled) 
	# Convert normalized numpy array to normalized greyscale img
	grey_normalized_rescaled_img = Image.fromarray(grey_normalized_rescaled.astype('uint8'), "L")
	grey_normalized_rescaled_img.save('../24x24/normalized/normalized_'+img_name+'.jpg')




