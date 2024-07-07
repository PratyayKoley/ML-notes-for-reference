import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Loads the data
breast_cancer = pd.read_csv('./DataSets/breast_cancer.csv')
iris = pd.read_csv('./DataSets/iris_data.csv')

# Displays the five rows of data
print(breast_cancer.head())
print(iris.head())

# Counting the number of values for the labelled rows in both dataset
print(breast_cancer['diagnosis'].value_counts())
print(iris['Species'].value_counts())

# Importing the label encoder
label_encoder = LabelEncoder()

# Tranforming the labels of diagnosis column of breast cancer
labels = label_encoder.fit_transform(breast_cancer['diagnosis'])

# Putting these tranform values to the table in a new column target by erasing the column diagnosis
breast_cancer['target'] = labels

print(breast_cancer['target'].value_counts())

# Tranforming the labels of diagnosis column of iris
labels = label_encoder.fit_transform(iris['Species'])

# Putting these tranform values to the table in a new column target by erasing the column diagnosis
iris['class'] = labels

print(iris['class'].value_counts())