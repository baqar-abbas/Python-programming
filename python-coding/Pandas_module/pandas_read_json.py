# Pandas Read JSON

# Read JSON
# Big data sets are often stored, or extracted as JSON.

# JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

# In our examples we will be using a JSON file called 'data.json'.

# Example
# Load the JSON file into a DataFrame:

import pandas as pd

df = pd.read_json('data.json')

print(df.to_string())

# Tip: use to_string() to print the entire DataFrame.