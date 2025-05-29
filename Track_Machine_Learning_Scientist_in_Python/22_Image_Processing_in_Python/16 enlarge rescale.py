import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

# Import the module and function to enlarge images
from skimage.transform import rescale

# Import the data module
from skimage import data

# Load the image from data
rocket_image = data.rocket()

# Enlarge the image so it is 3 times bigger
# enlarged_rocket_image = rescale(rocket_image, 3, anti_aliasing=True, multichannel=True)
enlarged_rocket_image = rescale(rocket_image, 3, anti_aliasing=True, channel_axis=-1)

# Show original and resulting image
show_image(rocket_image)
show_image(enlarged_rocket_image, "3 times enlarged image")