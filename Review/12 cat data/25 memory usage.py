import pandas as pd

used_cars = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\cars_rating.csv')

print(used_cars['price_usd'].nbytes)
print(used_cars['price_usd'].astype('category').nbytes)

print(used_cars['drivetrain'].nbytes)
print(used_cars['drivetrain'].astype('category').nbytes)

print(used_cars['model_name'].nbytes)
print(used_cars['model_name'].astype('category').nbytes)