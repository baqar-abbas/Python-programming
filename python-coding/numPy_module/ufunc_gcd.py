# NumPy GCD Greatest Common Divisor

# Finding GCD (Greatest Common Divisor)
# The GCD (Greatest Common Divisor), also known as HCF (Highest Common Factor) is the biggest number that is a common factor of both of the numbers.

# Example
# Find the HCF of the following two numbers:

import numpy as np

num1 = 6
num2 = 9

x = np.gcd(num1, num2)

print(x)

# Returns: 3 because that is the highest number both numbers can be divided by (6/3=2 and 9/3=3).