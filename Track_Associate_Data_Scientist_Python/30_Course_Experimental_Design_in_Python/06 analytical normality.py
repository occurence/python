import pandas as pd
from scipy.stats import shapiro
from scipy.stats import anderson

chicken_data = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\30_Course_Experimental_Design_in_Python\datasets\chick_weight.csv')

# Run a Shapiro-Wilk normality test on the weight column
test_statistic, p_value = shapiro(chicken_data['weight'])

print(f"p: {round(p_value, 4)} test stat: {round(test_statistic, 4)}")

if round(test_statistic, 4) <= 0.05:
    print("not normally distributed")
else:
    print("normally distributed")

# Run the Anderson-Darling test
result = anderson(x=chicken_data['weight'], dist='norm')

print(f"Test statistic: {round(result.statistic, 4)}")
print(f"Significance Levels: {result.significance_level}")
print(f"Critical Values: {result.critical_values}")

if round(result.statistic, 4) <= 0.05:
    print("The data does not come from a Normal distribution")
else:
    print("The data come from a Normal distribution")