import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

# damaged_image = plt.imread(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\22_Image_Processing_in_Python\datasets\Image Processing with Python course exercise dataset\chapter 4\sally_damaged_image.jpg')
data = np.loadtxt(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\22_Image_Processing_in_Python\datasets\cleaned_damaged_image.csv', delimiter=',')
data = (data * 255).astype(np.uint8)
damaged_image = data.reshape((666, 666, 3))
show_image(damaged_image)

def get_mask(image):
    # Create mask with three defect regions: left, middle, right respectively
    mask_for_solution = np.zeros(image.shape[:-1])
    mask_for_solution[450:475, 470:495] = 1
    mask_for_solution[320:355, 140:175] = 1
    mask_for_solution[130:155, 345:370] = 1
    return mask_for_solution

# Import the necessary modules
from skimage.restoration import denoise_tv_chambolle, inpaint
from skimage import transform

# Transform the image so it's not rotated
upright_img = transform.rotate(damaged_image, 20)
show_image(upright_img)

# Remove noise from the image, using the chambolle method
# upright_img_without_noise = denoise_tv_chambolle(upright_img,weight=0.1, multichannel=True)
upright_img_without_noise = denoise_tv_chambolle(upright_img,weight=0.1, channel_axis=-1)
show_image(upright_img_without_noise)

# Reconstruct the image missing parts
mask = get_mask(upright_img)
mask = transform.resize(mask, upright_img_without_noise.shape[:2], preserve_range=True).astype(bool)
show_image(mask)

# result = inpaint.inpaint_biharmonic(upright_img_without_noise, mask, multichannel=True)
result = inpaint.inpaint_biharmonic(upright_img_without_noise, mask, channel_axis=-1)

show_image(result)