# Functions in Python
# Functions are reusable blocks of code that perform a specific 
# task. They help organize code, avoid repetition, and make 
# programs more modular.

# 1. Defining and Calling Functions
# Basic Function

def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!

# Function with Parameters
def greet(name):
    print(f"Hello, {name}")

greet("Alice")  # Output: Hello, Alice

# Function with Return Value

def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8

# Multiple retunn values
def get_user_info():
    name = "Alice"
    age = 30
    return name, age

name, age = get_user_info()
print(f"Name: {name}, Age: {age}")  # Output: Name: Alice, Age: 30

def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [3, 1, 4, 1, 5]
min_num, max_num = get_min_max(nums)
print(f"Min: {min_num}, Max: {max_num}")  # Output: Min: 1, Max: 5

# 2. Types of Arguments

# Positional Arguments

def describe_person(name, age, city):
    print(f"{name} is {age} years old from {city}")

# Order matters
describe_person("Alice", 25, "NYC")
# Output: Alice is 25 years old from NYC

# Keyword Arguments

# Order doesn't matter with keywords
describe_person(age=30, city="LA", name="Bob")
# Output: Bob is 30 years old from LA

# Mix positional and keyword (positional first)
describe_person("Charlie", city="Chicago", age=35)
# Output: Charlie is 35 years old from Chicago

# Default Arguments

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")           # Output: Hello, Alice!
greet("Bob", "Hi")       # Output: Hi, Bob!
greet("Charlie", "Hey")  # Output: Hey, Charlie!

# Default value is evaluated only once at definition
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]  - Uses same list!

# Better way - avoid mutable default arguments
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# Variable-Length Arguments (*args)

# *args collects extra positional arguments as tuple
def sum_all(*numbers):
    print(f"Numbers: {numbers}")  # Tuple
    return sum(numbers)

print(sum_all(1, 2, 3))        # Output: 6
print(sum_all(1, 2, 3, 4, 5))  # Output: 15

# Mix regular params with *args
def multiply(multiplier, *numbers):
    return [multiplier * n for n in numbers]

print(multiply(2, 1, 2, 3))  # Output: [2, 4, 6]

# Keyword Variable-Length Arguments (kwargs)**

# **kwargs collects extra keyword arguments as dict
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# Output:
# name: Alice
# age: 25
# city: NYC

# Mix all argument types
def complex_func(required, *args, default="Default", **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

complex_func("must", 1, 2, 3, default="Custom", x=10, y=20)

# 3. Return Statement

# Single return
def square(x):
    return x ** 2

# Multiple returns (returns tuple)
def circle_props(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return area, circumference

a, c = circle_props(5)
print(f"Area: {a}, Circumference: {c}")

# Return None implicitly
def say_hello(name):
    print(f"Hello, {name}")
    # No return - returns None

result = say_hello("Alice")
print(result)  # Output: None

# Early return
def check_positive(number):
    if number < 0:
        return False
    return True

print(check_positive(5))   # Output: True
print(check_positive(-3))  # Output: False

# 4. Scope and Lifetime
# Local vs Global Variables

# Global variable
global_var = 100

def my_function():
    # Local variable
    local_var = 50
    print(f"Local: {local_var}")
    print(f"Global: {global_var}")

my_function()
# print(local_var)  # Error! local_var not accessible

# Modifying global variable
counter = 0

def increment():
    global counter  # Declare we're using global
    counter += 1

increment()
increment()
print(counter)  # Output: 2

# nonlocal Keyword (for nested functions)

def outer():
    x = 10
    
    def inner():
        nonlocal x  # Use x from outer scope
        x += 5
        print(f"Inner: {x}")
    
    inner()  # Output: Inner: 15
    print(f"Outer: {x}")  # Output: Outer: 15

outer()

