# Data

## Data Collection sites for Machine Learning

1. [Kaggle](https://www.kaggle.com/)
2. [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
3. [Google Dataset Search](https://datasetsearch.research.google.com/)

## Handling Missing values in the dataset

The values in the dataset can be empty in some places but we can't feed such data to the model which contains null or empty values. We have to handle such data.

1. Imputation => Filling the missing values by mean, median or values.
2. Dropping => Dropping all the rows which contain the missing values.

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
# 1. Imputation => Filling the missing values by mean, median or mode
# 2. Dropping => Dropping all the rows which contain the missing values

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