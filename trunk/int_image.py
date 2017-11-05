from PIL import Image
import numpy as np

np.set_printoptions(linewidth = 200)

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

kevin1 = Image.open("../training_data/24x24/kevin_1.jpg")
kevin_grey = kevin1.convert("L")

kevin_grey.save("../training_data/24x24/kevin_grey.jpg")

pixel_list = list(kevin_grey.getdata())
SUB_WINDOW_SIZE_X = 24
SUB_WINDOW_SIZE_Y = 24

array = np.array(pixel_list, dtype=int)
array = array.reshape(SUB_WINDOW_SIZE_Y, SUB_WINDOW_SIZE_X)  
print array.sum()
integral_image = image_integrate(array, SUB_WINDOW_SIZE_Y, SUB_WINDOW_SIZE_X) 
print integral_image 
