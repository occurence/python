import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

defect_image = plt.imread(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\22_Image_Processing_in_Python\datasets\Image Processing with Python course exercise dataset\chapter 3\defect_image.png')
# defect_image = defect_image[:, :, :3]

def get_mask(image):
    '''Creates mask with defect regions'''
    mask = np.zeros(image.shape[:-1])
    # mask = np.zeros(image.shape[:2], dtype=bool)

    mask[18:59, 0:21] = 1
    mask[28:90, 313:355] = 1
    mask[159:180, 71:158] = 1
    mask[351:392, 71:92] = 1

    return mask

mask = get_mask(defect_image)
print(mask)
print("Image shape:", defect_image.shape)
print("Mask shape:", mask.shape)


# Import the module from restoration
from skimage.restoration import inpaint

# Show the defective image
show_image(defect_image, 'Image to restore')

# Apply the restoration function to the image using the mask
# restored_image = inpaint.inpaint_biharmonic(defect_image, mask, multichannel=True)
# restored_image = inpaint.inpaint_biharmonic(defect_image, mask)
restored_image = inpaint.inpaint_biharmonic(defect_image, mask, channel_axis=-1)
show_image(restored_image)

show_image(mask)