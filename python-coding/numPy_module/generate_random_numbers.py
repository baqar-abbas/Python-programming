# Generate Random Number
# NumPy offers the random module to work with random numbers.

# Example
# Generate a random integer from 0 to 100:

from numpy import random

x = random.randint(100)

print(x)

# Generate Random Float
# The random module's rand() method returns a random float between 0 and 1.

# Example
# Generate a random float from 0 to 1:

x = random.rand()

print(x)

# Generate Random Array
# In NumPy we work with arrays, and we can use the two methods from the above examples to make random arrays.

# Integers
# The randint() method takes a size parameter where we can specify the shape of an array.

# Example
# Generate a 1-D array containing 5 random integers from 0 to 100:

x=random.randint(100, size=(5))

print(x)

# Example
# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:

x = random.randint(100, size=(3, 5))

print(x)

# Floats
# The rand() method also allows you to specify the shape of the array.

# Example
# Generate a 1-D array containing 5 random floats:

x = random.rand(5)

print(x)

# Example
# Generate a 2-D array with 3 rows, each row containing 5 random numbers:

x = random.rand(3, 5)

print(x)

# Generate Random Number From Array
# The choice() method allows you to generate a random value based on an array of values.

# The choice() method takes an array as a parameter and randomly returns one of the values.

# Example
# Return one of the values in an array:

x = random.choice([3, 5, 7, 9])

print(x)