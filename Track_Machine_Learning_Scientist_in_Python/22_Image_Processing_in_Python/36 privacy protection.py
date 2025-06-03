from skimage import data
from skimage.feature import Cascade
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from skimage import color, measure, filters
from skimage.color import rgb2gray
from skimage.restoration import inpaint
from skimage.feature import canny
from skimage.feature import corner_harris, corner_peaks
from skimage.segmentation import slic
from skimage.color import label2rgb
from skimage.filters import gaussian

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

def getFaceRectangle(d):
    ''' Extracts the face from the image using the coordinates of the detected image '''
    # X and Y starting points of the face rectangle
    x, y  = d['r'], d['c']
    
    # The width and height of the face rectangle
    width, height = d['r'] + d['width'],  d['c'] + d['height']
    
    # Extract the detected face
    face= group_image[ x:width, y:height]
    return face

def mergeBlurryFace(original, gaussian_image):
     # X and Y starting points of the face rectangle
    x, y  = d['r'], d['c']
    # The width and height of the face rectangle
    width, height = d['r'] + d['width'],  d['c'] + d['height']
    
    # original[ x:width, y:height] =  gaussian_image
    original[x:width, y:height] = (gaussian_image * 255).astype(np.uint8)
    return original

group_image = plt.imread(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\22_Image_Processing_in_Python\datasets\Image Processing with Python course exercise dataset\chapter 4\face_det25.jpg')
group_image = group_image.copy()
show_image(group_image)
trained_file = data.lbp_frontal_face_cascade_filename()
detector = Cascade(trained_file)

# Detect the faces
detected = detector.detect_multi_scale(img=group_image, 
                                       scale_factor=1.2, step_ratio=1, 
                                       min_size=(10, 10), max_size=(100, 100))
# For each detected face
for d in detected:  
    # Obtain the face rectangle from detected coordinates
    face = getFaceRectangle(d)
    
    # Apply gaussian filter to extracted face
    # blurred_face = gaussian(face, multichannel=True, sigma = 8)
    # blurred_face = gaussian(face, sigma = 8)
    blurred_face = gaussian(face, sigma=8, channel_axis=-1)
    
    # Merge this blurry face to our final image and show it
    resulting_image = mergeBlurryFace(group_image, blurred_face) 
show_image(resulting_image, "Blurred faces")