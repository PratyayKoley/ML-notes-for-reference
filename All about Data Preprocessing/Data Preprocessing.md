# Data

## Data Collection sites for Machine Learning

1. [Kaggle](https://www.kaggle.com/)
2. [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
3. [Google Dataset Search](https://datasetsearch.research.google.com/)

## Handling Missing values in the dataset

The values in the dataset can be empty in some places but we can't feed such data to the model which contains null or empty values. We have to handle such data.

1. Imputation => Filling the missing values by mean, median or values. Used often when the dataset is small consisting of small number of rows and cols.
2. Dropping => Dropping all the rows which contain the missing values. Used usually when the dataset is very large in numbers of lakhs or thousands of rows.

## Loading the csv file 'Placement' and performing opeartions on it

```python
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
```

#### Output

| sl_no | gender | ssc_p | ssc_b   | hsc_p | hsc_b   | hsc_s    | degree_p | degree_t  | workex | etest_p | specialisation | mba_p | status     | salary   |
| ----- | ------ | ----- | ------- | ----- | ------- | -------- | -------- | --------- | ------ | ------- | -------------- | ----- | ---------- | -------- |
| 1     | M      | 67.00 | Others  | 91.00 | Others  | Commerce | 58.00    | Sci&Tech  | No     | 55.0    | Mkt&HR         | 58.80 | Placed     | 270000.0 |
| 2     | M      | 79.33 | Central | 78.33 | Others  | Science  | 77.48    | Sci&Tech  | Yes    | 86.5    | Mkt&Fin        | 66.28 | Placed     | 200000.0 |
| 3     | M      | 65.00 | Central | 68.00 | Central | Arts     | 64.00    | Comm&Mgmt | No     | 75.0    | Mkt&Fin        | 57.80 | Placed     | 250000.0 |
| 4     | M      | 56.00 | Central | 52.00 | Central | Science  | 52.00    | Sci&Tech  | No     | 66.0    | Mkt&HR         | 59.43 | Not Placed | NaN      |
| 5     | M      | 85.80 | Central | 73.60 | Central | Commerce | 73.30    | Comm&Mgmt | No     | 96.8    | Mkt&Fin        | 55.50 | Placed     | 425000.0 |

    (215, 15)

    sl_no              0
    gender             0
    ssc_p              0
    ssc_b              0
    hsc_p              0
    hsc_b              0
    hsc_s              0
    degree_p           0
    degree_t           0
    workex             0
    etest_p            0
    specialisation     0
    mba_p              0
    status             0
    salary            67

This means that out of 215 rows in total there are 67 rows which contains null values for the salary column. These `67 rows` can be imputed by placing mean, median or mode values of salary column to it.

`Mean` : It is used when the data is normally distributed, it has no outliers or skewed.  
Example : For salary data, if the salaries are normally distributed, you might use the mean to fill in missing values.

`Median` : It is used when the data has outliers or is skewed.  
Example : For house prices or income data, where a few high or low values can skew the mean, the median is a better choice.

`Mode` : It is used when the most frequent category is the most logical replacement.  
Example : For gender, work experience, or any other categorical variable, the mode is used.

### What are outliers or skewed ?

![Skewed/Normaml](https://cdn.prod.website-files.com/5ff66329429d880392f6cba2/6466495a070b0a9f5a9e1798_648%20Preview.jpg)

![Outliers](https://vitalflux.com/wp-content/uploads/2023/05/Outlier-detection-Python-Machine-Learning.png)

### Plotting the salary column of Placement dataset to know that the 67 missing values must be imputed by mean, median or mode

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# There are 2 ways to handle missing values in the dataset
# 1. Imputation => Filling the missing values by mean, median or mode
# 2. Dropping => Dropping all the rows which contain the missing values

# Loading the Placement dataset which contains the missing values
placement_data = pd.read_csv('./Datasets/Placement_Dataset.csv')

# Plotting the placement data
sns.histplot(data=placement_data['salary'], kde=True)
plt.show()
```

#### Output

![Salary Plotting](./Images/Salary%20Plotting.png)

### Seeing the plot it can be seen that the plot is not distributed normally so we cannot impute the missing values by mean. So imputing them by median and mode values.

1.  Imputing by median value :

    ```python
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    # There are 2 ways to handle missing values in the dataset
    # 1. Imputation => Filling the missing values by mean, median or mode
    # 2. Dropping => Dropping all the rows which contain the missing values

    # Loading the Placement dataset which contains the missing values
    placement_data = pd.read_csv('./Datasets/Placement_Dataset.csv')

    # The plotting tells that the median or mode values can be considered.
    # Imputing by median values :
    placement_data['salary'].fillna(placement_data['salary'].median(), inplace=True)

    # Checking the number of missing values
    print(placement_data.isnull().sum())
    ```

2.  Imputing by mode value :

    ```python
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    # There are 2 ways to handle missing values in the dataset
    # 1. Imputation => Filling the missing values by mean, median or mode
    # 2. Dropping => Dropping all the rows which contain the missing values

    # Loading the Placement dataset which contains the missing values
    placement_data = pd.read_csv('./Datasets/Placement_Dataset.csv')

    # The plotting tells that the median or mode values can be considered.
    # Imputing by mode values :
    placement_data['salary'].fillna(placement_data['salary'].mode(), inplace=True)

    # Checking the number of missing values
    print(placement_data.isnull().sum())
    ```

    #### Output

        sl_no             0
        gender            0
        ssc_p             0
        ssc_b             0
        hsc_p             0
        hsc_b             0
        hsc_s             0
        degree_p          0
        degree_t          0
        workex            0
        etest_p           0
        specialisation    0
        mba_p             0
        status            0
        salary            0

### Dropping the missing values from dataset :

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# There are 2 ways to handle missing values in the dataset
# 1. Imputation => Filling the missing values by mean, median or mode.
# 2. Dropping => Dropping all the rows which contain the missing values.

# Loading the Placement dataset which contains the missing values
placement_data = pd.read_csv('./Datasets/Placement_Dataset.csv')

# Dropping the missing values
placement_data.dropna(inplace=True)     # Put the values in the place instead of creating a copy
print(placement_data.isnull().sum())
print(placement_data.shape)
```

#### Output

    sl_no             0
    gender            0
    ssc_p             0
    ssc_b             0
    hsc_p             0
    hsc_b             0
    hsc_s             0
    degree_p          0
    degree_t          0
    workex            0
    etest_p           0
    specialisation    0
    mba_p             0
    status            0
    salary            0
    dtype: int64

    (148, 15)

As we can see that the shape has been reduced from 215 to 148 i.e. 215 - 67 = 148

## Data Standardization: An Important Preprocessing Step

**Data standardization** is a crucial preprocessing step to ensure that the data is **scaled** and **centralized** properly.

<span style="font-size: 1.2em; font-weight: bold;">What do you actually mean by scaled and centralized ?</span>

- **Scaled:** Scaling involves adjusting the range of the data so that it fits within a specific scale, often with a standard deviation of one.
- **Centralized:** Centralization involves adjusting the data so that its mean is zero.

By standardizing your data, you improve the performance of many machine learning algorithms and models.

### The steps to be followed for the data standardization is :

- See for any missing values in the dataset. If exists, handle the missing values by imputating the rows or dropping the rows.

  ```python
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
  ```

  #### Output

  First five rows of the dataset:
  | | mean radius | mean texture | mean perimeter | mean area | mean smoothness | ... | worst compactness | worst concavity | worst concave points | worst symmetry | worst fractal dimension |
  | --- | ----------- | ------------ | -------------- | --------- | --------------- | --- | ----------------- | --------------- | -------------------- | -------------- | ----------------------- |
  | 0 | 17.99 | 10.38 | 122.80 | 1001.0 | 0.11840 | ... | 0.6656 | 0.7119 | 0.2654 | 0.4601 | 0.11890 |
  | 1 | 20.57 | 17.77 | 132.90 | 1326.0 | 0.08474 | ... | 0.1866 | 0.2416 | 0.1860 | 0.2750 | 0.08902 |
  | 2 | 19.69 | 21.25 | 130.00 | 1203.0 | 0.10960 | ... | 0.4245 | 0.4504 | 0.2430 | 0.3613 | 0.08758 |
  | 3 | 11.42 | 20.38 | 77.58 | 386.1 | 0.14250 | ... | 0.8663 | 0.6869 | 0.2575 | 0.6638 | 0.17300 |
  | 4 | 20.29 | 14.34 | 135.10 | 1297.0 | 0.10030 | ... | 0.2050 | 0.4000 | 0.1625 | 0.2364 | 0.07678 |

  [5 rows x 30 columns]

  The shape of the dataframe: (569, 30)

    <hr>

- Split the original data into training and testing data.

  ```python
  # Splitting the data into X (features i.e independent variable) and Y (target i.e dependent variable on features)
  X = breast_cancer_df
  Y = breast_cancer_dataset.target

  # X is the variable which needs to be standardized i.e the dataframe values as all the values are in the range 10 or 17 or 1000 or 0 or 100

  # Calculating the std of the dataframe
  print("\n The std of the dataframe before standardization is : ", breast_cancer_dataset.data.std())

  # test_size tells the percentage of the original data to be used for testing here it is said that 20% of the data will be used

  # random_state tells that for each different value of random_state the splitting of the data will be different. Using the same random_state value again will give you the same split of data that you obtained previously with that particular random_state.
  X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=3)
  ```

  #### Output

  The std of the dataframe before standardization is : 228.29740508276657  
  As it should be 1 so performing standardization

    <hr>

- Identify the standardization techniques :

  1.  **StandardScaler** : Computes the mean and standard deviation from dataset. Used for Normal Distribution of data.
  2.  **MinMaxScaler** : Scales the column between a given range, generally between 0 and 1. Used when we need Fixed Range data.
  3.  **RobustScaler** : Computes the median and the interqurtile range. Generally used for dataset with outliers.

  ```python
  # Standardizing the training data
  scaler = StandardScaler()
  ```

    <hr>

- Fit and Tranform the original data :

  1.  **Fitting the data** : When you fit the StandardScaler to the training data, it calculates the mean and standard deviation for each feature in the training set. These values are stored in a variable for further usage.

  2.  **Transforming the data** : After fitting, you transform the training data to apply the standardization.

      Let's understand the above procedure by taking an example :

      Consider a feature with values _[10, 20, 30, 40, 50]._

      **Fitting:**

      Mean: 30  
      Standard Deviation: 15.81

      **Transforming:**

      For each value, subtract the mean and divide by the standard deviation:  
      (10 - 30) / 15.81 ≈ -1.26  
      (20 - 30) / 15.81 ≈ -0.63  
      (30 - 30) / 15.81 = 0  
      (40 - 30) / 15.81 ≈ 0.63  
      (50 - 30) / 15.81 ≈ 1.26  
      The scaled feature values are [-1.26, -0.63, 0, 0.63, 1.26].

  ```python
  # scaler.fit(X_train)   Fits the data => Mean and std
  # X_train_standardized = scaler.transform(X_train)  Transforms the data => Applies mean and std to original data

  X_train_standardized = scaler.fit_transform(X_train)    # 2 in 1
  ```

    <hr>

- Use the same scaler data obtained from the original data to fit and tranform the test data as well.

  ```python
  # Standardizing the testing data using the same scaler object
  X_test_standardized = scaler.transform(X_test)
  ```

  <hr>

#### Overall Output for Standardization

```python
Standard deviation of X_train_standardized: 1.0     # Changed from 228 to 1
Standard deviation of X_test_standardized: 0.8654541077212674     # Close to 1
```

Generally it is not needed to train the Y data as it is the prediction. Scaling Y would change the interpretation of your predictions.

## Label Encoding

It converts the labelled data (written text) into numerical form.

Loading the datasets and finding the count of the values

```python
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
```

#### Output

| id       | diagnosis | radius_mean | texture_mean | perimeter_mean | area_mean | ... | compactness_worst | concavity_worst | concave points_worst | symmetry_worst | fractal_dimension_worst | Unnamed: 32 |
| -------- | --------- | ----------- | ------------ | -------------- | --------- | --- | ----------------- | --------------- | -------------------- | -------------- | ----------------------- | ----------- |
| 842302   | M         | 17.99       | 10.38        | 122.80         | 1001.0    | ... | 0.6656            | 0.7119          | 0.2654               | 0.4601         | 0.11890                 | NaN         |
| 842517   | M         | 20.57       | 17.77        | 132.90         | 1326.0    | ... | 0.1866            | 0.2416          | 0.1860               | 0.2750         | 0.08902                 | NaN         |
| 84300903 | M         | 19.69       | 21.25        | 130.00         | 1203.0    | ... | 0.4245            | 0.4504          | 0.2430               | 0.3613         | 0.08758                 | NaN         |
| 84348301 | M         | 11.42       | 20.38        | 77.58          | 386.1     | ... | 0.8663            | 0.6869          | 0.2575               | 0.6638         | 0.17300                 | NaN         |
| 84358402 | M         | 20.29       | 14.34        | 135.10         | 1297.0    | ... | 0.2050            | 0.4000          | 0.1625               | 0.2364         | 0.07678                 | NaN         |

| Id  | SepalLengthCm | SepalWidthCm | PetalLengthCm | PetalWidthCm | Species     |
| --- | ------------- | ------------ | ------------- | ------------ | ----------- |
| 1   | 5.1           | 3.5          | 1.4           | 0.2          | Iris-setosa |
| 2   | 4.9           | 3.0          | 1.4           | 0.2          | Iris-setosa |
| 3   | 4.7           | 3.2          | 1.3           | 0.2          | Iris-setosa |
| 4   | 4.6           | 3.1          | 1.5           | 0.2          | Iris-setosa |
| 5   | 5.0           | 3.6          | 1.4           | 0.2          | Iris-setosa |

    diagnosis
    B    357
    M    212
    Name: count, dtype: int64

    Species
    Iris-setosa        50
    Iris-versicolor    50
    Iris-virginica     50
    Name: count, dtype: int64

As we can see that there are 357 cases of benign (B) breast cancer and 212 cases of malignant(M) breast cancer.  
Also for iris dataset there are 50 cases of setosa, 50 of versicolor and 50 of virginica.  
These columns are the target values in the dataset, so instead of reading the labels we convert this to numerical form. That is called **Label Encoding**.

  <hr />

```python
# Breast Cancer Dataset

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Loads the data
breast_cancer = pd.read_csv('./DataSets/breast_cancer.csv')
iris = pd.read_csv('./DataSets/iris_data.csv')

# Importing the label encoder
label_encoder = LabelEncoder()

# Tranforming the labels of diagnosis column
labels = label_encoder.fit_transform(breast_cancer['diagnosis'])

# Putting these tranform values to the table in a new column target
breast_cancer['target'] = labels

print(breast_cancer['target'].value_counts())
```

#### Output

    diagnosis
    0    357
    1    212
    Name: count, dtype: int64

As we can see that the Beningn(B) is changed to 0 and the Malignant(M) is changed to 1.

```python
# Iris Dataset

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Loads the data
breast_cancer = pd.read_csv('./DataSets/breast_cancer.csv')
iris = pd.read_csv('./DataSets/iris_data.csv')

# Importing the label encoder
label_encoder = LabelEncoder()

# Tranforming the labels of Species column of iris
labels = label_encoder.fit_transform(iris['Species'])

# Putting these tranform values to the table in a new column class
iris['class'] = labels

print(iris['class'].value_counts())
```

#### Output

    class
    0    50
    1    50
    2    50
    Name: count, dtype: int64

Here the Species Iris-setosa, Iris-versicolor and Iris-virginica are changed to their numerical form.  
These numbers are assigned by the alphabetical orders.  
`Iris-setosa => 0`  
`Iris-virginica => 1`  
`Iris-versicolor => 2`

## Handling the Imbalanced Dataset

An **imbalanced dataset** is a dataset with an unequal class distribution.  
For example, in this dataset we have credit card transactions with a column of class containing the values 0 and 1.  
`0 => Legit Transactions`  
`1 => Fradulent Transactions`  
But in this dataset the number of Legit Transactions is much much more higher than the number of Fradulent Transactions.

### Loading the Dataset and counting the values of 0 and 1

```python
import numpy as np
import pandas as pd

# Loading the dataset
credit_card_data = pd.read_csv('DataSets/credit_data.csv')

# Printing the first five rows
print(credit_card_data.head())

# Counting the number of values of the column 'Class'
print(credit_card_data['Class'].value_counts())
```

#### Output

| Time | V1        | V2        | V3       | V4        | V5        | V6        | V7        | V8        | ... | V22       | V23       | V24       | V25       | V26       | V27       | V28       | Amount | Class |
| ---- | --------- | --------- | -------- | --------- | --------- | --------- | --------- | --------- | --- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | ------ | ----- |
| 0.0  | -1.359807 | -0.072781 | 2.536347 | 1.378155  | -0.338321 | 0.462388  | 0.239599  | 0.098698  | ... | 0.277838  | -0.110474 | 0.066928  | 0.128539  | -0.189115 | 0.133558  | -0.021053 | 149.62 | 0     |
| 0.0  | 1.191857  | 0.266151  | 0.166480 | 0.448154  | 0.060018  | -0.082361 | -0.078803 | 0.085102  | ... | -0.638672 | 0.101288  | -0.339846 | 0.167170  | 0.125895  | -0.008983 | 0.014724  | 2.69   | 0     |
| 1.0  | -1.358354 | -1.340163 | 1.773209 | 0.379780  | -0.503198 | 1.800499  | 0.791461  | 0.247676  | ... | 0.771679  | 0.909412  | -0.689281 | -0.327642 | -0.139097 | -0.055353 | -0.059752 | 378.66 | 0     |
| 1.0  | -0.966272 | -0.185226 | 1.792993 | -0.863291 | -0.010309 | 1.247203  | 0.237609  | 0.377436  | ... | 0.005274  | -0.190321 | -1.175575 | 0.647376  | -0.221929 | 0.062723  | 0.061458  | 123.50 | 0     |
| 2.0  | -1.158233 | 0.877737  | 1.548718 | 0.403034  | -0.407193 | 0.095921  | 0.592941  | -0.270533 | ... | 0.798278  | -0.137458 | 0.141267  | -0.206010 | 0.502292  | 0.219422  | 0.215153  | 69.99  | 0     |

[5 rows x 31 columns]

    Class
    0    284315
    1       492
    Name: count, dtype: int64

It can be clearly seen that the number of legit transactions is 2,84,315 and that of fradulent transactions is 492. Here what we do is we take a limited number of datapoints from the legit transactions to match the number of datapoints from the fradulent transactions. 
**This approach is known as Undersampling.** This makes a new dataset which will be balanced.

#### Advantages : This method helps prevent the model from being biased towards the majority class.

- Seperating the legit and fraud transactions 
  ```python
  # Seperating the Legit and Fraudulent Transactions
  legit_transac = credit_card_data[credit_card_data['Class'] == 0]
  fraud_transac = credit_card_data[credit_card_data['Class'] == 1]

  # legit_transac contains 2,84,315 datapoints and fraud_transac contains 492 datapoints
  ```

- Creating a new legit_tranac with 492 datapoints
  ```python
  # Creating a new dataset of legit_transac with random 492 points out of the old dataset of legit_transac
  new_legit_transac = legit_transac.sample(n=492)     

  # Printing the shape of the new dataset of legit_transac
  print(new_legit_transac.shape)
  ```

  #### Output
      (492, 31)

- Combining the new_legit and old_fraud to make a new balanced dataset
  ```python
  # Creating the new credit_card dataset with mixed datapoints of 492 new_legit and 492 old_fraud transactions
  # axis = 0 means combine in terms of rows not in columns
  new_credit_card_data = pd.concat([new_legit_transac,fraud_transac],axis=0)

  # Printing the first five rows of data
  print(new_credit_card_data.head()) 

  # Printing the last five rows of data
  print(new_credit_card_data.tail())

  # Counting the number of values of the column 'Class' in new dataset
  print(new_credit_card_data['Class'].value_counts())
  ```

  #### Output
  head()

  | Index  | Time    | V1       | V2       | V3       | V4       | V5       | V6       | V7       | V8       | ... | V22      | V23      | V24      | V25      | V26      | V27      | V28      | Amount | Class |
  |--------|---------|----------|----------|----------|----------|----------|----------|----------|----------|-----|----------|----------|----------|----------|----------|----------|----------|--------|-------|
  | 80907  | 58710.0 | -1.050926| 0.815976 | -0.306074| -0.131973| -1.560249| 0.738732 | 2.257305 | -0.177135| ... | 0.103563 | -0.212282| -0.422392| -0.022029| 1.163511 | -0.089614| -0.090484| 419.96 | 0     |
  | 61060  | 49638.0 | -0.768831| 0.721597 | 2.077620 | 1.386042 | -0.953130| 0.210961 | -0.572920| 0.786263 | ... | 0.441626 | 0.050288 | 0.383550 | -0.586890| -0.331563| 0.111361 | 0.087345 | 10.00  | 0     |
  | 270086 | 163914.0| -0.335261| -0.154156| -0.421476| -0.008303| -1.166101| 2.387925 | -1.053310| -3.551293| ... | 1.431594 | -1.357234| 0.018353 | 1.824909 | 0.953848 | 0.288240 | 0.099910 | 378.00 | 0     |
  | 71138  | 54175.0 | 0.817135 | -2.201222| 0.779840 | -1.123952| -2.374996| -0.405841| -1.101712| -0.003851| ... | -0.122978| -0.164727| 0.508008 | -0.023591| -0.297312| -0.003803| 0.079369 | 327.60 | 0     |
  | 88073  | 61972.0 | 1.011703 | -0.309617| 0.853154 | 1.676177 | -0.902768| -0.183472| -0.273783| 0.073116 | ... | -0.111641| -0.155781| 0.396962 | 0.623388 | -0.292656| 0.035216 | 0.037332 | 85.60  | 0     |

  [5 rows x 31 columns]

  tail()
  | Index  | Time    | V1       | V2       | V3       | V4       | V5       | V6       | V7       | V8       | ... | V22      | V23      | V24      | V25      | V26      | V27      | V28      | Amount | Class |
  |--------|---------|----------|----------|----------|----------|----------|----------|----------|----------|-----|----------|----------|----------|----------|----------|----------|----------|--------|-------|
  | 279863 | 169142.0| -1.927883| 1.125653 | -4.518331| 1.749293 | -1.566487| -2.010494| -0.882850| 0.697211 | ... | -0.319189| 0.639419 | -0.294885| 0.537503 | 0.788395 | 0.292680 | 0.147968 | 390.00 | 1     |
  | 280143 | 169347.0| 1.378559 | 1.289381 | -5.004247| 1.411850 | 0.442581 | -1.326536| -1.413170| 0.248525 | ... | 0.028234 | -0.145640| -0.081049| 0.521875 | 0.739467 | 0.389152 | 0.186637 | 0.76   | 1     |
  | 280149 | 169351.0| -0.676143| 1.126366 | -2.213700| 0.468308 | -1.120541| -0.003346| -2.234739| 1.210158 | ... | 0.834108 | 0.190944 | 0.032070 | -0.739695| 0.471111 | 0.385107 | 0.194361 | 77.89  | 1     |
  | 281144 | 169966.0| -3.113832| 0.585864 | -5.399730| 1.817092 | -0.840618| -2.943548| -2.208002| 1.058733 | ... | -0.269209| -0.456108| -0.183659| -0.328168| 0.606116 | 0.884876 | -0.253700| 245.00 | 1     |
  | 281674 | 170348.0| 1.991976 | 0.158476 | -2.583441| 0.408670 | 1.151147 | -0.096695| 0.223050 | -0.068384| ... | -0.295135| -0.072173| -0.450261| 0.313267 | -0.289617| 0.002988 | -0.015309| 42.53  | 1     |

  [5 rows x 31 columns]

      Class
      0    492
      1    492
      Name: count, dtype: int64
