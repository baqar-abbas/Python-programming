# Check type of variable
x = 10
print(type(x))  # <class 'int'>

# Check if variable is specific type
print(isinstance(x, int))  # True
print(isinstance(x, (int, float)))  # True

# Type conversion
x = int("10")      # String to int
y = float(10)      # int to float
z = str(10)        # int to 

# Implicit conversion by Python
x = 10      # int
y = 3.14    # float
result = x + y  # Python automatically converts x to float
print(result)   # Output: 13.14
print(type(result))  # <class 'float'>

# Integer to complex
a = 5        # int
b = 2 + 3j   # complex
c = a + b    # a is converted to complex
print(c)     # Output: (7+3j)

# Explicit Casting

print(int(3.14))
print(int(9.99))      # Output: 9
print(int(-2.7))      # Output: -2

# From string to int (must be valid integer string)
print(int("100"))     # Output: 100
print(int("-50"))     # Output: -50
# print(int("3.14"))  # ValueError: invalid literal
# print(int("abc"))   # ValueError

# From boolean to int
print(int(True))      # Output: 1
print(int(False))     # Output: 0

# From other bases
print(int("1010", 2)) # Binary to int: 10
print(int("FF", 16))  # Hexadecimal to int: 255
print(int("17", 8))   # Octal to int: 15

# float() Casting
# Converts values to float type

# From int to float
print(float(10))      # Output: 10.0
print(float(-5))      # Output: -5.0

# From string to float
print(float("3.14"))  # Output: 3.14
print(float("7"))     # Output: 7.0
print(float("-2.5"))  # Output: -2.5
print(float("1e-3"))  # Output: 0.001

# From boolean to float
print(float(True))    # Output: 1.0
print(float(False))   # Output: 0.0

# Special cases
print(float("inf"))   # Output: inf
print(float("-inf"))  # Output: -inf
print(float("nan"))   # Output: nan

# str() Casting

# From int to str
print(str(123))           # Output: "123"
print(type(str(123)))     # <class 'str'>

# From float to str
print(str(3.14))          # Output: "3.14"

# From boolean to str
print(str(True))          # Output: "True"

# From list to str
print(str([1, 2, 3]))     # Output: "[1, 2, 3]"

# From other types
print(str(None))          # Output: "None"
print(str({"a": 1}))      # Output: "{'a': 1}"

# bool() Casting

# Converts values to boolean type

# Values that convert to False
print(bool(False))        # Output: False
print(bool(0))            # Output: False
print(bool(0.0))          # Output: False
print(bool(""))           # Output: False (empty string)
print(bool([]))           # Output: False (empty list)
print(bool({}))           # Output: False (empty dict)
print(bool(set()))        # Output: False (empty set)
print(bool(()))           # Output: False (empty tuple)
print(bool(None))         # Output: False

# Values that convert to True
print(bool(True))         # Output: True
print(bool(1))            # Output: True
print(bool(-5))           # Output: True
print(bool(3.14))         # Output: True
print(bool("Hello"))      # Output: True (non-empty string)
print(bool([1, 2]))       # Output: True (non-empty list)
print(bool({"a": 1}))     # Output: True (non-empty dict)

# Collection Type Casting

# list() Casting

# From tuple to list
print(list((1, 2, 3)))          # Output: [1, 2, 3]

# From string to list
print(list("hello"))             # Output: ['h', 'e', 'l', 'l', 'o']

# From set to list
print(list({1, 2, 3}))           # Output: [1, 2, 3]

# From dictionary (gets keys)
print(list({"a": 1, "b": 2}))    # Output: ['a', 'b']

# tuple() Casting

# From list to tuple
print(tuple([1, 2, 3]))          # Output: (1, 2, 3)

# From string to tuple
print(tuple("hello"))             # Output: ('h', 'e', 'l', 'l', 'o')

# From set to tuple
print(tuple({1, 2, 3}))           # Output: (1, 2, 3)

# set() Casting

# From list to set (removes duplicates)
print(set([1, 2, 2, 3, 3, 3]))   # Output: {1, 2, 3}

# From string to set
print(set("hello"))               # Output: {'h', 'e', 'l', 'o'}

# From tuple to set
print(set((1, 2, 2, 3)))          # Output: {1, 2, 3}

# dict() Casting

# From list of tuples to dict
print(dict([("a", 1), ("b", 2)]))  # Output: {'a': 1, 'b': 2}

# From tuples to dict
print(dict(a=1, b=2))              # Output: {'a': 1, 'b': 2}

# Advanced Casting

# Type Conversion

# Mixed type operations
age = 25
message = "I am " + str(age) + " years old"
print(message)  # Output: I am 25 years old

# Converting input (input() always returns string)
user_input = input("Enter a number: ")
number = int(user_input)  # Convert string to int
result = number * 2
print(f"Double is: {result}")


