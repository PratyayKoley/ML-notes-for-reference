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

#### Overall Output for Standardization

```python
Standard deviation of X_train_standardized: 1.0     # Changed from 228 to 1
Standard deviation of X_test_standardized: 0.8654541077212674     # Close to 1
```

Generally it is not needed to train the Y data as it is the prediction. Scaling Y would change the interpretation of your predictions. 