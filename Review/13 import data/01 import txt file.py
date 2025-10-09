# Open a file as read-only and bind it to file
with open(r'D:\STUDY\python\Review\13 import data\datasets\moby_dick.txt', 'r') as file:
  	# Print it
    print(file.read())