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

# Rounding
# The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.

# E.g. round off to 1 decimal point, 3.16666 is 3.2

# Example
# Round off 3.1666 to 2 decimal places:

import numpy as np

arr = np.around(3.1666, 2)

print(arr)

