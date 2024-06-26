# Numpy - Numerical Python

### Advantages : 
1. Allows several Mathematical Operations
2. Faster Operations

#### Numpy vs List

```python
from time import process_time
import numpy as np

# For a list calculate the time taken for an operation

process_list = [i for i in range(100000000)]

start_time = process_time()

process_list = [i+5 for i in process_list]

end_time = process_time()

print(f"Total time for list = {end_time - start_time:.10f}")

# For a numpy array calculate the time taken for an operation

numpy_array = np.array([i for i in range(100000000)])

start_time = process_time()

numpy_array += 5

end_time = process_time()

print(f"Total time for numpy array = {end_time - start_time:.10f}")
```
#### Output :  
    Total time for list = 4.5937500000
    Total time for numpy array = 0.1718750000

### Numpy Operations

#### 1-D Array : 

```python
import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
print(arr.shape)
```

#### Output :  

    [1 2 3 4 5]
    <class 'numpy.ndarray'>
    (5,)

#### 2-D Array : 

```python
import numpy as np

b = np.array([(1,2,3,4,5), (7,8,9,6,2)])
print(b)
print(b.shape)
```

#### Output :  

    [[1 2 3 4 5]
    [7 8 9 6 2]]
    (2, 5)

#### We can also state the datatype of the array, by default the datatype is int

```python
import numpy as np

b = np.array([(1,2,3,4,5), (7,8,9,6,2)], dtype=float)
print(b)

b = np.array([(1,2,3,4,5), (7,8,9,6,2)], dtype=bool)
print(b)
```

#### Output :  

    [[1. 2. 3. 4. 5.]
    [7. 8. 9. 6. 2.]]

    [[ True  True  True  True  True]
    [ True  True  True  True  True]]

#### Create a numpy array of zeros

```python
import numpy as np

c = np.zeros([4,6])
print(c)
```

#### Output :
    [[0. 0. 0. 0. 0. 0.]
    [0. 0. 0. 0. 0. 0.]
    [0. 0. 0. 0. 0. 0.]
    [0. 0. 0. 0. 0. 0.]]

#### Create a numpy array of ones

```python
import numpy as np

c = np.ones([4,6])
print(c)
```

#### Output :
    [[1. 1. 1. 1. 1. 1.]
    [1. 1. 1. 1. 1. 1.]
    [1. 1. 1. 1. 1. 1.]
    [1. 1. 1. 1. 1. 1.]]

#### Create an array of particular value

```python
import numpy as np

c = np.full([4,3], 2)
print(c)
```

Here [4,3] is the shape of array and 2 is the value with which array should be filled.

#### Output
    [[2 2 2]
    [2 2 2]
    [2 2 2]
    [2 2 2]]

#### Create an identity matrix 

```python
import numpy as np

c = np.eye(3)
print(c) 
```

Here identity matrix always involves equal no. of rows and columns, therefore we have only one parameter for eye function.

#### Output
    [[1. 0. 0.]
    [0. 1. 0.]
    [0. 0. 1.]]

#### Create a numpy array with random values

```python
import numpy as np

c = np.random.random([4,3])
print(c)
```
It generates random values between 0 and 1 and takes the parameter as the shape of the array

#### Output
    [[0.16097031 0.61441621 0.07040195]
    [0.74110241 0.08907046 0.78833529]
    [0.45036893 0.4324787  0.54514011]
    [0.3159782  0.94576156 0.97300974]]

#### Create a numpy array with random values as integers

```python
import numpy as np

c = np.random.randint(1,10,[3,4])
print(c)
```

Here the first two params are the range of integer value and thirs param is the shape of array

#### Output
    [[5 9 1 4]
    [3 5 5 3]
    [6 9 2 7]]

#### Create a numpy array with evenly spaced data

1.  Specifying the number of values

```python
import numpy as np

c = np.linspace(1,10,5)
print(c)
```

This takes the first and second param as the range of array and the third param as the number of values or the length of the array needed

#### Output
    [ 1.    3.25  5.5   7.75 10.  ]

2.  Specifying the differnece (step) between the values

```python
import numpy as np

c = np.arange(1,30,5)
print(c)
```

This takes the first and second param as the range of array and the third param as the step value (value with which the current value must increment). Basically it creates an A.P.

#### Output

    [ 1  6 11 16 21 26]

#### Converting a list to numpy array

```python
import numpy as np

list1 = [1,2,3,4,5,6,7]
c = np.asarray(list1)
print(c)
print(type(c))
```
#### Output
    [1 2 3 4 5 6 7]
    <class 'numpy.ndarray'>

### Analysis of a numpy array

##### Creation of an array
```python
import numpy as np

n1 = np.random.randint(10,90,[5,5])
print(n1)
```

#### Output
    [[36 67 43 71 57]
    [45 43 49 48 30]
    [24 38 31 27 63]
    [35 32 72 53 23]
    [66 29 87 56 78]]

1.  Shape of array

    ```python
    print(n1.shape)
    ```
    #### Output
        (5, 5)

2.  Dimension of array

    ```python
    print(n1.ndim)
    ```
    #### Output
        2 (rows and columns so 2 dimensions)

