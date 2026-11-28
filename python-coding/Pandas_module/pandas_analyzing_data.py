# Pandas - Analyzing DataFrames

# Viewing the Data
# One of the most used method for getting a quick overview of the DataFrame, is the head() method.

# The head() method returns the headers and a specified number of rows, starting from the top.

# Example
# Get a quick overview by printing the first 10 rows of the DataFrame:

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))

# Result:

#    Duration  Pulse  Maxpulse  Calories
# 0        60    110       130     409.1
# 1        60    117       145     479.0
# 2        60    103       135     340.0
# 3        45    109       175     282.4
# 4        45    117       148     406.0
# 5        60    102       127     300.0
# 6        60    110       136     374.0
# 7        45    104       134     253.3
# 8        30    109       133     195.1
# 9        60     98       124     269.0

# Note: if the number of rows is not specified, the head() method will return the top 5 rows.

# Example
# Print the first 5 rows of the DataFrame:

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())

# Result:

#    Duration  Pulse  Maxpulse  Calories
# 0        60    110       130     409.1
# 1        60    117       145     479.0
# 2        60    103       135     340.0
# 3        45    109       175     282.4
# 4        45    117       148     406.0

# There is also a tail() method for viewing the last rows of the DataFrame.

# The tail() method returns the headers and a specified number of rows, starting from the bottom.

# Example
# Print the last 5 rows of the DataFrame:

print(df.tail()) 

# Result:

#      Duration  Pulse  Maxpulse  Calories
# 164        60    105       140     290.8
# 165        60    110       145     300.0
# 166        60    115       145     310.2
# 167        75    120       150     320.4
# 168        75    125       150     330.4