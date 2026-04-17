import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

therapy_outcomes = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\30_Course_Experimental_Design_in_Python\datasets\therapy_outcomes.csv')

# Perform Tukey's HSD test
tukey_results = pairwise_tukeyhsd(
    therapy_outcomes['Anxiety_Reduction'], 
    therapy_outcomes['Therapy_Type'], 
    alpha=0.05
)

print(tukey_results)

print('ACT and CBT meandiff dont differ significantly from this experiment')