import numpy as np
import matplotlib.pyplot as plt

# Load the cleaned CSV file
data = np.loadtxt(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\22_Image_Processing_in_Python\datasets\cleaned_damaged_image.csv', delimiter=',')
data = (data * 255).astype(np.uint8)

# Reshape and display
image = data.reshape((666, 666, 3))
plt.imshow(image.astype(np.uint8))
plt.axis('off')
plt.show()
print(image.shape)