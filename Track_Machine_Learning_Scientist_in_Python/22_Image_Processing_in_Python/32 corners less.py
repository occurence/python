import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from skimage import color, measure, filters
from skimage.color import rgb2gray
from skimage.restoration import inpaint
from skimage.feature import canny
from skimage.feature import corner_harris, corner_peaks

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

def show_image_with_corners(image, coords, title="Corners detected"):
    plt.figure(figsize=(12, 10))
    plt.imshow(image, interpolation='nearest', cmap='gray')
    plt.title(title)
    plt.plot(coords[:, 1], coords[:, 0], '+r', markersize=35)
    plt.axis('off')
    plt.show()
    plt.close()

building_image = plt.imread(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\22_Image_Processing_in_Python\datasets\Image Processing with Python course exercise dataset\chapter 4\corners_building_top.jpg')
show_image(building_image, "Original")
building_image = rgb2gray(building_image)
measure_image = corner_harris(building_image)

# Find the peaks with a min distance of 10 pixels
coords_w_min_10 = corner_peaks(measure_image, min_distance=10, threshold_rel=0.02)
print("With a min_distance set to 10, we detect a total", len(coords_w_min_10), "corners in the image.")

# Find the peaks with a min distance of 60 pixels
coords_w_min_60 = corner_peaks(measure_image, min_distance=60, threshold_rel=0.02)
print("With a min_distance set to 60, we detect a total", len(coords_w_min_60), "corners in the image.")

# Show original and resulting image with corners detected
show_image_with_corners(building_image, coords_w_min_10, "Corners detected with 10 px of min_distance")
show_image_with_corners(building_image, coords_w_min_60, "Corners detected with 60 px of min_distance")