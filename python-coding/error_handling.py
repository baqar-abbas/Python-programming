# Error handling in Python using try-except blocks
# Error handling in Python is done using try-except blocks. 
# This allows you to catch and handle exceptions gracefully 
# without crashing the program.

# Basic try-except block
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Output: Error: division by zero

try:
    number = int(input("Enter a number: "))  # This may raise a ValueError
    print(f"You entered: {number}")
except ValueError as e:
    print("Invalid input! Please enter a valid number.")
    print(f"Error: {e}")
finally:
    print("This block will always execute.")