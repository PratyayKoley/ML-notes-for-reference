import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20,20,100)
y = x**2

# Parabola as y = x^2 
# plt.plot(x,y)
# plt.xlabel('x')
# plt.ylabel('$x^2$') # LaTeX formatting
# plt.title('Parabola')
# plt.show()

# Parabola with different colors
# plt.plot(x,y,'r')       # r is for red
# plt.xlabel('x')
# plt.ylabel('$x^2$') # LaTeX formatting
# plt.title('Parabola')
# plt.show()

# Parabola with different symbols
# plt.plot(x,y,'+')       # + shows the symbol to represent the points of parabola
# plt.xlabel('x')
# plt.ylabel('$x^2$')     # LaTeX formatting
# plt.title('Parabola')
# plt.show()

# Both can also be combined the symbol and the color
plt.plot(x,y,'g+')       # + shows the symbol to represent the points of parabola and g represents green color
plt.xlabel('x')
plt.ylabel('$x^2$')     # LaTeX formatting
plt.title('Parabola')
plt.show()
