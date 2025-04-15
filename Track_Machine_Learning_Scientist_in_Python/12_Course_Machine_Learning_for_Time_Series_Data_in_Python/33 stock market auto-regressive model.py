import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

prices = pd.read_csv(
    r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\prices_rolling.csv',
    index_col=0,
    parse_dates=True
)

# Visualize the dataset
prices.plot(legend=False)
plt.tight_layout()
plt.show()

# Count the missing values of each time series
missing_values = prices.isna().sum()
print(missing_values)

# Create a function we'll use to interpolate and plot
def interpolate_and_plot(prices, interpolation):

    # Create a boolean mask for missing values
    missing_values = prices.isna()

    # Interpolate the missing values
    prices_interp = prices.interpolate(interpolation)

    # Plot the results, highlighting the interpolated values in black
    fig, ax = plt.subplots(figsize=(10, 5))
    prices_interp.plot(color='k', alpha=.6, ax=ax, legend=False)
    
    # Now plot the interpolated values on top in red
    prices_interp[missing_values].plot(ax=ax, color='r', lw=3, legend=False)
    plt.show()

# Interpolate using the latest non-missing value
interpolation_type = 'zero'
interpolate_and_plot(prices, interpolation_type)

# Interpolate linearly
interpolation_type = 'linear'
interpolate_and_plot(prices, interpolation_type)

# Interpolate with a quadratic function
interpolation_type = 'quadratic'
interpolate_and_plot(prices, interpolation_type)

print("When you interpolate, the pre-existing data is used to infer the values of missing data. As you can see, the method you use for this has a big effect on the outcome.")

# Your custom function
def percent_change(series):
    # Collect all *but* the last value of this window, then the final value
    # previous_values = series[:-1]
    # last_value = series[-1]
    previous_values = series.iloc[:-1]
    last_value = series.iloc[-1]


    # Calculate the % difference between the last value and the mean of earlier values
    percent_change = (last_value - np.mean(previous_values)) / np.mean(previous_values)
    return percent_change

# Apply your custom function and plot
prices_perc = prices.rolling(20).apply(percent_change)
prices_perc.loc["2014":"2015"].plot()
plt.show()

print("You've converted the data so it's easier to compare one time point to another. This is a cleaner representation of the data.")

def replace_outliers(series):
    # Calculate the absolute difference of each timepoint from the series mean
    absolute_differences_from_mean = np.abs(series - np.mean(series))
    
    # Calculate a mask for the differences that are > 3 standard deviations from zero
    this_mask = absolute_differences_from_mean > (np.std(series) * 3)
    
    # Replace these values with the median accross the data
    series[this_mask] = np.nanmedian(series)
    return series

# Apply your preprocessing function to the timeseries and plot the results
prices_perc = prices_perc.apply(replace_outliers)
prices_perc.loc["2014":"2015"].plot()
plt.show()

print("Since you've converted the data to % change over time, it was easier to spot and correct the outliers.")

# Define a rolling window with Pandas, excluding the right-most datapoint of the window
prices_perc_rolling = prices_perc.rolling(20, min_periods=5, closed='right')

# Define the features you'll calculate for each window
# features_to_calculate = [np.min, np.max, np.mean, np.std]
features_to_calculate = ['min', 'max', 'mean', 'std']

# Calculate these features for your rolling window object
features = prices_perc_rolling.aggregate(features_to_calculate)

# Plot the results
ax = features.loc[:"2011-01"].plot()
prices_perc.loc[:"2011-01"].plot(ax=ax, color='k', alpha=.2, lw=3)
ax.legend(loc=(1.01, .6))
plt.show()

# Import partial from functools
from functools import partial
percentiles = [1, 10, 25, 50, 75, 90, 99]

# Use a list comprehension to create a partial function for each quantile
percentile_functions = [partial(np.percentile, q=percentile) for percentile in percentiles]

# Calculate each of these quantiles on the data using a rolling window
prices_perc_rolling = prices_perc.rolling(20, min_periods=5, closed='right')
features_percentiles = prices_perc_rolling.aggregate(percentile_functions)

# Plot a subset of the result
ax = features_percentiles.loc[:"2011-01"].plot(cmap=plt.cm.viridis)
ax.legend(percentiles, loc=(1.01, .5))
plt.show()

# print(prices_perc[1006:1510])
prices_perc_1415 = prices_perc.loc["2014":"2015", ['EBAY']]

# Extract date features from the data, add them as columns
prices_perc_1415['day_of_week'] = prices_perc_1415.index.weekday
# prices_perc_1415['week_of_year'] = prices_perc_1415.index.weekofyear
prices_perc_1415['week_of_year'] = prices_perc_1415.index.strftime('%U').astype(int)
prices_perc_1415['month_of_year'] = prices_perc_1415.index.month

# Print prices_perc_1415
print(prices_perc_1415)

prices_perc_lag = prices_perc.loc[:, ['AAPL']]
# print(type(prices_perc_lag))

# These are the "time lags"
shifts = np.arange(1, 11).astype(int)

# Use a dictionary comprehension to create name: value pairs, one pair per shift
# shifted_data = {"lag_{}_day".format(day_shift): prices_perc_lag.shift(day_shift) for day_shift in shifts}
shifted_data = {"lag_{}_day".format(day_shift): prices_perc_lag.shift(day_shift).iloc[:, 0] for day_shift in shifts}

# Convert into a DataFrame for subsequent use
prices_perc_shifted = pd.DataFrame(shifted_data)

# Plot the first 100 samples of each
ax = prices_perc_shifted.iloc[:100].plot(cmap=plt.cm.viridis)
# prices_perc_lag.iloc[:100].plot(color='r', lw=2)
prices_perc_lag.iloc[:100].plot(ax=ax, color='r', lw=2, label='AAPL')
ax.legend(loc='best')
plt.show()

# === TRANSFORMATION BEFORE THE ACTIVITY === #

prices_perc_hold = prices.rolling(20).apply(percent_change)
prices_perc_hold = prices['AAPL'].rolling(2).apply(percent_change)

prices_df = prices[['AAPL']]
prices_perc_hold2 = prices_df.pct_change()
prices_perc_shifted = pd.concat(
    # [prices_perc_hold2.shift(i).rename(columns={'AAPL': f'lag_{i}_day'}) for i in range(1, 11)],
    # [prices_perc_hold2.shift(i).fillna(method='ffill').rename(columns={'AAPL': f'lag_{i}_day'}) for i in range(1, 11)],
    [prices_perc_hold2.shift(i).ffill().rename(columns={'AAPL': f'lag_{i}_day'}) for i in range(1, 11)],
    axis=1
)


from sklearn.linear_model import Ridge

# Replace missing values with the median for each column
X = prices_perc_shifted.fillna(np.nanmedian(prices_perc_shifted))
y = prices_perc_hold.fillna(np.nanmedian(prices_perc_hold))

# Fit the model
model = Ridge()
model.fit(X, y)