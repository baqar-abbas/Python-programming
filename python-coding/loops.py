# Loops in Python

# 1. For Loop

# Iterarate over a list

fruits = ["banana", "apple", "mango"]
for fruit in fruits:
    print(fruit)

# Output: apple
#         banana
#         orange


# Iterate over a string

for char in "Python":
    print(char)
# Output: P y t h o n (each on new line)

# Iterate over a tuple

colors = ("red","green", "blue")
for color in colors:
    print(color)

# For Loop with range()

# range(stop) - 0 to stop-1

for i in range(5):
    print(i) # Output: 0 1 2 3 4

# range(start, stop)
for i in range(2, 6):
    print(i)  # Output: 2 3 4 5

# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)  # Output: 1 3 5 7 9

# Reverse range
for i in range(5, 0, -1):
    print(i)  # Output: 5 4 3 2 1

# For Loop with enumerate()

# Get both index and value
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
# Output: Index 0: apple
#         Index 1: banana
#         Index 2: orange

# Start index from 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# Output: 1. apple
#         2. banana
#         3. orange

# For Loop with zip()

# Iterate multiple sequences simultaneously
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old from {city}")
# Output: Alice is 25 years old from NYC
#         Bob is 30 years old from LA
#         Charlie is 35 years old from Chicago

# For Loop with Dictionaries

person = {"name": "John", "age": 30, "city":"NYC"}

for key in person:
    print(key) # Output: name age city

for value in person.values():
    print(value) # Output: John 30 NYC

# Iterate over key-value pairs

for key, value in person.items():
    print(f"{key}: {value}")

# Output: name: John
#         age: 30
#         city: NYC

# 2. While Loop

# Simple counter

count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
# Output: Count: 0,1,2,3,4

# User input until valid
password = ""
while len(password) < 8:
    password = input("Enter password (min 8 chars): ")
print("Password accepted!")

# While True Loop (Infinite)

# Use with break to exit

while True:
    user_input = input("Enter 'quit' to exit ")
    if user_input == "quit":
        break
    print(f"You entered {user_input}")

# 3. Loop Control Statements

# break - Exit the loop completely

# Stop loop when condition met
for i in range(10):
    if i == 5:
        break
    print(i)  # Output: 0 1 2 3 4

# Find first even number
numbers = [1, 3, 5, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"First even: {num}")
        break  # Output: First even: 8

# continue - Skip current iteration

# Skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Output: 1 3 5 7 9

# Skip vowels
word = "hello"
for char in word:
    if char in "aeiou":
        continue
    print(char)  # Output: h l l

# pass - Do nothing (placeholder)

# Placeholder for future code
for i in range(5):
    if i == 2:
        pass  # Will implement later
    else:
        print(i)  # Output: 0 1 3 4

# Empty loop (does nothing)
for i in range(10):
    pass

# else with Loops

# else executes when loop completes normally (no break)
for i in range(5):
    print(i)
else:
    print("Loop completed normally")
# Output: 0 1 2 3 4 Loop completed normally

# else won't execute if break occurs
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't print")
# Output: 0 1 2

# Useful for search operations
numbers = [1, 3, 5, 7, 9]
search_for = 4
for num in numbers:
    if num == search_for:
        print("Found!")
        break
else:
    print("Not found!")  # This runs

# 4. Nested Loops

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("-" * 10)

# Print pattern
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()
# Output:
# *
# **
# ***
# ****
# *****