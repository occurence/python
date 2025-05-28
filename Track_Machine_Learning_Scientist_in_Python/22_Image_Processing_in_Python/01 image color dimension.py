# import numpy as np
from skimage import data

coffee_image = data.coffee()
coins_image = data.coins()
# print(np.shape(coffee_image))

print(coffee_image.shape)
print(coins_image.shape)

print("! The coffee image is RGB-3 colored, that's why it has a 3 at the end, when displaying the shape (H, W, D) of it. While the coins image is grayscale and has a single color channel.")