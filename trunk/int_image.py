from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from integral_img import * 


# Takes in 2D matrix, displays heat map
def plot_matrix(integral_image):
	print integral_image
	flattened = integral_image.flatten()
	flattened.sort()
	flattened = np.unique(flattened)
	min_value = flattened[1] # Minimum value excluding -999
	plt.imshow(integral_image, cmap='hot', interpolation='nearest', vmin=min_value, vmax=integral_image.max())
	plt.show()


np.set_printoptions(linewidth = 400)

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

# Record value of each feature in 5D matrix
# feature_vals(x, h, w, i, j)
# x:  representing Five Haar like patterns
# h:  height of feature 
# w:  width of feature 
# i:  y coordinate of the top left pixel of the feature
# j:  x coordinate of the top left pixel of the feature
# number of possible locations depends on the features size 
feature_vals = np.ndarray(shape=(6, 25, 25, 24, 24), dtype=int) 
feature_vals = np.full_like(feature_vals, -999)

# Type 1 Haar like feature
current_feature = 1
# Size 
for h in range(1, SUB_WINDOW_SIZE_Y+1):
	for w in xrange(2, SUB_WINDOW_SIZE_X+1, 2):
		#Location
		for i in range(0, SUB_WINDOW_SIZE_Y-h+1):
			for j in range(0, SUB_WINDOW_SIZE_X-w+1):
				#print "h: "+str(h)+" w: "+str(w)
				#print "i: "+str(i)+" j: "+str(j)
				#print "i: "+str(i)+" j+w-1: "+str(j+w-1)
				#print "i+w-1: "+str(i+w-1)+" j: "+str(j)
				#print "i+w-1: "+str(i+w-1)+" j+w-1: "+str(j+w-1)
				feature_vals[current_feature, h, w, i, j] = calc_sum((i, j+w/2), (i, j+w-1), (i+h-1, j+w/2), (i+h-1, j+w-1), integral_image) \
									  - calc_sum((i, j), (i, j+w/2-1), (i+h-1, j), (i+h-1, j+w/2-1), integral_image)

# Type 2 Haar like feature
current_feature = 2
# Size 
for h in range(1, SUB_WINDOW_SIZE_Y+1):
	for w in xrange(3, SUB_WINDOW_SIZE_X+1, 3):
		#Location
		for i in range(0, SUB_WINDOW_SIZE_Y-h+1):
			for j in range(0, SUB_WINDOW_SIZE_X-w+1):
				#print "h: "+str(h)+" w: "+str(w)
				#print "i: "+str(i)+" j: "+str(j)
				#print "i: "+str(i)+" j+w-1: "+str(j+w-1)
				#print "i+w-1: "+str(i+w-1)+" j: "+str(j)
				#print "i+w-1: "+str(i+w-1)+" j+w-1: "+str(j+w-1)
				feature_vals[current_feature, h, w, i, j] = - calc_sum((i, j), (i, j+w/3-1), (i+h-1, j), (i+h-1, j+w/3-1), integral_image) \
									    + calc_sum((i, j+w/3), (i, j+2*w/3-1), (i+h-1, j+w/3), (i+h-1, j+2*w/3-1), integral_image) \
									    - calc_sum((i, j+2*w/3), (i, j+w-1), (i+h-1, j+2*w/3), (i+h-1, j+w-1), integral_image) \

# Type 3 Haar like feature
current_feature = 3
# Size 
for h in xrange(2, SUB_WINDOW_SIZE_Y+1, 2):
	for w in range(1, SUB_WINDOW_SIZE_X+1):
		#Location
		for i in range(0, SUB_WINDOW_SIZE_Y-h+1):
			for j in range(0, SUB_WINDOW_SIZE_X-w+1):
				feature_vals[current_feature, h, w, i, j] = calc_sum((i, j), (i, j+w-1), (i+h/2-1, j), (i+h/2-1, j+w-1), integral_image) \
									  - calc_sum((i+h/2, j), (i+h/2, j+w-1), (i+h-1, j), (i+h-1, j+w-1), integral_image)

# Type 4 Haar like feature
current_feature = 4
# Size 
for h in xrange(3, SUB_WINDOW_SIZE_Y+1, 3):
	for w in range(1, SUB_WINDOW_SIZE_X+1):
		#Location
		for i in range(0, SUB_WINDOW_SIZE_Y-h+1):
			for j in range(0, SUB_WINDOW_SIZE_X-w+1):
				feature_vals[current_feature, h, w, i, j] = - calc_sum((i, j), (i, j+w-1), (i+h/3-1, j), (i+h/3-1, j+w-1), integral_image) \
									    + calc_sum((i+h/3, j), (i+h/3, j+w-1), (i+2*h/3-1, j), (i+2*h/3-1, j+w-1), integral_image) \
									    - calc_sum((i+2*h/3, j), (i+2*h/3, j+w-1), (i+h-1, j), (i+h-1, j+w-1), integral_image) \

# Type 5 Haar like feature
current_feature = 5
# Size 
for h in xrange(2, SUB_WINDOW_SIZE_Y+1, 2):
	for w in xrange(2, SUB_WINDOW_SIZE_X+1, 2):
		#Location
		for i in range(0, SUB_WINDOW_SIZE_Y-h+1):
			for j in range(0, SUB_WINDOW_SIZE_X-w+1):
				feature_vals[current_feature, h, w, i, j] = - calc_sum((i, j), (i, j+w/2-1), (i+h/2-1, j), (i+h/2-1, j+w/2-1), integral_image) \
									    + calc_sum((i, j+w/2), (i, j+w-1), (i+h/2-1, j+w/2), (i+h/2-1, j+w-1), integral_image) \
									    - calc_sum((i+h/2, j+w/2), (i+h/2, j+w-1), (i+h-1, j+w/2), (i+h-1, j+w-1), integral_image) \
									    + calc_sum((i+h/2, j), (i+h/2, j+w/2-1), (i+h-1, j), (i+h-1, j+w/2-1), integral_image) \

plot_matrix(feature_vals[5, 20, 16])
