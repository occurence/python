import pandas as pd

airlines = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\20_Course_Cleaning_Data_in_Python\datasets\airlines_name.csv')

# Replace "Dr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Dr.","")

# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace('Mr.','')

# Replace "Miss" with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace('Miss','')

# Replace "Ms." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace('Ms.','')

# Assert that full_name has no honorifics
assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False

print(airlines)