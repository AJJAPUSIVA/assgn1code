from helper_functions import *
from skimage import io

#-----------------------FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS--------------------------
datafolder = "assgn1code\images\2.jpg"
imgpath = datafolder + "1.jpg" 
#----------------------------------------STARTER CODE----------------------------------------
# Convert the color image to grayscale and returns the grayscale pixels 
pixel_values = read_colorimg(imgpath)
# The returned pixel values INCLUDE 2 boundary rows and 2 boundary colns. Therefore,
numb_rows = len(pixel_values) - 2
numb_colns = len(pixel_values[0]) - 2
#
#----------------------------------------WRITE YOUR CODE HERE----------------------------------------
# Create a data structure to store updated pixel information
temp = [0] * numb_colns
new_pixel_values = [temp] * numb_rows
# Define the 3 x 3 mask as a tuple of tuples
mask = [[0,0,0], [0,1,0], [0,0,0]]

# Implement a function to slice a part from the image as a 2D list
def get_slice_2d_list():
    slice_2d_list = []
    for i in len(pixel_values):
        for j in len(pixel_values):
            slice_2d_list = [pixel_values[i][j],]
        end
    return [slice_2d_list]



# Implement a function to flatten a 2D list or a 2D tuple
def flatten():
    list_1 = sum(slice_2d_list, [])
    list_2 = sum (mask, [])
    return []

# For each of the pixel values, excluding the boundary values
    # Create little local 3x3 box using list slicing
    neighbour_pixels = get_slice_2d_list()
    # Apply the mask
    mult_result = map(lambda slice_2d_list, mask:slice_2d_list*mask, list1, list2)        
    # Sum all the multiplied values and set the new pixel value
    sum(mult_result)
#        
#----------------------------------------END YOUR CODE HERE----------------------------------------
# Verify your result
verify_result(pixel_values, new_pixel_values, mask)
# View the original image and the edges of the image
view_images(imgpath, new_pixel_values)
