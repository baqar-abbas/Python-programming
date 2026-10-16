# NumPy Products

# Products
# To find the product of the elements in an array, use the prod() function.

# Example
# Find the product of the elements of this array:

import numpy as np

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)

print(x)
Returns: 24 because 1*2*3*4 = 24

Example
Find the product of the elements of two arrays:

import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])

print(x)
Returns: 40320 because 1*2*3*4*5*6*7*8 = 40320