# Simple Arithmetic
# You could use arithmetic operators + - * / directly between NumPy arrays, but this section discusses an extension of the same where we have functions that can take any array-like objects e.g. lists, tuples etc. and perform arithmetic conditionally.

# Arithmetic Conditionally: means that we can define conditions where the arithmetic operation should happen.

# All of the discussed arithmetic functions take a where parameter in which we can specify that condition.

# Addition
# The add() function sums the content of two arrays, and return the results in a new array.

# Example
# Add the values in arr1 to the values in arr2:

import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)

print(newarr)