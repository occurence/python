import pandas as pd
import numpy as np

airlines = pd.read_csv(r'D:\STUDY\python\Review\14 clean data\datasets\airlines_final.csv', index_col=0)
categories = pd.read_csv(r'D:\STUDY\python\Review\14 clean data\datasets\airlines_categories.csv')

# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']

# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, 
                                labels = label_names)

# Create mappings and replace
mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday', 
            'Thursday': 'weekday', 'Friday': 'weekday', 
            'Saturday': 'weekend', 'Sunday': 'weekend'}

airlines['day_week'] = airlines['day'].replace(mappings)

print(airlines[['wait_min', 'wait_type', 'day', 'day_week']])