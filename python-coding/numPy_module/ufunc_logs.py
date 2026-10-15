# NumPy Logs

# Logs
# NumPy provides functions to perform log at the base 2, e and 10.

# We will also explore how we can take log for any base by creating a custom ufunc.

# All of the log functions will place -inf or inf in the elements if the log can not be computed.

# Log at Base 2
# Use the log2() function to perform log at the base 2.

# Example
# Find log at base 2 of all elements of following array:

import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr))

# Note: The arange(1, 10) function returns an array with integers starting from 1 (included) to 10 (not included).

# Log at Base 10
# Use the log10() function to perform log at the base 10.

# Example
# Find log at base 10 of all elements of following array:

import numpy as np

arr = np.arange(1, 10)

print(np.log10(arr))