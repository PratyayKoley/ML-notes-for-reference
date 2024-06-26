import numpy as np

a = np.random.randint(2,18,[3,4])
print(a)
print(a.shape)

b = np.transpose(a)
print(b)
print(b.shape)

c = a.T
print(c)
print(c.shape)