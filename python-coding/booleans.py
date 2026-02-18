#Booleans in Python

is_active = True
is_completed = False

print(is_active)
print(is_completed)
print(not is_active)

# comparison operators
x, y = 5, 10

print(x > y)
print(x < y)
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)

# boolean operators & member checking
x, y = True, False

# print(x and y)
# print(x or y)

# falsy values --> 0 numbers and empty data structs
# print(bool(0))
# print(bool(""))
# print(bool([]))

# truthy values --> everything else
# print(bool(1))
# print(bool("hello, ninjas"))
# print(bool([100, 99, 98]))


# evaluating strings
name = "mario"

print(name.startswith('m'))
print(name.startswith('a'))
print(name.endswith('o'))

# Membership Operators

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)  # True
print("grape" in fruits)   # False
print("grape" not in fruits)  # True

text = "Hello World"
print("Hello" in text)          # True
print("Python" in text)         # False

# Identity Operators

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is c)       # True (same object)
print(a is b)       # False (different objects)
print(a == b)       # True (same value)
print(a is not b)   # True

# Boolean in Control Flow
# If Statements

age = 18
if age >= 18:
    print("You can vote!")
else:
    print("You are too young to vote.")

# Short-circuit evaluation
x = 5
if x > 0 and 10/x > 1:  # Second condition only checked if first is True
    print("Valid")

# While Loops

count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1

# Ternary Operator

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)

# Boolean Methods
# String Boolean Methods

text = "Python123"
print(text.isalnum())   # True (alphanumeric)
print(text.isalpha())   # False (has numbers)
print(text.isdigit())   # False
print(text.islower())   # False
print(text.isupper())   # False
print(text.isspace())   # False
print(text.istitle())   # False

# Start/End with
print(text.startswith("Py"))  # True
print(text.endswith("123"))   # True

# List/Collection Boolean Methods

numbers = [1, 2, 3]
print(any(numbers))     # True (at least one True)
print(all(numbers))     # True (all are True)

mixed = [True, False, True]
print(any(mixed))       # True
print(all(mixed))       # False

# Check if all numbers are positive
nums = [1, 2, -3, 4]
print(all(n > 0 for n in nums))  # False

# Boolean in Real-World Examples
# User Authentication

def authenticate(username, password):
    valid_users = { "admin": "1234", "user": "abcd" }
    return username in valid_users and valid_users[username] == password

print(authenticate("admin", "1234"))  # True
print(authenticate("user", "wrong"))  # False

# Form Validation

def validate_form(data):
    is_valid = True
    errors = []
    
    if not data.get("name"):
        is_valid = False
        errors.append("Name is required")
    
    if not data.get("email"):
        is_valid = False
        errors.append("Email is required")
    elif "@" not in data["email"]:
        is_valid = False
        errors.append("Invalid email")
    
    return is_valid, errors

data = {"name": "John", "email": "john@email.com"}
valid, errors = validate_form(data)
print(valid)   # True
print(errors)  # []
