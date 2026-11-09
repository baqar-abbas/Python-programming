# NumPy Set Operations

# What is a Set
# A set in mathematics is a collection of unique elements.

# Sets are used for operations involving frequent intersection, union and difference operations.

# Create Sets in NumPy
# We can use NumPy's unique() method to find unique elements from any array. E.g. create a set array, but remember that the set arrays should only be 1-D arrays.

# Example
# Convert following array with repeated elements to a set:

import numpy as np

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)

print(x)