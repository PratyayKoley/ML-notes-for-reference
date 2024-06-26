import pandas as pd
from sklearn.datasets import fetch_california_housing

boston_dataset = fetch_california_housing()

print(type(boston_dataset))

print(boston_dataset)

# using pandas dataframe to display the data in tabular format 

boston_df = pd.DataFrame(boston_dataset.data, columns= boston_dataset.feature_names)

# Gives the top 5 rows of the data table
print("\n ", boston_df.head())

# Gives the last 5 rows of the data table
print(boston_df.tail())

# Know the rows and columns present in the table
print("\n ", boston_df.shape)

# Know the type of boston_df
print("\n", type(boston_df)) 