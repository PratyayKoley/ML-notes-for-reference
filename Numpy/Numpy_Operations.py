# 1-D Array

import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
print(arr.shape)


print("\n 2-D Array")
import numpy as np

b = np.array([(1,2,3,4,5), (7,8,9,6,2)])
print(b)
print(b.shape)

print("\n We can also state the datatype of the array by default the datatype is int")

import numpy as np

b = np.array([(1,2,3,4,5), (7,8,9,6,2)], dtype=float)
print(b)

b = np.array([(1,2,3,4,5), (7,8,9,6,2)], dtype=bool)
print(b)

print("\n Create a numpy array of zeros")

import numpy as np

c = np.zeros([4,6])
print(c)


print("\n Create a numpy array of ones")

import numpy as np

c = np.ones([4,6])
print(c)

print("\n Create a numpy array of particular value")
import numpy as np

c = np.full([4,3], 2)
print(c)

print("\n Create an identity matrix")
import numpy as np

c = np.eye(3)
print(c) 

print("\n Create a numpy array with random values")
import numpy as np

c = np.random.random([4,3])
print(c)

print("\n Create a numpy array with random integers")
import numpy as np

c = np.random.randint(1,10,[3,4])
print(c)

print("\n Create a numpy array of a specified range by specifying the number of values needed")
import numpy as np

c = np.linspace(1,10,5)
print(c)

print("\n Create a numpy array of a specified range by specifying the difference (step) between each value")
import numpy as np

c = np.arange(1,30,5)
print(c)

print("\n Converting a list to numpy array")
import numpy as np

list1 = [1,2,3,4,5,6,7]
c = np.asarray(list1)
print(c)
print(type(c))

print("\n Random Array")
import numpy as np

n1 = np.random.randint(10,90,[5,5])
print(n1)

print("\n Shape of array")
print(n1.shape)

print("\n Dimensions of array")
print(n1.ndim)

print("\n Number of elements in array")
print(n1.size)

print("\n Datatype of array")
print(n1.dtype)