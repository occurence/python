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

noisy_image = plt.imread(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\22_Image_Processing_in_Python\datasets\image.png')

# Import the module and function
from skimage.restoration import denoise_tv_chambolle

# Apply total variation filter denoising
# denoised_image = denoise_tv_chambolle(noisy_image, multichannel=True)
denoised_image = denoise_tv_chambolle(noisy_image)

# Show the noisy and denoised images
show_image(noisy_image, 'Noisy')
show_image(denoised_image, 'Denoised image')



import skimage.color
from skimage.filters import sobel

denoised_image = skimage.color.rgb2gray(denoised_image)

# # Apply edge detection filter
# edge_sobel = sobel(denoised_image)

# # Show original and resulting image to compare
# show_image(denoised_image, "Original")
# show_image(edge_sobel, "Edges with Sobel")


from skimage.feature import canny

canny_edges = canny(denoised_image)

# Show resulting image
show_image(canny_edges, "Edges with Canny")
show_image(canny(canny_edges, sigma=1.8), "Sigma of 1.8")
show_image(canny(canny_edges, sigma=2.2), "Sigma of 2.2")