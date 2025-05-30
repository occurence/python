import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.restoration import inpaint

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

image_with_logo = plt.imread(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\22_Image_Processing_in_Python\datasets\Image Processing with Python course exercise dataset\chapter 3\image_with_logo.png')

# Initialize the mask
mask = np.zeros(image_with_logo.shape[:-1])

# Set the pixels where the logo is to 1
# mask[210:290, 360:425] = 1
mask[219:273, 364:418] = 1

# Apply inpainting to remove the logo
# image_logo_removed = inpaint.inpaint_biharmonic(image_with_logo, mask, multichannel=True)
# image_logo_removed = inpaint.inpaint_biharmonic(image_with_logo, mask)
image_logo_removed = inpaint.inpaint_biharmonic(image_with_logo, mask, channel_axis=-1)

# Show the original and logo removed images
show_image(image_with_logo, 'Image with logo')
show_image(image_logo_removed, 'Image with logo removed')
