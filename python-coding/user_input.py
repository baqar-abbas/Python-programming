import math


print("Enter your name: ")
name = input()
print(f"Hello, {name}!")

# Using prompt
# In the example above, the user had to input their name on a 
# new line. The Python input() function has a prompt parameter, 
# which acts as a message you can put in front of the user input,
#  on the same line:

name = input("Enter your name: ")
print(f"Hello, {name}!")

# Multiple Inputs
# You can add as many inputs as you want, Python will stop 
# executing at each of them, waiting for user input:

name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

# Input Number
# The input from the user is treated as a string. Even if, in the example above, you can input a number, the Python interpreter will still treat it as a string.

# You can convert the input into a number with the float() function:

age = float(input("Enter your age: "))
print(f"You are {age} years old.")

x = input("Enter a number:")

#find the square root of the number:
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")

# Validate Input
# It's good practice to validate the input from the user to ensure it's in the expected format. For example, you can check if the input is a valid number before converting it:

try:
    age = float(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid number for your age.")