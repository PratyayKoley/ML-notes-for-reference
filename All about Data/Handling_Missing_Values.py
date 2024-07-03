import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# There are 2 ways to handle missing values in the dataset
# 1. Imputation => Filling the missing values by mean, median or mode
# 2. Dropping => Dropping all the rows which contain the missing values

# Loading the Placement dataset which contains the missing values
placement_data = pd.read_csv('./Datasets/Placement_Dataset.csv')

# Printing the top five rows
print(placement_data.head())

# Printing the number of rows and columns 
print(placement_data.shape)

# Printing the number of null values in the data
print(placement_data.isnull().sum())

# Plotting the placement data
sns.histplot(data=placement_data['salary'], kde=True)
plt.show()

# The plotting tells that the median or mode values can be considered.

# Imputing by median values :
placement_data['salary'].fillna(placement_data['salary'].median(), inplace=True)

# Checking the number of missing values
print(placement_data.isnull().sum())

# Imputing by mode values :
placement_data['salary'].fillna(placement_data['salary'].mode(), inplace=True)

# Checking the number of missing values
print(placement_data.isnull().sum())

# Dropping the missing values
placement_data.dropna(inplace=True)     # Put the values in the place instead of creating a copy
print(placement_data.isnull().sum())
print(placement_data.shape)
