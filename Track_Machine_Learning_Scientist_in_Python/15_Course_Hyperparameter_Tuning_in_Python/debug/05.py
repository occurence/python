import pandas as pd
import numpy as np
import csv

tree_viz_image = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\tree_viz_image.csv', header=None)

# Assuming tree_viz_image is a numpy array of shape (359, 747, 4)
with open('tree_viz_image.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    for row in tree_viz_image:
        # Iterate over each row and write it to the CSV file
        for i in range(row.shape[0]):
            writer.writerow(row[i])  # Writing each pixel as a row
