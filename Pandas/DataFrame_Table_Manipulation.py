from sklearn.datasets import fetch_california_housing
import pandas as pd

california_dataset = fetch_california_housing()

california_df = pd.DataFrame(california_dataset.data, columns= california_dataset.feature_names)

# Adding a column to california_df
california_df['Price'] = california_dataset.target

print("\n", california_df.head())

# Removing a row from california_df
row_drop = california_df.drop(index=0, axis=0)

print(row_drop)

# Removing a column from california_df
col_drop = california_df.drop(columns='AveOccup', axis=1)

print(col_drop)

# Locating a particular row
print(california_df.iloc[2])

# Locating a particular column
print(california_df.iloc[:,0])       # Prints the first column
print(california_df.iloc[:,1])       # Prints the second column
print(california_df.iloc[:,-1])       # Prints the last column

# Correlation 
print(california_df.corr())