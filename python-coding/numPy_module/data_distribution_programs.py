# Example Random Data Distribution
# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.

# The probability for the value to be 3 is set to be 0.2

# The probability for the value to be 5 is set to be 0.3

# The probability for the value to be 7 is set to be 0.5

# The probability for the value to be 9 is set to be 0

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.2, 0.3, 0.5, 0.0], size=(100))

print(x)

# The sum of all probability numbers should be 1.

# Even if we run the example above 100 times, the value 9 will never occur.

# We can return arrays of any shape and size by specifying the shape in the size parameter.