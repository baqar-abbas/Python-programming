# Rayleigh Distribution
# Rayleigh distribution is used in signal processing.

# It has two parameters:

# scale - (standard deviation) decides how flat the distribution will be default 1.0).

# size - The shape of the returned array.

# Example
# Draw out a sample for rayleigh distribution with scale of 2 with size 2x3:

from numpy import random

x = random.rayleigh(scale=2, size=(2, 3))

print(x)

# Visualization of Rayleigh Distribution

# Example

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.rayleigh(size=1000), kind="kde")

plt.show()