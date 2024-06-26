import pandas as pd

diabetes_df = pd.read_csv('C:\Machine Learning\DataSets\diabetes.csv')

# Type of diabetes_df
print(f"\n {type(diabetes_df)} \n")

# Gives the top 5 rows of the data table
print(diabetes_df.head())

# Know the rows and columns present in the table
print("\n", diabetes_df.shape)