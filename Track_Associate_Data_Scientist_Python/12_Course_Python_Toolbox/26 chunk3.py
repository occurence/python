def read_large_file(file_object):
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Open a connection to the file
with open(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\12_Course_Python_Toolbox\datasets\world_dev_ind.csv') as file:

    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

# Print            
print(counts_dict)