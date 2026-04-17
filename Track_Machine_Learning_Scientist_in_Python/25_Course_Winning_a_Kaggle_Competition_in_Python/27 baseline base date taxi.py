import pandas as pd

train = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\taxi_train_chapter_4.csv')
test = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\taxi_test_chapter_4.csv')

# Get pickup hour from the pickup_datetime column
train['hour'] = pd.to_datetime(train['pickup_datetime']).dt.hour
test['hour'] = pd.to_datetime(test['pickup_datetime']).dt.hour

# Calculate average fare_amount grouped by pickup hour 
hour_groups = train.groupby('hour')['fare_amount'].mean()

# Make predictions on the test set
test['fare_amount'] = test.hour.map(hour_groups)

# Write predictions
test[['id','fare_amount']].to_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\results\hour_mean_sub.csv', index=False)