# Rounding Decimals
# There are primarily five ways of rounding off decimals in NumPy:

# truncation
# fix
# rounding
# floor
# ceil

# Truncation
# Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.

# Example
# Truncate elements of following array:

import numpy as np

arr = np.trunc([-3.1666, 3.6667])

print(arr)

# Example
# Same example, using fix():

import numpy as np

arr = np.fix([-3.1666, 3.6667])

print(arr)

