txt = f"The price is 49 dollars"
print(txt)

# Placeholders and Modifiers
# To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.

price = 59
txt = f"The price is {price} dollars"
print(txt)

# A placeholder can also include a modifier to format the value.

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Perform Operations in F-Strings

txt = f"The price is {20 * 59} dollars"
print(txt)

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

# can perform if...else statements inside the placeholders:

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

# You can also call functions inside the placeholders:

def to_uppercase(x):
  return x.upper()

txt = f"Hello, {to_uppercase('world')}!"
print(txt)


# Execute Functions in F-Strings

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)