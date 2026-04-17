import pandas as pd

taiwan_real_estate = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\26_Course_Introduction_to_Regression_with_Statmodels_in_Python\datasets\taiwan_real_estate2.csv')

# Import seaborn with alias sns
import seaborn as sns

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Draw the scatter plot
sns.scatterplot(x='n_convenience', y='price_twd_msq', data=taiwan_real_estate)

# Show the plot
plt.show()

for index, (label, row) in enumerate(taiwan_real_estate.iterrows()):
    if index == 0:
        print(','.join(row.index))
        print(','.join(str(row[i]) for i in range(len(row))))
    else:
        print(','.join(str(row[i]) for i in range(len(row))))