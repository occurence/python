# Open a file as read-only and bind it to file
with open(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\19_Course_Introduction_to_Importing_Data_in_Python\datasets\moby_dick.txt', 'r') as file:
  	# Print it
    print(file.read())