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

# The example above returns [30 32 34 36 38 40] which is the sums of 10+20, 11+21, 12+22 etc.

# Subtraction
# The subtract() function subtracts the values from one array with the values from another array, and return the results in a new array.

# Example
# Subtract the values in arr2 from the values in arr1:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2)

print(newarr)

# The example above returns [-10 -1 8 17 26 35] which is the result of 10-20, 20-21, 30-22 etc.

# Multiplication
# The multiply() function multiplies the values from one array with the values from another array, and return the results in a new array.

# Example
# Multiply the values in arr1 with the values in arr2:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1, arr2)

print(newarr)

# Division
# The divide() function divides the values from one array with the values from another array, and return the results in a new array.

# Example
# Divide the values in arr1 with the values in arr2:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)

print(newarr)

# The example above returns [3.33333333 4. 3. 5. 25. 1.81818182] which is the result of 10/3, 20/5, 30/10 etc.

# Power
# The power() function rises the values from the first array to the power of the values of the second array, and return the results in a new array.

# Example
# Raise the valules in arr1 to the power of values in arr2:

import numpy as np

arr1 = np.array([2, 3, 4, 5, 6, 7])
arr2 = np.array([3, 5, 6, 8, 2, 3])

newarr = np.power(arr1, arr2)

print(newarr)

