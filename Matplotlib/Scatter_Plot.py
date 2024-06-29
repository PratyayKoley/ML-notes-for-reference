import matplotlib.pyplot as plt
import numpy as np

# Scatter Graph 

x = np.linspace(10,20,50)
fig, ax = plt.subplots()
ax.scatter(x,np.sin(x),color='r')
ax.scatter(x,np.cos(x),color='b')   # we have to use color parameter to apply color
plt.show()

# 3D Scatter Graph

# to give subplots a parameter subplot_kw={} is needed it tells that the subplots contains a parameter 
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

x = 20 * np.random.rand(100)     # generates 100 random values between 0 and 1

# c = x => the color of each point varies according to its x-coordinate
# cmap => colormap => gives different shades of the color

ax.scatter(np.sin(x),np.cos(x),x,c=x,cmap='Blues')
plt.show()