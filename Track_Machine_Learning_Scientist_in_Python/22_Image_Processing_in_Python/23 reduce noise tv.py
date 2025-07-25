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

noisy_image = plt.imread(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\22_Image_Processing_in_Python\datasets\Image Processing with Python course exercise dataset\chapter 3\miny.jpeg')

# Import the module and function
from skimage.restoration import denoise_tv_chambolle

# Apply total variation filter denoising
# denoised_image = denoise_tv_chambolle(noisy_image, multichannel=True)
denoised_image = denoise_tv_chambolle(noisy_image)

# Show the noisy and denoised images
show_image(noisy_image, 'Noisy')
show_image(denoised_image, 'Denoised image')