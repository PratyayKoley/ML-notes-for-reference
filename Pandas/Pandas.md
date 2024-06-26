# Pandas

### Advantages

1. Useful for Data Processing and Analysis

### Pandas DataFrame

A Pandas DataFrame is a 2-D tabular data structure with labeled axes (rows and columns).

### Importing Pandas

    import pandas as pd

## Importing Dataset from Scikit-Learn

```python
import pandas as pd
from sklearn.datasets import fetch_california_housing

boston_dataset = fetch_california_housing()

print(type(boston_dataset))

print(boston_dataset)
```

#### Output

    <class 'sklearn.utils._bunch.Bunch'>

    {'data': array([[   8.3252    ,   41.        ,    6.98412698, ...,    2.55555556,
          37.88      , -122.23      ],
       [   8.3014    ,   21.        ,    6.23813708, ...,    2.10984183,
          37.86      , -122.22      ],
       [   7.2574    ,   52.        ,    8.28813559, ...,    2.80225989,
          37.85      , -122.24      ],
       ...,
       [   1.7       ,   17.        ,    5.20554273, ...,    2.3256351 ,
          39.43      , -121.22      ],
       [   1.8672    ,   18.        ,    5.32951289, ...,    2.12320917,
          39.43      , -121.32      ],
       [   2.3886    ,   16.        ,    5.25471698, ...,    2.61698113,
          39.37      , -121.24      ]]), 'target': array([4.526, 3.585, 3.521, ..., 0.923, 0.847, 0.894]), 'frame': None, 'target_names': ['MedHouseVal'], 'feature_names': ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude'], 'DESCR': '.. _california_housing_dataset:\n\nCalifornia Housing dataset\n--------------------------\n\n**Data Set Characteristics:**\n\n:Number of Instances: 20640\n\n:Number of Attributes: 8 numeric, predictive attributes and the target\n\n:Attribute Information:\n    - MedInc        median income in block group\n    - HouseAge      median house age in block group\n    - AveRooms      average number of rooms per household\n    - AveBedrms     average number of bedrooms per household\n    - Population    block group population\n    - AveOccup      average number of household members\n    - Latitude      block group latitude\n    - Longitude     block group longitude\n\n:Missing Attribute Values: None\n\nThis dataset was obtained from the StatLib repository.\nhttps://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html\n\nThe target variable is the median house value for California districts,\nexpressed in hundreds of thousands of dollars ($100,000).\n\nThis dataset was derived from the 1990 U.S. census, using one row per census\nblock group. A block group is the smallest geographical unit for which the U.S.\nCensus Bureau publishes sample data (a block group typically has a population\nof 600 to 3,000 people).\n\nA household is a group of people residing within a home. Since the average\nnumber of rooms and bedrooms in this dataset are provided per household, these\ncolumns may take surprisingly large values for block groups with few households\nand many empty houses, such as vacation resorts.\n\nIt can be downloaded/loaded using the\n:func:`sklearn.datasets.fetch_california_housing` function.\n\n.. topic:: References\n\n    - Pace, R. Kelley and Ronald Barry, Sparse Spatial Autoregressions,\n      Statistics and Probability Letters, 33 (1997) 291-297\n'}

### Now we use Pandas Dataframe to represent this data in a tabular format

```python
boston_df = pd.DataFrame(boston_dataset.data, columns= boston_dataset.feature_names)
```

boston_dataset.data gives the data of the file and boston_dataset.features_names gives the column name of the table

```python
# head() gives only the starting five rows of the data
print(boston_df.head())
```

#### Output

|   | MedInc | HouseAge | AveRooms | AveBedrms | Population | AveOccup | Latitude | Longitude |
| - | ------ | -------- | -------- | --------- | ---------- | -------- | -------- | --------- |
| 0 | 8.3252 | 41.0     | 6.98413  | 1.02381   | 322.0      | 2.55556  | 37.88    | -122.23   |
| 1 | 8.3014 | 21.0     | 6.23814  | 0.97188   | 2401.0     | 2.10984  | 37.86    | -122.22   |
| 2 | 7.2574 | 52.0     | 8.28814  | 1.07345   | 496.0      | 2.80226  | 37.85    | -122.24   |
| 3 | 5.6431 | 52.0     | 5.81735  | 1.07306   | 558.0      | 2.54795  | 37.85    | -122.25   |
| 4 | 3.8462 | 52.0     | 6.28185  | 1.08108   | 565.0      | 2.18147  | 37.85    | -122.25   |

```python
# tail() gives only the last five rows of the data
print(boston_df.tail())
```

#### Output

|       | MedInc | HouseAge | AveRooms | AveBedrms | Population | AveOccup | Latitude | Longitude |
| ----- | ------ | -------- | -------- | --------- | ---------- | -------- | -------- | --------- |
| 20635 | 1.5603 | 25.0     | 5.04546  | 1.13333   | 845.0      | 2.56061  | 39.48    | -121.09   |
| 20636 | 2.5568 | 18.0     | 6.11403  | 1.31579   | 356.0      | 3.12281  | 39.49    | -121.21   |
| 20637 | 1.7000 | 17.0     | 5.20554  | 1.12009   | 1007.0     | 2.32563  | 39.43    | -121.22   |
| 20638 | 1.8672 | 18.0     | 5.32951  | 1.17192   | 741.0      | 2.12321  | 39.43    | -121.32   |
| 20639 | 2.3886 | 16.0     | 5.25472  | 1.16226   | 1387.0     | 2.61698  | 39.37    | -121.24   |

### To know what is the type of boston_df dataframe we use the type() function

```python
print("\n", type(boston_df))
```

#### Output

    <class 'pandas.core.frame.DataFrame'>

To know the total number of rows and columns in the fetch_california_housing we use shape() function

```python
print("\n ", boston_df.shape)
```

#### Output

    (20640, 8)

## Importing Dataset from CSV Files

```python
diabetes_df = pd.read_csv('C:\Machine Learning\DataSets\diabetes.csv')

print(f"\n {type(diabetes_df)} \n")
```

#### Output

    <class 'pandas.core.frame.DataFrame'>

```python
# head() gives only the starting five rows of the data
print(diabetes_df.head())
```

#### Output

| Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin | BMI  | DiabetesPedigreeFunction | Age | Outcome |
| ----------- | ------- | ------------- | ------------- | ------- | ---- | ------------------------ | --- | ------- |
| 6           | 148     | 72            | 35            | 0       | 33.6 | 0.627                    | 50  | 1       |
| 1           | 85      | 66            | 29            | 0       | 26.6 | 0.351                    | 31  | 0       |
| 8           | 183     | 64            | 0             | 0       | 23.3 | 0.672                    | 32  | 1       |
| 1           | 89      | 66            | 23            | 94      | 28.1 | 0.167                    | 21  | 0       |
| 0           | 137     | 40            | 35            | 168     | 43.1 | 2.288                    | 33  | 1       |

To know the total number of rows and columns

```python
print("\n", diabetes_df.shape)
```

#### Output

    (768, 9)

## Importing Dataset from Excel Files

```python
df_file = pd.read_excel('file path name')
```

## Exporting DataFrame to CSV File

```python
import pandas as pd
from sklearn.datasets import fetch_california_housing

# Stored the data in a variable
california_data = fetch_california_housing();

# Created the dataframe
california_df = pd.DataFrame(california_data.data, columns= california_data.feature_names)

# Exported to CSV File
california_df.to_csv('C:\Machine Learning\DataSets\california_housing.csv')
```

#### Output

![Export DataFrame to CSV](image.png)

## Exporting DataFrame to Excel File

```python
import pandas as pd
from sklearn.datasets import fetch_california_housing

# Storing dataset values to a variable
california_data = fetch_california_housing()

# Converting the dataset to a dataframe (table with rows and columns)
california_df = pd.DataFrame(california_data.data, columns= california_data.feature_names)

# Converting the dataframe to an excel file
california_df.to_excel(r'C:\Machine Learning\DataSets\california_housing.xlsx')

# The library openpyxl is required by pandas to write Excel files. You can install it using pip.
```

#### Output

![Export DataFrame to Excel](image-1.png)

## Creating a DataFrame with random values

```python
import pandas as pd
import numpy as np

random_df = pd.DataFrame(np.random.random([8,10]))

print(random_df)
```

#### Output

|   | 0        | 1        | 2        | 3        | 4        | 5        | 6        | 7        | 8        | 9        |
| - | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 0 | 0.124781 | 0.324184 | 0.966929 | 0.085830 | 0.875148 | 0.925833 | 0.548331 | 0.015590 | 0.142717 | 0.677127 |
| 1 | 0.695605 | 0.079186 | 0.231467 | 0.786858 | 0.396522 | 0.227811 | 0.402814 | 0.364105 | 0.798947 | 0.258354 |
| 2 | 0.031550 | 0.678814 | 0.266284 | 0.737498 | 0.868418 | 0.108365 | 0.160744 | 0.946375 | 0.849001 | 0.272515 |
| 3 | 0.551627 | 0.511984 | 0.129549 | 0.019113 | 0.730004 | 0.727899 | 0.784647 | 0.495162 | 0.160560 | 0.628646 |
| 4 | 0.922802 | 0.798485 | 0.632395 | 0.823757 | 0.894062 | 0.770464 | 0.788515 | 0.207887 | 0.701167 | 0.728991 |
| 5 | 0.734756 | 0.459887 | 0.732785 | 0.637659 | 0.492561 | 0.292597 | 0.401443 | 0.104715 | 0.615217 | 0.575720 |
| 6 | 0.459182 | 0.153598 | 0.474180 | 0.479398 | 0.027839 | 0.245715 | 0.357060 | 0.651737 | 0.606458 | 0.810851 |
| 7 | 0.686772 | 0.653825 | 0.989086 | 0.392228 | 0.828385 | 0.334816 | 0.813015 | 0.075781 | 0.275272 | 0.996695 |

## Functions used in Dataframe

```python
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
```

#### Output

|   | MedInc | HouseAge | AveRooms | AveBedrms | Population | AveOccup | Latitude | Longitude |
| - | ------ | -------- | -------- | --------- | ---------- | -------- | -------- | --------- |
| 0 | 8.3252 | 41.0     | 6.98413  | 1.02381   | 322.0      | 2.55556  | 37.88    | -122.23   |
| 1 | 8.3014 | 21.0     | 6.23814  | 0.97188   | 2401.0     | 2.10984  | 37.86    | -122.22   |
| 2 | 7.2574 | 52.0     | 8.28814  | 1.07345   | 496.0      | 2.80226  | 37.85    | -122.24   |
| 3 | 5.6431 | 52.0     | 5.81735  | 1.07306   | 558.0      | 2.54795  | 37.85    | -122.25   |
| 4 | 3.8462 | 52.0     | 6.28185  | 1.08108   | 565.0      | 2.18147  | 37.85    | -122.25   |

|       | MedInc | HouseAge | AveRooms | AveBedrms | Population | AveOccup | Latitude | Longitude |
| ----- | ------ | -------- | -------- | --------- | ---------- | -------- | -------- | --------- |
| 20635 | 1.5603 | 25.0     | 5.04546  | 1.13333   | 845.0      | 2.56061  | 39.48    | -121.09   |
| 20636 | 2.5568 | 18.0     | 6.11403  | 1.31579   | 356.0      | 3.12281  | 39.49    | -121.21   |
| 20637 | 1.7000 | 17.0     | 5.20554  | 1.12009   | 1007.0     | 2.32563  | 39.43    | -121.22   |
| 20638 | 1.8672 | 18.0     | 5.32951  | 1.17192   | 741.0      | 2.12321  | 39.43    | -121.32   |
| 20639 | 2.3886 | 16.0     | 5.25472  | 1.16226   | 1387.0     | 2.61698  | 39.37    | -121.24   |

    <class 'pandas.core.frame.DataFrame'>
      RangeIndex: 20640 entries, 0 to 20639
      Data columns (total 8 columns):
      #   Column      Non-Null Count  Dtype
      ---  ------      --------------  -----
      0   MedInc      20640 non-null  float64
      1   HouseAge    20640 non-null  float64
      2   AveRooms    20640 non-null  float64
      3   AveBedrms   20640 non-null  float64
      4   Population  20640 non-null  float64
      5   AveOccup    20640 non-null  float64
      6   Latitude    20640 non-null  float64
      7   Longitude   20640 non-null  float64
      dtypes: float64(8)
      memory usage: 1.3 MB
      None

|       | MedInc | HouseAge | AveRooms | AveBedrms | Population | AveOccup | Latitude | Longitude |
| ----- | ------ | -------- | -------- | --------- | ---------- | -------- | -------- | --------- |
| 0     | False  | False    | False    | False     | False      | False    | False    | False     |
| 1     | False  | False    | False    | False     | False      | False    | False    | False     |
| 2     | False  | False    | False    | False     | False      | False    | False    | False     |
| 3     | False  | False    | False    | False     | False      | False    | False    | False     |
| 4     | False  | False    | False    | False     | False      | False    | False    | False     |
| ...   | ...    | ...      | ...      | ...       | ...        | ...      | ...      | ...       |
| 20635 | False  | False    | False    | False     | False      | False    | False    | False     |
| 20636 | False  | False    | False    | False     | False      | False    | False    | False     |
| 20637 | False  | False    | False    | False     | False      | False    | False    | False     |
| 20638 | False  | False    | False    | False     | False      | False    | False    | False     |
| 20639 | False  | False    | False    | False     | False      | False    | False    | False     |

      MedInc        0
      HouseAge      0
      AveRooms      0
      AveBedrms     0
      Population    0
      AveOccup      0
      Latitude      0
      Longitude     0
      dtype: int64

```python
import pandas as pd

diabetes_df = pd.read_csv('C:\Machine Learning\DataSets\diabetes.csv')

# head() gives first five rows
print("\n", diabetes_df.head())

# value_counts() count the number of identical rows
# Here diabetes_df contains all unique rows so it gives the rightmost column as value 1 meaning that particular row appeared only once in the dataframe
print("\n", diabetes_df.value_counts())

# value_counts(col_name) counts the number of identical rows based only on the column provided
# Here Outcome has value of only 1 or 0 so it displays the number of rows with value 1 and value 0
print("\n", diabetes_df.value_counts('Outcome'))
```

#### Output

| Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin | BMI  | DiabetesPedigreeFunction | Age | Outcome |
| ----------- | ------- | ------------- | ------------- | ------- | ---- | ------------------------ | --- | ------- |
| 6           | 148     | 72            | 35            | 0       | 33.6 | 0.627                    | 50  | 1       |
| 1           | 85      | 66            | 29            | 0       | 26.6 | 0.351                    | 31  | 0       |
| 8           | 183     | 64            | 0             | 0       | 23.3 | 0.672                    | 32  | 1       |
| 1           | 89      | 66            | 23            | 94      | 28.1 | 0.167                    | 21  | 0       |
| 0           | 137     | 40            | 35            | 168     | 43.1 | 2.288                    | 33  | 1       |

| Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin | BMI  | DiabetesPedigreeFunction | Age | Outcome | Count |
| ----------- | ------- | ------------- | ------------- | ------- | ---- | ------------------------ | --- | ------- | ----- |
| 0           | 57      | 60            | 0             | 0       | 21.7 | 0.735                    | 67  | 0       | 1     |
|             | 67      | 76            | 0             | 0       | 45.3 | 0.194                    | 46  | 0       | 1     |
| 5           | 103     | 108           | 37            | 0       | 39.2 | 0.305                    | 65  | 0       | 1     |
|             | 104     | 74            | 0             | 0       | 28.8 | 0.153                    | 48  | 0       | 1     |
|             | 105     | 72            | 29            | 325     | 36.9 | 0.159                    | 28  | 0       | 1     |
|             |         |               |               |         |      |                          |     |         | ...   |
| 2           | 84      | 50            | 23            | 76      | 30.4 | 0.968                    | 21  | 0       | 1     |
|             | 85      | 65            | 0             | 0       | 39.6 | 0.930                    | 27  | 0       | 1     |
|             | 87      | 0             | 23            | 0       | 28.9 | 0.773                    | 25  | 0       | 1     |
|             |         | 58            | 16            | 52      | 32.7 | 0.166                    | 25  | 0       | 1     |
| 17          | 163     | 72            | 41            | 114     | 40.9 | 0.817                    | 47  | 1       | 1     |

    Outcome
      0    500
      1    268
      Name: count, dtype: int64

## Grouping and applying aggregate functions to the data

```python
# groupby(col_name) groups the same rows together of a particular column
# col_name is compulsory or else groupby won't work
diabetes_grouped = diabetes_df.groupby('Outcome')
```

```python
# mean() gives the mean of all columns based on the Outcome column value
print("\n", diabetes_grouped.mean())
```

#### Output

| Outcome | Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin | BMI    | DiabetesPedigreeFunction | Age    |
| ------- | ----------- | ------- | ------------- | ------------- | ------- | ------ | ------------------------ | ------ |
| 0       | 3.298       | 109.980 | 68.184        | 19.664        | 68.792  | 30.304 | 0.429734                 | 31.190 |
| 1       | 4.866       | 141.257 | 70.825        | 22.164        | 100.336 | 35.143 | 0.550500                 | 37.067 |

Above table gives the mean value for the columns meaning patients with diabetes have a mean glucose of 141.25 and insulin of 100.336 whereas patients who are not diabetic have a mean glucose of 109.98 and insulin of 68.79

## Statistical Functions on DataFrame

1. count()

```python
# count() gives the number of values in each column
print("\n",california_df.count())
```

#### Output

      MedInc        20640
      HouseAge      20640
      AveRooms      20640
      AveBedrms     20640
      Population    20640
      AveOccup      20640
      Latitude      20640
      Longitude     20640

2. mean()

```python
# mean() gives the mean values of each column
print("\n", california_df.mean())
```

#### Output

      MedInc           3.870671
      HouseAge        28.639486
      AveRooms         5.429000
      AveBedrms        1.096675
      Population    1425.476744
      AveOccup         3.070655
      Latitude        35.631861
      Longitude     -119.569704

3. std()

```python
# std() gives the standard deviation values of each column
print("\n", california_df.std())
```

#### Output

      MedInc           1.899822
      HouseAge        12.585558
      AveRooms         2.474173
      AveBedrms        0.473911
      Population    1132.462122
      AveOccup        10.386050
      Latitude         2.135952
      Longitude        2.003532

4. median()

```python
# median() gives the median value of each column
print("\n", california_df.median())
```

#### Output

      MedInc           3.534800
      HouseAge        29.000000
      AveRooms         5.229129
      AveBedrms        1.048780
      Population    1166.000000
      AveOccup         2.818116
      Latitude        34.260000
      Longitude     -118.490000

5. var()

```python
# var() gives the variance value of each column
print("\n", california_df.var())
```

#### Output

      MedInc        3.609323e+00
      HouseAge      1.583963e+02
      AveRooms      6.121533e+00
      AveBedrms     2.245915e-01
      Population    1.282470e+06
      AveOccup      1.078700e+02
      Latitude      4.562293e+00
      Longitude     4.014139e+00

6. min()

```python
# min() gives the minimum value of each column
print("\n", california_df.min())
```

#### Output

      MedInc          0.499900
      HouseAge        1.000000
      AveRooms        0.846154
      AveBedrms       0.333333
      Population      3.000000
      AveOccup        0.692308
      Latitude       32.540000
      Longitude    -124.350000

7. max()

```python
# max() gives the maximum value of each column
print("\n", california_df.max())
```

#### Output

      MedInc           15.000100
      HouseAge         52.000000
      AveRooms        141.909091
      AveBedrms        34.066667
      Population    35682.000000
      AveOccup       1243.333333
      Latitude         41.950000
      Longitude      -114.310000

8. sum()

```python
# sum() gives the total calculated value of each column
print("\n", california_df.sum())
```

#### Output

      MedInc        7.989065e+04
      HouseAge      5.911190e+05
      AveRooms      1.120546e+05
      AveBedrms     2.263538e+04
      Population    2.942184e+07
      AveOccup      6.337832e+04
      Latitude      7.354416e+05
      Longitude    -2.467919e+06

9. describe()

```python
# describe() is a shorthand function to get all the above data in a single table
print("\n", california_df.describe())
```

#### Output

| Statistic    | MedInc    | HouseAge  | AveRooms  | AveBedrms | Population | AveOccup  | Latitude  | Longitude |
| ------------ | --------- | --------- | --------- | --------- | ---------- | --------- | --------- | --------- |
| count        | 20640.000 | 20640.000 | 20640.000 | 20640.000 | 20640.000  | 20640.000 | 20640.000 | 20640.000 |
| mean         | 3.870671  | 28.639486 | 5.429000  | 1.096675  | 1425.476   | 3.070655  | 35.631861 | -119.5697 |
| std          | 1.899822  | 12.585558 | 2.474173  | 0.473911  | 1132.462   | 10.38605  | 2.135952  | 2.003532  |
| min          | 0.4999    | 1.0000    | 0.8461    | 0.3333    | 3.0000     | 0.6923    | 32.5400   | -124.3500 |
| 25%          | 2.5634    | 18.0000   | 4.4407    | 1.0061    | 787.0000   | 2.4297    | 33.9300   | -121.8000 |
| 50% (median) | 3.5348    | 29.0000   | 5.2291    | 1.0488    | 1166.0000  | 2.8181    | 34.2600   | -118.4900 |
| 75%          | 4.7433    | 37.0000   | 6.0524    | 1.0995    | 1725.0000  | 3.2823    | 37.7100   | -118.0100 |
| max          | 15.0001   | 52.0000   | 141.9091  | 34.0667   | 35682.0000 | 1243.3333 | 41.9500   | -114.3100 |

## Dataframe Table Manipulations

### Adding a Column to Dataframe

```python
from sklearn.datasets import fetch_california_housing
import pandas as pd

california_dataset = fetch_california_housing()

california_df = pd.DataFrame(california_dataset.data, columns= california_dataset.feature_names)

# Adding a column to california_df
california_df['Price'] = california_dataset.target

print("\n", california_df.head())
```

The california_dataset.target must contain the same column as that of california_df columns

#### Output

| MedInc | HouseAge | AveRooms | AveBedrms | Population | AveOccup | Latitude | Longitude | Price |
| :----: | :------: | :------: | :-------: | :--------: | :------: | :------: | :-------: | :---: |
| 8.3252 |   41.0   | 6.984127 | 1.023810 |   322.0   | 2.555556 |  37.88  |  -122.23  | 4.526 |
| 8.3014 |   21.0   | 6.238137 | 0.971880 |   2401.0   | 2.109842 |  37.86  |  -122.22  | 3.585 |
| 7.2574 |   52.0   | 8.288136 | 1.073446 |   496.0   | 2.802260 |  37.85  |  -122.24  | 3.521 |
| 5.6431 |   52.0   | 5.817352 | 1.073059 |   558.0   | 2.547945 |  37.85  |  -122.25  | 3.413 |
| 3.8462 |   52.0   | 6.281853 | 1.081081 |   565.0   | 2.181467 |  37.85  |  -122.25  | 3.422 |

### Remove a specific row from Dataframe

```python
from sklearn.datasets import fetch_california_housing
import pandas as pd

california_dataset = fetch_california_housing()

california_df = pd.DataFrame(california_dataset.data, columns= california_dataset.feature_names)

# Removing a row from california_df
row_drop = california_df.drop(index=0, axis=0)

print(row_drop)
```

axis = 0 should be mentioned when removing a row and axis = 1 should be mentioned when removing a column. index = 0 indicates the first row should be removed.

#### Output

| Serial | MedInc | HouseAge | AveRooms | AveBedrms | Population | AveOccup | Latitude | Longitude | Price |
| -----: | -----: | -------: | -------: | --------: | ---------: | -------: | -------: | --------: | ----: |
|      1 | 8.3014 |     21.0 | 6.238137 |  0.971880 |     2401.0 | 2.109842 |    37.86 |   -122.22 | 3.585 |
|      2 | 7.2574 |     52.0 | 8.288136 |  1.073446 |      496.0 | 2.802260 |    37.85 |   -122.24 | 3.521 |
|      3 | 5.6431 |     52.0 | 5.817352 |  1.073059 |      558.0 | 2.547945 |    37.85 |   -122.25 | 3.413 |
|      4 | 3.8462 |     52.0 | 6.281853 |  1.081081 |      565.0 | 2.181467 |    37.85 |   -122.25 | 3.422 |
|      5 | 4.0368 |     52.0 | 4.761658 |  1.103627 |      413.0 | 2.139896 |    37.85 |   -122.25 | 2.697 |
|    ... |    ... |      ... |      ... |       ... |        ... |      ... |      ... |       ... |   ... |
|  20635 | 1.5603 |     25.0 | 5.045455 |  1.133333 |      845.0 | 2.560606 |    39.48 |   -121.09 | 0.781 |
|  20636 | 2.5568 |     18.0 | 6.114035 |  1.315789 |      356.0 | 3.122807 |    39.49 |   -121.21 | 0.771 |
|  20637 | 1.7000 |     17.0 | 5.205543 |  1.120092 |     1007.0 | 2.325635 |    39.43 |   -121.22 | 0.923 |
|  20638 | 1.8672 |     18.0 | 5.329513 |  1.171920 |      741.0 | 2.123209 |    39.43 |   -121.32 | 0.847 |
|  20639 | 2.3886 |     16.0 | 5.254717 |  1.162264 |     1387.0 | 2.616981 |    39.37 |   -121.24 | 0.894 |

### Removing a specific column from dataframe

```python
from sklearn.datasets import fetch_california_housing
import pandas as pd

california_dataset = fetch_california_housing()

california_df = pd.DataFrame(california_dataset.data, columns= california_dataset.feature_names)

# Removing a column from california_df
col_drop = california_df.drop(columns='AveOccup', axis=1)

print(col_drop)

```

axis = 1 means we are removing a column and the other parameter is columns where we need to mention the name of column.

So for row removal we provide row number using index parameter and for column removal we provide the name of the column.

#### Output

| Serial | MedInc | HouseAge | AveRooms | AveBedrms | Population | Latitude | Longitude | Price |
| -----: | -----: | -------: | -------: | --------: | ---------: | -------: | --------: | ----: |
|      0 | 8.3252 |     41.0 | 6.984127 |  1.023810 |      322.0 |    37.88 |   -122.23 | 4.526 |
|      1 | 8.3014 |     21.0 | 6.238137 |  0.971880 |     2401.0 |    37.86 |   -122.22 | 3.585 |
|      2 | 7.2574 |     52.0 | 8.288136 |  1.073446 |      496.0 |    37.85 |   -122.24 | 3.521 |
|      3 | 5.6431 |     52.0 | 5.817352 |  1.073059 |      558.0 |    37.85 |   -122.25 | 3.413 |
|      4 | 3.8462 |     52.0 | 6.281853 |  1.081081 |      565.0 |    37.85 |   -122.25 | 3.422 |
|    ... |    ... |      ... |      ... |       ... |        ... |      ... |       ... |   ... |
|  20635 | 1.5603 |     25.0 | 5.045455 |  1.133333 |      845.0 |    39.48 |   -121.09 | 0.781 |
|  20636 | 2.5568 |     18.0 | 6.114035 |  1.315789 |      356.0 |    39.49 |   -121.21 | 0.771 |
|  20637 | 1.7000 |     17.0 | 5.205543 |  1.120092 |     1007.0 |    39.43 |   -121.22 | 0.923 |
|  20638 | 1.8672 |     18.0 | 5.329513 |  1.171920 |      741.0 |    39.43 |   -121.32 | 0.847 |
|  20639 | 2.3886 |     16.0 | 5.254717 |  1.162264 |     1387.0 |    39.37 |   -121.24 | 0.894 |

As we can see that the column named 'AveOccup' is not present in the table.

### Locating a particular row in the dataframe

```python
from sklearn.datasets import fetch_california_housing
import pandas as pd

california_dataset = fetch_california_housing()

california_df = pd.DataFrame(california_dataset.data, columns= california_dataset.feature_names)

# Locating a particular row
print(california_df.iloc[2])
```

iloc takes the index number of row and print its data

#### Output

      MedInc          7.257400
      HouseAge       52.000000
      AveRooms        8.288136
      AveBedrms       1.073446
      Population    496.000000
      AveOccup        2.802260
      Latitude       37.850000
      Longitude    -122.240000
      Price           3.521000

### Locating a particular column in dataframe

```python
from sklearn.datasets import fetch_california_housing
import pandas as pd

california_dataset = fetch_california_housing()

california_df = pd.DataFrame(california_dataset.data, columns= california_dataset.feature_names)

# Locating a particular column
print(california_df.iloc[:,0])       # Prints the first column
print(california_df.iloc[:,1])       # Prints the second column
print(california_df.iloc[:,-1])       # Prints the last column
```

#### Output
      0        8.3252
      1        8.3014
      2        7.2574
      3        5.6431
      4        3.8462
            ...
      20635    1.5603
      20636    2.5568
      20637    1.7000
      20638    1.8672
      20639    2.3886
      Name: MedInc, Length: 20640, dtype: float64


      0        4.526
      1        3.585
      2        3.521
      3        3.413
      4        3.422
            ...
      20635    0.781
      20636    0.771
      20637    0.923
      20638    0.847
      20639    0.894
      Name: Price, Length: 20640, dtype: float64

      
      0        41.0
      1        21.0
      2        52.0
      3        52.0
      4        52.0
            ...
      20635    25.0
      20636    18.0
      20637    17.0
      20638    18.0
      20639    16.0
      Name: HouseAge, Length: 20640, dtype: float64

### Finding the correlation in table
There are two types of correlation:
1.    Positive Correlation
2.    Negative Correlation
```python
from sklearn.datasets import fetch_california_housing
import pandas as pd

california_dataset = fetch_california_housing()

california_df = pd.DataFrame(california_dataset.data, columns= california_dataset.feature_names)

# Correlation 
print(california_df.corr())
```

#### Output
|              |    MedInc | HouseAge | AveRooms | AveBedrms | Population | AveOccup | Latitude | Longitude |    Price |
|--------------|----------:|---------:|---------:|----------:|-----------:|---------:|---------:|----------:|---------:|
| **MedInc**   |  1.000000 | -0.119034 | 0.326895 | -0.062040 |   0.004834 | 0.018766 | -0.079809 | -0.015176 |  0.688075 |
| **HouseAge** | -0.119034 |  1.000000 | -0.153277 | -0.077747 |  -0.296244 | 0.013191 |  0.011173 | -0.108197 |  0.105623 |
| **AveRooms** |  0.326895 | -0.153277 | 1.000000 |  0.847621 |  -0.072213 | -0.004852 | 0.106389 | -0.027540 |  0.151948 |
| **AveBedrms**| -0.062040 | -0.077747 | 0.847621 |  1.000000 |  -0.066197 | -0.006181 | 0.069721 |  0.013344 | -0.046701 |
| **Population**| 0.004834 | -0.296244 | -0.072213 | -0.066197 |  1.000000 | 0.069863 | -0.108785 |  0.099773 | -0.024650 |
| **AveOccup** |  0.018766 |  0.013191 | -0.004852 | -0.006181 |   0.069863 | 1.000000 | 0.002366 |  0.002476 | -0.023737 |
| **Latitude** | -0.079809 |  0.011173 | 0.106389 |  0.069721 |  -0.108785 | 0.002366 | 1.000000 | -0.924664 | -0.144160 |
| **Longitude**| -0.015176 | -0.108197 | -0.027540 |  0.013344 |   0.099773 | 0.002476 | -0.924664 |  1.000000 | -0.045967 |
| **Price**    |  0.688075 |  0.105623 | 0.151948 | -0.046701 |  -0.024650 | -0.023737 | -0.144160 | -0.045967 |  1.000000 |

This table shows that the houseage is positively related to price of house i.e. directly proportional. If one increase other will also increase