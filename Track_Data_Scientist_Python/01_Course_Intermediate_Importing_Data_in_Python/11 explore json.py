import json

# Load JSON: json_data
with open(r"D:\STUDY\python\Track_Data_Scientist_Python\01_Course_Intermediate_Importing_Data_in_Python\datasets\a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k, v in json_data.items():
    if k in ['Title', 'Year']:
        print(k + ': ', v)