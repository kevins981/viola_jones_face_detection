from PIL import Image
import numpy as np

from integral_img import * 

np.set_printoptions(linewidth = 200)

kevin1 = Image.open("../24x24/kevin_1.jpg")
kevin_grey = kevin1.convert("L")

kevin_grey.save("../24x24/kevin_grey.jpg")

pixel_list = list(kevin_grey.getdata())
SUB_WINDOW_SIZE_X = 24
SUB_WINDOW_SIZE_Y = 24

array = np.array(pixel_list, dtype=int)
#array = np.ones((24, 24), dtype=int) #new array to be returned 
array = array.reshape(SUB_WINDOW_SIZE_Y, SUB_WINDOW_SIZE_X)  
integral_image = image_integrate(array, SUB_WINDOW_SIZE_Y, SUB_WINDOW_SIZE_X) 
print integral_image
print array
print calc_sum((10,13), (10,16), (13,13), (13,16), integral_image)
 
	
