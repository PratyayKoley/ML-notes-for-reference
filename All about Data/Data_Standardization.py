import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Loading the dataset from sklearn
breast_cancer_dataset = load_breast_cancer()

# Converting the dataset into a dataframe
breast_cancer_df = pd.DataFrame(breast_cancer_dataset.data, columns=breast_cancer_dataset.feature_names)

# Printing the first five rows and dataset shape
print("First five rows of the dataset:")
print(breast_cancer_df.head())
print("\nThe shape of the dataframe:", breast_cancer_df.shape)

# Splitting the data into X (features) and Y (target)
X = breast_cancer_df
Y = breast_cancer_dataset.target

# X is the variable which needs to be standardized i.e the dataframe values as all the values are in the range 10 or 17 or 1000 or 0 or 100

# Calculating the std of the dataframe
print("\n The std of the dataframe before standardization is : ", breast_cancer_dataset.data.std())

# The std of the dataframe before standardization is :  228.29740508276657

# As it should be 1 so performing standardization, but before it the data must split into training and testing data

# test_size tells the percentage of the original data to be used for testing here it is said that 20% of the data will be used
# random_state tells that for each different value of random_state the splitting of the data will be different. Using the same random_state value again will give you the same split of data that you obtained previously with that particular random_state.
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=3)

# Standardizing the training data
scaler = StandardScaler()
# scaler.fit(X_train)   Fits the data => Mean and std
# X_train_standardized = scaler.transform(X_train)  Transforms the data => Applies mean and std to original data

X_train_standardized = scaler.fit_transform(X_train)

# Standardizing the testing data using the same scaler object
X_test_standardized = scaler.transform(X_test)

# Printing standard deviations to verify standardization
print("\nStandard deviation of X_train_standardized:", X_train_standardized.std())
print("Standard deviation of X_test_standardized:", X_test_standardized.std())

# Standard deviation of X_train_standardized: 1.0
# Standard deviation of X_test_standardized: 0.8654541077212674