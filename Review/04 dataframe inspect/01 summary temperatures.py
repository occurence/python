import pandas as pd

temperatures = pd.read_csv(r'D:\STUDY\python\Review\04 dataframe inspect\temperatures.csv')

# Methods
print(temperatures.head())
print(temperatures.info())
print(temperatures.describe())
print(temperatures.isna().sum())
print(temperatures['country'].value_counts())

# Attributes
print(temperatures.values)
print(temperatures.columns)
print(temperatures.index)
print(temperatures.shape)

print(temperatures)

# Sort Rows
print(temperatures.sort_values('country', ascending=False).head(5))
# Subset Cols
print(temperatures[['date','city','avg_temp_c']])
# Subset Rows
print(temperatures[(temperatures['date'] < '2001') & (temperatures['city'] == 'Manila')])
# Subset Rows isin Categorical Variables
city = ["Manila", "Jakarta", "Singapore"]
print(temperatures[temperatures['city'].isin(city)])

# Add/Mutate/Transform/Feature Engineering/convert
temperatures['avg_temp_f'] = temperatures['avg_temp_c'] * 1.8 + 32
temperatures['avg_temp_k'] = (temperatures['avg_temp_f']) + 459.67 * 1.8
temp_winter = temperatures[temperatures['avg_temp_c'] <= 10]
temp_summer = temperatures[temperatures['avg_temp_c'] >= 20]
print(temp_winter)
print(temp_summer)

# Sort Rows, Subset Cols, Subset Rows, New Cols
temperatures['country_temp'] = temperatures['country'].map(temperatures['country'].value_counts(normalize=True))
country_winter_temp = temperatures[temperatures['avg_temp_c'] <= 10]
country_winter_temp_srt = country_winter_temp.sort_values('country_temp', ascending=False)
print(country_winter_temp_srt)

# Summary Statistics
print(temperatures['avg_temp_c'].mean())
print(temperatures['avg_temp_c'].median())
# Aggregate Functions
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
print(temperatures[["avg_temp_c"]].agg([iqr,'median']))

# Cumulative Statistics
manila = temperatures[(temperatures['city'] == 'Manila')]
manila = manila.sort_values('date', ascending=True)
manila['cum_manila_temp'] = manila['avg_temp_c'].cummax()
print(manila[["date", "avg_temp_c", "cum_manila_temp"]])

# Count, Remove Duplicates and Categorical
unique_city = temperatures.drop_duplicates(subset=['city','country'])
print(unique_city)
print(unique_city['city'].value_counts(sort=True))
print(unique_city['city'].value_counts(normalize=True))

# Manual Grouped Summary Statistics
print(temperatures[temperatures['city'] == 'Manila']['avg_temp_c'].mean())
print(temperatures[temperatures['city'] == 'Jakarta']['avg_temp_c'].mean())
print(temperatures[temperatures['city'] == 'Singapore']['avg_temp_c'].mean())
print(temperatures[temperatures['city'] == 'Bangkok']['avg_temp_c'].mean())
print(temperatures[temperatures['city'] == 'Tokyo']['avg_temp_c'].mean())

# Grouped Summary Statistics
print(temperatures.groupby('city')['avg_temp_c'].mean())

# Grouped Summary Statistics Agg
print(temperatures.groupby('city')['avg_temp_c'].agg(['min','max','sum']))
print(temperatures.groupby(['country','city'])[['avg_temp_c']].agg(['min','max','sum']))

# Pivot
print(temperatures.pivot_table(values='avg_temp_c', index='city'))
print(temperatures.pivot_table(values='avg_temp_c', index='city', aggfunc=['mean','median']))
print(temperatures.pivot_table(values='avg_temp_c', index='city', columns='country', fill_value=0, margins=True))

# Index
print(temperatures)
temperatures_ind = temperatures.set_index('city')
print(temperatures_ind)
print(temperatures_ind.reset_index())
print(temperatures_ind.reset_index(drop=True))

# Index Subset
cities = ["London", "Paris"]
temperatures_ind = temperatures.set_index(['city'])
print(temperatures[temperatures['city'].isin(cities)])
print(temperatures_ind.loc[cities])

# Index Multiple Tuples
temperatures_country_city = temperatures.set_index(['country','city'])
rows_to_keep = [('Brazil','Rio De Janeiro'), ('Pakistan','Lahore')]
print(temperatures_country_city.loc[rows_to_keep])

# Index Sort
print(temperatures_country_city.sort_index())
print(temperatures_country_city.sort_index(level=['city']))
print(temperatures_country_city.sort_index(level=['country','city'], ascending=[True,False]))

# Index Subset Sort Multiple Tuples
temperatures_srt = temperatures_country_city.sort_index()
print(temperatures_srt.loc['Pakistan':'Philippines'])
print(temperatures_srt.loc['Lahore':'Manila'])
print(temperatures_srt.loc[('Pakistan','Lahore'):('Philippines','Manila')])

# Index Subset Sort Slice Multiple Tuples
print(temperatures_srt.loc[('India','Hyderabad'):('Iraq','Baghdad')])
print(temperatures_srt.loc[:, 'date':'avg_temp_c'])
print(temperatures_srt.loc[('India','Hyderabad'):('Iraq','Baghdad'), 'date':'avg_temp_c'])

# Index Subset Sort Time
temperatures_bool = temperatures[(temperatures['date'] >= "2010-01-01") & (temperatures['date'] <= "2011-12-01")]
temperatures_time = temperatures.set_index('date').sort_index()
print(temperatures_time.loc['2010':'2011'])
print(temperatures_time.loc['2010-08-01':'2011-02-01'])

# Index Number
print(temperatures.iloc[22, 1])
print(temperatures.iloc[:5])
print(temperatures.iloc[:, 2:4])
print(temperatures.iloc[:5, 2:4])

# Pivot Subset Filter
temperatures['year'] = pd.to_datetime(temperatures['date']).dt.year
temp_by_country_city_vs_year = temperatures.pivot_table('avg_temp_c', index=['country', 'city'], columns='year')
temp_by_country_city_vs_year.loc['Egypt':'India']
temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi')]
temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi'),'2005':'2010']
mean_temp_by_year = temp_by_country_city_vs_year.mean(axis='index')
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis='columns')
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])