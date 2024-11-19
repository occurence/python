import pandas as pd
temperatures = pd.read_csv(r'D:\STUDY\python\Course_Data_Manipulation_Pandas\temperatures.csv')
temperatures['year'] = pd.to_datetime(temperatures['date']).dt.year
temp_by_country_city_vs_year = temperatures.pivot_table(values='avg_temp_c', index=['country','city'], columns='year')