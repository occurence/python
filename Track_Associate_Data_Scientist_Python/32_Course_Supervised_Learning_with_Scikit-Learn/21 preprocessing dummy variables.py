import pandas as pd

music_df = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\32_Course_Supervised_Learning_with_Scikit-Learn\datasets\music_df.csv')

# Create music_dummies
music_dummies = pd.get_dummies(music_df, drop_first=True)

# Print the new DataFrame's shape
print("Shape of music_dummies: {}".format(music_dummies.shape))

print(music_dummies.info())

music_dummies = music_dummies.astype({col: 'uint8' for col in music_dummies.select_dtypes(include='bool').columns})

print(music_dummies.info())

print(music_dummies.head())