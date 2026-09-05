# Poisson Distribution
# Poisson Distribution is a Discrete Distribution.

# It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?

# It has two parameters:

# lam - rate or known number of occurrences e.g. 2 for above problem.

# size - The shape of the returned array.

# Example
# Generate a random 1x10 distribution for occurrence 2:

from numpy import random

x = random.poisson(lam=2, size=10)

print(x)

# Visualization of Poisson Distribution
# Example

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.poisson(lam=2, size=1000))

plt.show()

