import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

building_image = plt.imread(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\22_Image_Processing_in_Python\datasets\Image Processing with Python course exercise dataset\chapter 2\building_image.jpg')

# Import Gaussian filter 
from skimage.filters import gaussian

# Apply filter
# gaussian_image = gaussian(building_image, multichannel=True)
gaussian_image = gaussian(building_image)

# Show original and resulting image to compare
show_image(building_image, "Original")
show_image(gaussian_image, "Reduced sharpness Gaussian")