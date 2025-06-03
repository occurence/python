input_path = r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\22_Image_Processing_in_Python\datasets\damaged_image.csv'
output_path = r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\22_Image_Processing_in_Python\datasets\cleaned_damaged_image.csv'

cleaned_lines = []

with open(input_path, 'r') as infile:
    for i, line in enumerate(infile, 1):
        # Remove brackets, whitespace, and newlines
        line = line.replace('[', '').replace(']', '').strip()
        
        # Split and remove empty strings caused by double commas
        parts = [v.strip() for v in line.split(',') if v.strip() != '']
        
        if len(parts) != 3:
            print(f"Skipping row {i} due to {len(parts)} values: {parts}")
            continue

        cleaned_lines.append(','.join(parts))

# Write to new cleaned file
with open(output_path, 'w') as outfile:
    outfile.write('\n'.join(cleaned_lines))
