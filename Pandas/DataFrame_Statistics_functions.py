from sklearn.datasets import fetch_california_housing
import pandas as pd

california_data = fetch_california_housing()

california_df = pd.DataFrame(california_data.data, columns= california_data.feature_names)

# count() gives the number of values in each column
print("\n",california_df.count())

# mean() gives the mean values of each column
print("\n", california_df.mean())

# std() gives the standard deviation values of each column
print("\n", california_df.std())

# median() gives the median value of each column
print("\n", california_df.median())

# var() gives the variance value of each column
print("\n", california_df.var())

# min() gives the minimum value of each column
print("\n", california_df.min())

# max() gives the maximum value of each column
print("\n", california_df.max())

# sum() gives the total calculated value of each column
print("\n", california_df.sum())

# describe() is a shorthand function to get all the above data in a single table
print("\n", california_df.describe())