x = None
print(x)  # Output: None
print(type(x))  # Output: <class 'NoneType'>

# Comparing to None
# To compare a value to None, use the identity operator is or is not
if x is None:
    print("x is None")  # Output: x is None
else:
    print("x is not None")

result = None
if result is not None:
  print("Result is ready")
else:
  print("No result yet")

# True or False
# None evaluates to False in a boolean context.

print(bool(None))

# Functions returning None
# Functions that do not explicitly return a value return None by default.

def my_function():
    print("Hello, World!")

result = my_function()
print(result)  # Output: None