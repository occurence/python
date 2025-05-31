import csv
import pandas as pd


mask = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\22_Image_Processing_in_Python\datasets\defect_image_mask.csv').to_numpy()

# Replace 'output.csv' with your desired filename
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow([f'col_{i}' for i in range(mask.shape[1])])

    # Write the data rows
    for row in mask:
        # Ensure commas in values are removed or replaced to avoid CSV formatting issues
        clean_row = [str(value).replace(',', '') for value in row]
        writer.writerow(clean_row)
