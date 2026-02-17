# Lists, Tuples, Sets, and Dictionaries in Python

# 1. Lists [ ] - Mutable, Ordered, Allows Duplicates

# Creating lists
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
empty = []

# List operations
fruits.append("orange")          # Add to end
fruits.insert(1, "grape")       # Insert at index
fruits.remove("banana")        # Remove by value
popped = fruits.pop()          # Remove and return last item
fruits[0] = "kiwi"             # Modify by index
print(fruits)                 # Output: ['kiwi', 'grape', 'cherry']
print(fruits[1:3])              # Slicing - Output: ['grape', 'cherry']

# List methods
numbers = [3, 1, 4, 1, 5]
numbers.sort()                 # [1, 1, 3, 4, 5]
numbers.reverse()              # [5, 4, 3, 1, 1]
print(len(numbers))            # 5
print(3 in numbers)            # True

# 2. Tuples ( ) - Immutable, Ordered, Allows Duplicates

# Creating tuples
coordinates = (10, 20) 
rgb = (255, 128, 0)
single = (42,)  # Note the comma for single element
mixed = (1, "hello", 3.14, True)
without_prentheses = 1, 2, 3  # Also creates a tuple

# Tuple operations (read only)
print(coordinates[0])          # Output: 10
print(rgb[1:])                # Output: (128, 0)
x, y = coordinates             # Unpacking
print(x, y)                   # Output: 10 20

# Cannot modify!
# coordinates[0] = 15           # Error!

# When to use: fixed data, dictionary keys

# 3. Sets { } - Mutable, Unordered, No Duplicates

# Creating sets
unique_numbers = {1, 2, 3, 3, 3}     # {1, 2, 3}
fruits = {"apple", "banana", "apple"} # {"apple", "banana"}
empty_set = set()                      # Can't use {} (that's dict)

# Set operations
fruits.add("orange")                   # Add item
fruits.remove("banana")                 # Remove (error if missing)
fruits.discard("grape")                 # Remove (no error)

# Set mathematics
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)      # Union: {1, 2, 3, 4, 5}
print(set1 & set2)      # Intersection: {3}
print(set1 - set2)      # Difference: {1, 2}
print(set1 ^ set2)      # Symmetric diff: {1, 2, 4, 5}

# 4. Dictionaries {key: value} - Mutable, Ordered (3.7+), Keys Unique

# Creating dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
empty_dict = {}
another = dict(name="Alice", age=25)   # Using dict()

# Dictionary operations
print(person["name"])                   # John
person["age"] = 31                       # Modify
person["email"] = "john@email.com"       # Add new
del person["city"]                        # Delete

# Dictionary methods
print(person.keys())     # dict_keys(['name', 'age', 'email'])
print(person.values())   # dict_values(['John', 31, 'john@email.com'])
print(person.items())    # dict_items([('name', 'John'), ('age', 31), ...])

# Safe access
print(person.get("phone", "Not found"))  # Not found

# When to Use What?
# List: Shopping list, student names, to-do items

# Tuple: Coordinates, RGB values, days of week

# Set: Unique visitors, tags, removing duplicates

# Dict: Phonebook, user profiles, configuration settings