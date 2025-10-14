# Import pickle package
import pickle

# Open pickle file and load data: d
with open(r'D:\STUDY\python\Review\13 import data\datasets\data.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))