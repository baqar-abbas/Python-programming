# NumPy Trigonometric Functions

# Trigonometric Functions
# NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.

# Example
# Find sine value of PI/2:

import numpy as np

x = np.sin(np.pi/2)

print(x)

# Example
# Find sine values for all of the values in arr:

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)