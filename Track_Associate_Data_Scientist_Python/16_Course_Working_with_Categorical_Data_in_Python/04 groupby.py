import pandas as pd

adult = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\16_Course_Working_with_Categorical_Data_in_Python\datasets\adult.csv')

gb = adult.groupby(by=[ "Workclass",
                        "Above/Below 50k", 
                        "Education"])

print(gb.size())