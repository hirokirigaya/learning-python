import pandas as pd

data_series = pd.Series([10.2, -2, None, 15, 24.3])

print(data_series)  # return a series with the data
print('Data type:', data_series.dtypes)  # return the data type
# return if the values are unique
print('The values are unique:', data_series.is_unique)
print('Verify if has NaN:', data_series.hasnans)  # return if has NaN
print('How many values are:', data_series.count())  # return values exept NaN


# Analisys

# return the smallest value
print('What is the smallest value:', data_series.min())

# return the greatest value
print('What is the greatest value:', data_series.max())

# return arithmetic average
print('What is the arithmetic average:', data_series.mean())

# return standard deviation
print('What is the standard deviation:', data_series.std())

# return the media of the series
print('what is the median:', data_series.median())

# return the resume of the series
print('\nResume \n', data_series.describe())
