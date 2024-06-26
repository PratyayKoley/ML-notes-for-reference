import pandas as pd
from sklearn.datasets import fetch_california_housing

# Stored the data in a variable
california_data = fetch_california_housing();

# Created the dataframe
california_df = pd.DataFrame(california_data.data, columns= california_data.feature_names)

# Exported to CSV File
california_df.to_csv('C:\Machine Learning\DataSets\california_housing.csv')