import matplotlib.pyplot as plt
import numpy as np
from skimage.restoration import inpaint
from skimage import img_as_float
from skimage.io import imread

# Load the image and convert to float
defect_image = img_as_float(imread(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\22_Image_Processing_in_Python\datasets\Image Processing with Python course exercise dataset\chapter 3\defect_image.png'))

# Create a proper mask
def get_mask(image):
    '''Creates mask with defect regions'''
    mask = np.zeros(image.shape[:2], dtype=bool)

    mask[18:59, 0:21] = 1
    mask[28:90, 313:355] = 1
    mask[159:180, 71:158] = 1
    mask[351:392, 71:92] = 1

    return mask

mask = get_mask(defect_image)

# Apply inpainting
restored_image = inpaint.inpaint_biharmonic(defect_image, mask, channel_axis=-1)

# Plot
def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

show_image(defect_image, 'Image to restore')
show_image(mask, 'Mask')
show_image(restored_image, 'Image restored')
