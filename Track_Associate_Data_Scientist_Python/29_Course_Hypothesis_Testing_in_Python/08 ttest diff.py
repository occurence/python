import pandas as pd
import pingouin

sample_dem_data = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\29_Course_Hypothesis_Testing_in_Python\datasets\sample_dem_data.csv')

# Conduct a t-test on diff
test_results = pingouin.ttest(x=sample_dem_data['diff'],
                              y=0,
                              paired=True,
                              alternative='two-sided')

# Print the test results
print(test_results)