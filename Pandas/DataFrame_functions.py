import pandas as pd
from sklearn.datasets import fetch_california_housing

# Storing data into variable
california_data = fetch_california_housing()

# Converting the dataset to Dataframe
california_df = pd.DataFrame(california_data.data, columns= california_data.feature_names)

# head() gives first five rows
print("\n", california_df.head())

# tail() gives last five rows
print("\n", california_df.tail())

# info() gives information about the DataFrame
print(california_df.info())

# isnull() gives whether any columns is null or not, returns a boolean value
print("\n", california_df.isnull())

# isnull().sum() gives the total number of null values in each column
print("\n", california_df.isnull().sum())

diabetes_df = pd.read_csv('C:\Machine Learning\DataSets\diabetes.csv')

# head() gives first five rows
print("\n", diabetes_df.head())

# value_counts() count the number of identical rows 
# Here diabetes_df contains all unique rows so it gives the rightmost column as value 1 meaning that particular row appeared only once in the dataframe
print("\n", diabetes_df.value_counts())

# value_counts(col_name) counts the number of identical rows based only on the column provided
# Here Outcome has value of only 1 or 0 so it displays the number of rows with value 1 and value 0
print("\n", diabetes_df.value_counts('Outcome'))

# groupby(col_name) groups the same rows together of a particular column
# col_name is compulsory or else groupby won't work
diabetes_grouped = diabetes_df.groupby('Outcome')

# After this grouping we can apply aggregate funcitons to it to see the result 
# mean() gives the mean of all columns based on the Outcome column value
print("\n", diabetes_grouped.mean())
