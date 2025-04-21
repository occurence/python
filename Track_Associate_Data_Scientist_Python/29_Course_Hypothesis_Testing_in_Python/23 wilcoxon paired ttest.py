import pandas as pd
import pingouin

sample_dem_data = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\29_Course_Hypothesis_Testing_in_Python\datasets\sample_dem_data.csv')

# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results = pingouin.ttest(x=sample_dem_data['dem_percent_12'],
                                     y=sample_dem_data['dem_percent_16'],
                                     paired=True,
                                     alternative='two-sided') 

# Print paired t-test results
print(paired_test_results)