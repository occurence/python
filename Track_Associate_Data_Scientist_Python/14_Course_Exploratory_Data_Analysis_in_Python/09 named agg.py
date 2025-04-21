import pandas as pd

unemployment = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\14_Course_Exploratory_Data_Analysis_in_Python\datasets\clean_unemployment.csv')

continent_summary = unemployment.groupby("continent").agg(
    # Create the mean_rate_2021 column
    mean_rate_2021=('2021', 'mean'),
    # Create the std_rate_2021 column
    std_rate_2021=('2021', 'std')
)
print(continent_summary)