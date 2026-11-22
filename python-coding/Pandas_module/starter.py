import pandas as pd

# Create a sample DataFrame
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

# Pandas as pd
# Pandas is usually imported under the pd alias.

# alias: In Python alias are an alternate name for referring to the same thing.

# Create an alias with the as keyword while importing:

# import pandas as pd

# Checking Pandas Version
# The version string is stored under __version__ attribute.

# Example
import pandas as pd

print(pd.__version__)