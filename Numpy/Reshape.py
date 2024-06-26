import numpy as np

a = np.random.randint(10,50,[4,5])
print(a)
print(a.shape)

b = a.reshape([2,10])
print(b)
print(b.shape)

b = a.reshape([5,4])
print(b)
print(b.shape)