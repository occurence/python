import pandas as pd
import random

attrition_pop = pd.read_feather(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\28_Course_Sampling_in_Python\datasets\attrition.feather')
attrition_srs = attrition_pop.sample(frac=0.25, random_state=2022)
attrition_strat = attrition_pop.groupby('RelationshipSatisfaction').sample(frac=0.25, random_state=2022)
satisfaction_unique = list(attrition_pop['RelationshipSatisfaction'].unique())
satisfaction_samp = random.sample(satisfaction_unique, k=2)
satis_condition = attrition_pop['RelationshipSatisfaction'].isin(satisfaction_samp)
attrition_clust_prep = attrition_pop[satis_condition]
attrition_clust_prep['RelationshipSatisfaction'] = attrition_clust_prep['RelationshipSatisfaction'].cat.remove_unused_categories()
attrition_clust = attrition_clust_prep.groupby('RelationshipSatisfaction').sample(n=len(attrition_pop) // 4, random_state=2022)
# attrition_clust = attrition_clust_prep.groupby('RelationshipSatisfaction').apply(
#     lambda group: group.sample(n=min(len(group), len(attrition_pop) // 4), random_state=2022))








# Mean Attrition by RelationshipSatisfaction group
mean_attrition_pop = attrition_pop.groupby('RelationshipSatisfaction')['Attrition'].mean()

# Print the result
print(mean_attrition_pop)

# Calculate the same thing for the simple random sample 
mean_attrition_srs = attrition_srs.groupby('RelationshipSatisfaction')['Attrition'].mean()

# Print the result
print(mean_attrition_srs)

# Calculate the same thing for the stratified sample 
mean_attrition_strat = attrition_strat.groupby('RelationshipSatisfaction')['Attrition'].mean()

# Print the result
print(mean_attrition_strat)

# Calculate the same thing for the cluster sample 
mean_attrition_clust = attrition_clust.groupby('RelationshipSatisfaction')['Attrition'].mean()

# Print the result
print(mean_attrition_clust)