import matplotlib.pyplot as plt

# sin and cos curves
import numpy as np

x = np.linspace(1,20,100)
sin_term = np.sin(x)
cos_term = np.cos(x)

print(f"Equally spaced values between 1 and 20\n{x} \n\n Sin values of the x values\n{sin_term} \n\n Cos values of the x values \n{cos_term}")

# Sine wave
plt.plot(x,sin_term)
plt.show()

# Cosine wave
plt.plot(x,cos_term)
plt.show()

# Adding title, x label and y label to the plotting

# Sine wave
plt.plot(x,sin_term)
plt.xlabel('Angle')
plt.ylabel('Sin Value')
plt.title('Sine Curve')
plt.show()

# Cosine wave
plt.plot(x,cos_term)
plt.xlabel('Angle')
plt.ylabel('Cos Value')
plt.title('Cosine Curve')
plt.show()

# Sine and Cosine wave in a single graph
plt.plot(x,sin_term,'r-')
plt.plot(x,cos_term,'b--')
plt.show()