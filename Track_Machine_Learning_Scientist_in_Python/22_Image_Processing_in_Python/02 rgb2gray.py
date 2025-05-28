import matplotlib.pyplot as plt

# Import the modules from skimage
from skimage import data, color

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

# Load the rocket image
rocket = data.rocket()

# Convert the image to grayscale
gray_scaled_rocket = color.rgb2gray(rocket)

# Show the original image
show_image(rocket, 'Original RGB image')

# Show the grayscale image
show_image(gray_scaled_rocket, 'Grayscale image')

print("You converted an image to grayscale. For many applications of image processing, color information doesn't help us identify important edges or other features. Something that we will cover later in the course.")