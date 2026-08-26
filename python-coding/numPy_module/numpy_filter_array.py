# NumPy Filter Array
# Filtering Arrays
# Getting some elements out of an existing array and creating a new array out of them is called filtering.

# In NumPy, we filter an array using a boolean index list.

# A boolean index list is a list of booleans corresponding to indexes in the array.

# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

# Example
# Create an array from the elements on index 0 and 2:

import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)