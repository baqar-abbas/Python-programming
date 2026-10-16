# NumPy Summations

# Summations

# What is the difference between summation and addition?

# Addition is done between two arguments whereas summation happens over n elements.

# Example
# Add the values in arr1 to the values in arr2:

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)

print(newarr)

# Returns: [2 4 6]

# Example
# Sum the values in arr1 and the values in arr2:

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])

print(newarr)

# Returns: 12