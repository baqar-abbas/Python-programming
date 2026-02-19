# 1. Basic If Statement

age = 18
if age >= 18:
    print("You are an adult")
    print("You can vote")
# Output: You are an adult
#         You can vote

# 2. If-Else Statement

temperature = 25
if temperature > 30:
    print("It's a hot day")
else:
    print("It's a nice day")
# Output: It's a nice day

# 3. If-Elif-Else Statement (Multiple conditions)

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is: {grade}")

# 4. Nested Conditionals

age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license to drive")
else:
    print("You are too young to drive")

# 5. Multiple Conditions with Logical Operators

# AND - both conditions must be True
age = 25
income = 50000
if age >= 18 and income > 30000:
    print("Eligible for loan")  # This runs

# OR - at least one condition must be True
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's weekend!")  # This runs

# NOT - reverses the condition
is_raining = False
if not is_raining:
    print("Let's go outside")  # This runs

# 6. Ternary Operator (Conditional Expression)

# Syntax: value_if_true if condition else value_if_false
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

# Another example
x = 10
result = "Positive" if x > 0 else "Negative or Zero"
print(result)  # Output: Positive

# Nested ternary (use sparingly)
num = 0
description = "Positive" if num > 0 else "Zero" if num == 0 else "Negative"
print(description)  # Output: Zero

# 7. Truthy and Falsy in Conditionals

# Values that evaluate to False
name = ""
if name:  # Same as if bool(name) == False
    print("Name exists")
else:
    print("Name is empty")  # This runs

# Values that evaluate to True
items = [1, 2, 3]
if items:  # Same as if bool(items) == True
    print(f"Has {len(items)} items")  # This runs

# # Common pattern
# data = get_data()  # Might return None
# if data:  # Check if data exists and is not empty
#     process(data)


# 8. Using 'in' Operator in Conditionals

# Check membership
fruits = ["apple", "banana", "orange"]
if "apple" in fruits:
    print("Apple is in the list")  # This runs

# Check in string
text = "Hello World"
if "World" in text:
    print("Found World")  # This runs

# Check in dictionary
user = {"name": "John", "age": 30}
if "name" in user:
    print(f"Name is {user['name']}")  # This runs

# 9. Using 'is' Operator in Conditionals

# Check for None
value = None
if value is None:
    print("No value")  # This runs

# Check for boolean
flag = True
if flag is True:
    print("Flag is True")  # This runs

# Check object identity
a = [1, 2, 3]
b = a
if a is b:
    print("Same object")  # This runs

# 10. Match Statement (Python 3.10+)

# Similar to switch-case in other languages
def describe_day(day):
    match day.lower():
        case "monday":
            return "Start of work week"
        case "friday":
            return "TGIF!"
        case "saturday" | "sunday":  # Multiple patterns
            return "Weekend!"
        case _:  # Default case
            return "Regular weekday"

print(describe_day("Monday"))    # Start of work week
print(describe_day("Sunday"))    # Weekend!
print(describe_day("Wednesday")) # Regular weekday

# Match with conditions (guards)
point = (2, 3)
match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"X-axis at {x}")
    case (0, y):
        print(f"Y-axis at {y}")
    case (x, y) if x == y:
        print(f"On diagonal at {x},{y}")
    case (x, y):
        print(f"Point at {x},{y}")

# 15. Best Practices
# python
#  Avoid deep nesting
# if condition1:
#     if condition2:
#         if condition3:
#             do_something()

#  Better - use early returns or combine conditions
# if not condition1:
#     return
# if not condition2:
#     return
# if condition3:
#     do_something()

#  Or combine with 'and'
# if condition1 and condition2 and condition3:
#     do_something()

#  Use descriptive variable names for conditions
# is_eligible = age >= 18 and has_license and not is_suspended
# if is_eligible:
#     rent_car()