3.  Number of elements

    ```python
    print(n1.size)
    ```
    #### Output
        25

4.  DataType of array

    ```python
    print(n1.dtype)
    ```
    #### Output
        int32

## Operations on two Numpy arrays

```python
import numpy as np

a = np.random.randint(10,30,[4,4]);
print(a)
b = np.random.randint(30,50,[4,4]);
print(b)

print("\n Addition using a + b : \n")
print(a+b)
print("\n Subtraction using a - b : \n")
print(a-b)
print("\n Multiplication using a * b : \n")
print(a*b)
print("\n Division using a / b : \n")
print(a/b)
```

#### Output
    [[26 17 28 15]
    [24 18 11 28]
    [26 13 10 18]
    [21 11 28 13]]
    [[40 36 44 46]
    [30 46 31 46]
    [41 40 34 35]
    [37 45 49 30]]

    Addition using a + b :

    [[66 53 72 61]
    [54 64 42 74]
    [67 53 44 53]
    [58 56 77 43]]

    Subtraction using a - b :

    [[-14 -19 -16 -31]
    [ -6 -28 -20 -18]
    [-15 -27 -24 -17]
    [-16 -34 -21 -17]]

    Multiplication using a * b :

    [[1040  612 1232  690]
    [ 720  828  341 1288]
    [1066  520  340  630]
    [ 777  495 1372  390]]

    Division using a / b :

    [[0.65       0.47222222 0.63636364 0.32608696]
    [0.8        0.39130435 0.35483871 0.60869565]
    [0.63414634 0.325      0.29411765 0.51428571]
    [0.56756757 0.24444444 0.57142857 0.43333333]]

This same thing can be done using the functions of numpy array like add,subtract,multiply,divide

```python
a = np.random.randint(10,30,[4,4]);
print(a)
b = np.random.randint(30,50,[4,4]);
print(b)

print("\n Addition using np.add : \n")
print(np.add(a,b))
print("\n Subtraction using np.subtract : \n")
print(np.subtract(a,b))
print("\n Multiplication using np.multiply : \n")
print(np.multiply(a,b))
print("\n Division using np.divide : \n")
print(np.divide(a,b))
```
#### Output
    [[25 12 21 15]
    [12 22 11 28]
    [17 11 18 16]
    [28 25 18 24]]
    [[45 35 39 33]
    [49 49 36 31]
    [45 41 49 42]
    [43 37 32 34]]

    Addition using np.add :

    [[70 47 60 48]
    [61 71 47 59]
    [62 52 67 58]
    [71 62 50 58]]

    Subtraction using np.subtract :

    [[-20 -23 -18 -18]
    [-37 -27 -25  -3]
    [-28 -30 -31 -26]
    [-15 -12 -14 -10]]

    Multiplication using np.multiply :

    [[1125  420  819  495]
    [ 588 1078  396  868]
    [ 765  451  882  672]
    [1204  925  576  816]]

    Division using np.divide :

    [[0.55555556 0.34285714 0.53846154 0.45454545]
    [0.24489796 0.44897959 0.30555556 0.90322581]
    [0.37777778 0.26829268 0.36734694 0.38095238]
    [0.65116279 0.67567568 0.5625     0.70588235]]

## Transpose of Matrix

```python
import numpy as np

a = np.random.randint(2,18,[3,4])
print(a)
print(a.shape)
```

#### Output
    [[11  4  8  3]
    [14  5 15 13]
    [15  7  6 14]]

    (3, 4)

### Transpose can be found out using numpy in 2 ways

1.  Using transpose() function
    ```python
    b = np.transpose(a)
    print(b)
    print(b .shape)
    ```

    #### Output
        [[11 14 15]
        [ 4  5  7]
        [ 8 15  6]
        [ 3 13 14]]
        (4, 3)  

2.  Using T
    ```python
    c = a.T
    print(c)
    print(c.shape)
    ```

    #### Output
        [[11 14 15]
        [ 4  5  7]
        [ 8 15  6]
        [ 3 13 14]]
        (4, 3)

### Reshape Array
#### Here we can arrange the elements in a different way using reshape function. It takes the new shape of array as the parameter. It only works for those shapes which contains the same number of elements.
Eg : Array of (4,5) have 20 elements so reshape parameters can be any 2 multiples which gives product as 20 like (5,4), (10,2), (2,10), (1,20), (20,1)
```python
import numpy as np

a = np.random.randint(10,50,[4,5])
print(a)
print(a.shape)

# Reshaping to (5,4)
b = a.reshape([5,4])
print(b)
print(b.shape)

# Reshaping to (2,10)
b = a.reshape([2,10])
print(b)
print(b.shape)
```

#### Output
    [[27 17 40 43 21]
    [37 26 28 44 24]
    [45 47 30 29 42]
    [15 49 38 48 39]]
    (4, 5)

    [[27 17 40 43]
    [21 37 26 28]
    [44 24 45 47]
    [30 29 42 15]
    [49 38 48 39]]
    (5, 4)

    [[27 17 40 43 21 37 26 28 44 24]
    [45 47 30 29 42 15 49 38 48 39]]
    (2, 10)