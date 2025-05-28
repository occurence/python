import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

page_image = plt.imread(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\22_Image_Processing_in_Python\datasets\Image Processing with Python course exercise dataset\chapter 1\page_image.jpg')
page_image = rgb2gray(page_image)

# Import the local threshold function
from skimage.filters import threshold_local

# Set the block size to 35
# block_size = 35
block_size = 21

# Obtain the optimal local thresholding
# local_thresh = threshold_local(page_image, block_size=block_size, offset=10)
local_thresh = threshold_local(page_image, block_size=block_size, offset=0.1)

# Obtain the binary image by applying local thresholding
binary_local = page_image > local_thresh

# Show the binary image
show_image(binary_local, 'Local thresholding')

print("Now you know that you should use local thresholding instead of global if the image has a wide variation of background intensity.")