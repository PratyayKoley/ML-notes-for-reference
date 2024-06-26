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


print("\n Addition using np.add : \n")
print(np.add(a,b))
print("\n Subtraction using np.subtract : \n")
print(np.subtract(a,b))
print("\n Multiplication using np.multiply : \n")
print(np.multiply(a,b))
print("\n Division using np.divide : \n")
print(np.divide(a,b))