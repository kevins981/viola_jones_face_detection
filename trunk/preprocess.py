from PIL import Image
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import glob
import os
import re
SUB_WINDOW_SIZE_X=24 
SUB_WINDOW_SIZE_Y=24 

############
## COLOUR ##
############
preprocess_img_list = glob.glob('../24x24/grey/*.jpg') 
if not(os.path.isdir('../24x24/grey')):
    os.mkdir('../24x24/grey')
if not(os.path.isdir('../24x24/normalized')):
    os.mkdir('../24x24/normalized')

np.set_printoptions(linewidth = 400)

for preprocess_img in preprocess_img_list:
    preprocess_img_obj = Image.open(preprocess_img)
    matchObj = re.match(r'../24x24/grey\\(.*).jpg', preprocess_img)
    if matchObj:
        img_name = matchObj.group(1) 
        print img_name
    else:
	print "Error: file does not exists"	
	exit(1)

    # Convert img to list
    grey_pixel_list = list(preprocess_img_obj.getdata())
    # Convert list to numpy array
    grey_pixel_array = np.array(grey_pixel_list, dtype=float)
    # Turn 1D numpy array to 2D numpy array
    grey_pixel_array = grey_pixel_array.reshape(SUB_WINDOW_SIZE_Y, SUB_WINDOW_SIZE_X)  
    #####################
    ## GREY NORMALIZED ##
    #####################
    # Normalize mean and variance numpy array
    mean = np.mean(grey_pixel_array)
    std_var= np.std(grey_pixel_array)
    
    for pixel in np.nditer(grey_pixel_array, op_flags=['readwrite']):
        pixel[...] = (pixel-mean)/std_var
   
    old_max = np.amax(grey_pixel_array)
    old_min = np.amin(grey_pixel_array)
    print "max_pixel: "+str(old_max)
    print "min_pixel: "+str(old_min)
    new_max = 255.0
    new_min = 0

    for pixel in np.nditer(grey_pixel_array, op_flags=['readwrite']):
        pixel[...] = (pixel-old_min)*(new_max-new_min)/(old_max-old_min)+new_min 
    print grey_pixel_array

    grey_normalized_img = Image.fromarray(grey_pixel_array.astype('uint8'), "L")

    grey_normalized_img.save('../24x24/normalized/normalized_'+img_name+'.jpg')


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
