from PIL import Image
import numpy as np

# Takes black and white original image and size of image, return integral image
def image_integrate(original_image, size_y, size_x):
	integral_image = np.zeros((size_y, size_x), dtype=int) #new array to be returned 
	for y in range(0, size_y):
		for x in range(0, size_x): 
			new_pixel_val = original_image[y, x] #reset
			if (x>0):
				new_pixel_val += integral_image[y, x-1]		
			if (y>0): 
				new_pixel_val += integral_image[y-1, x]	
			if (y>0 and x>0): 
				new_pixel_val -= integral_image[y-1, x-1]	

			integral_image[y, x] = new_pixel_val

	return integral_image

# Takes top left, top right, bottom left, bottom right coordinates of the rectangle and integral image. Returns sum of pixels values within the rectangle.  
def calc_sum(tleft, tright, bleft, bright, integral_img):
	if (type(tleft) != tuple or type(tright) != tuple or type(bleft) != tuple or type(bright) != tuple):
		raise TypeError("Coordiantes must be tuples in the format (x, y)")	
	if (tleft == (0, 0)):
		# Rectange start from top left	
		return integral_img[bright]

	elif (tleft[0] == 0):
		# Rectangle on the left edge of image
		bleft = (bleft[0], bleft[1]-1)
		return integral_img[bright]-integral_img[bleft]

	elif (tleft[1] == 0):
		# Rectangle on the top edge of image
		tright = (tright[0]-1, tright[1])
		return integral_img[bright]-integral_img[tright]

	else: 
		# Normal case
		bleft = (bleft[0], bleft[1]-1)		
		tright = (tright[0]-1, tright[1])		
		tleft = (tleft[0]-1, tleft[1]-1)
		return integral_img[bright]-integral_img[bleft]-integral_img[tright]+integral_img[tleft] 



