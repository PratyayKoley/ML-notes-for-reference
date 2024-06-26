import pandas as pd
from sklearn.datasets import fetch_california_housing

# Storing dataset values to a variable
california_data = fetch_california_housing()

# Converting the dataset to a dataframe (table with rows and columns)
california_df = pd.DataFrame(california_data.data, columns= california_data.feature_names)

# Converting the dataframe to an excel file
california_df.to_excel(r'C:\Machine Learning\DataSets\california_housing.xlsx')

# The library openpyxl is required by pandas to write Excel files. You can install it using pip.

