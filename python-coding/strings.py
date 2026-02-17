# Different ways to create strings
single_quotes = 'Hello World'
double_quotes = "Hello World"
triple_quotes = """This is a
multi-line string"""
triple_single = '''This is also
multi-line'''

# Empty string
empty = ""

# String with escape characters
escaped = "He said, \"Python is awesome!\""
path = "C:\\Users\\Name"
newline = "First line\nSecond line"
tab = "Column1\tColumn2"

# String Characteristics

# Strings are immutable
text = "Hello"
# text[0] = "J"  # Error! Strings cannot be changed

# But you can reassign
text = "J" + text[1:]  # Creates new string
print(text)  # Output: Jello

# String length
message = "Python"
print(len(message))  # Output: 6

# String Operations

# String Concatenation

# Using + operator
first = "Hello"
second = "World"
result = first + " " + second
print(result)  # Output: Hello World

# Using join() method - more efficient for multiple strings
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # Output: Python is awesome

# String Repetition

print("Ha" * 3)     # Output: HaHaHa
print("-" * 20)     # Output: --------------------

# String Indexing and Slicing

text = "Python Programming"

# Indexing (starts at 0)
print(text[0])      # Output: P
print(text[3])      # Output: h
print(text[-1])     # Output: g (last character)
print(text[-2])     # Output: n (second last)

# Slicing [start:end:step]
print(text[0:6])    # Output: Python (positions 0 to 5)
print(text[7:])     # Output: Programming (position 7 to end)
print(text[:6])     # Output: Python (start to position 5)
print(text[7:12])   # Output: Progr
print(text[::2])    # Output: Pto rgamn (every 2nd character)
print(text[::-1])   # Output: gnimmargorP nohtyP (reverse)

# String Methods
# Python built-in methods for string manipulation:

# 1. Case Conversion Methods

text = "python Programming"

# Capitalize first letter

print(text.capitalize())

# Convert to uppercase
print(text.upper())

# Convert to lowercase
print(text.lower())           # Output: python programming

# Title case (first letter of each word capitalized)
print(text.title())           # Output: Python Programming

# Swap case
print(text.swapcase())        # Output: PYTHON pROGRAMMING

# Casefold (more aggressive lower() for comparisons)
text2 = "Straße"
print(text2.lower())          # Output: straße
print(text2.casefold())       # Output: strasse

# Searching and Finding Methods

text = "Python is awesome, Python is powerful"

# Find position (returns -1 if not found)
print(text.find("Python"))      # Output: 0
print(text.find("Python", 10))  # Output: 19 (start from position 10)
print(text.find("Java"))        # Output: -1

# Find position (raises ValueError if not found)
print(text.index("awesome"))    # Output: 10
# print(text.index("Java"))     # ValueError

# Count occurrences
print(text.count("Python"))     # Output: 2
print(text.count("is"))         # Output: 2

# Check start/end
print(text.startswith("Python"))  # Output: True
print(text.endswith("ful"))       # Output: True

# Find from right
print(text.rfind("Python"))       # Output: 19

# Validation Methods

# Check character types
print("Python123".isalnum())     # Output: True (alphanumeric)
print("Python 123".isalnum())    # Output: False (space not alnum)

print("Python".isalpha())        # Output: True
print("Python123".isalpha())     # Output: False

print("123".isdigit())           # Output: True
print("12.3".isdigit())          # Output: False

print("123".isnumeric())         # Output: True
print("½".isnumeric())           # Output: True (fraction)
print("²".isnumeric())           # Output: True (superscript)

print("abc".islower())           # Output: True
print("ABC".isupper())           # Output: True
print("Hello World".istitle())   # Output: True

print("   ".isspace())           # Output: True
print("Hello".isprintable())     # Output: True
print("\n".isprintable())        # Output: False

# Stripping and Padding Methods

# Removing whitespace
text = "   Hello World   "
print(text.strip())      # Output: "Hello World" (both ends)
print(text.lstrip())     # Output: "Hello World   " (left)
print(text.rstrip())     # Output: "   Hello World" (right)

# Remove specific characters
text = "***Hello***"
print(text.strip("*"))   # Output: Hello

# Padding
text = "Python"
print(text.center(20, "-"))    # Output: -------Python-------
print(text.ljust(20, "-"))     # Output: Python--------------
print(text.rjust(20, "-"))     # Output: --------------Python
print(text.zfill(10))          # Output: 0000Python

# Splitting and Joining Methods

# Split string into list
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)            # Output: ['apple', 'banana', 'orange']

# Split with max splits
text = "one,two,three,four"
print(text.split(",", 2))  # Output: ['one', 'two', 'three,four']

# Split into lines
multiline = "Line1\nLine2\nLine3"
print(multiline.splitlines())  # Output: ['Line1', 'Line2', 'Line3']

# Join list into string
fruits = ['apple', 'banana', 'orange']
print("-".join(fruits))        # Output: apple-banana-orange

# Partition (split into 3 parts)
text = "Python-Programming"
print(text.partition("-"))     # Output: ('Python', '-', 'Programming')
print(text.rpartition("-"))    # Output: ('Python', '-', 'Programming')

# Replacement Methods

text = "I like Python, Python is great"

# Replace substrings
print(text.replace("Python", "Java"))        # Output: I like Java, Java is great
print(text.replace("Python", "Java", 1))     # Output: I like Java, Python is great

# Translate (for multiple replacements)
# Create translation table
trans = str.maketrans("aeiou", "12345")
text = "hello world"
print(text.translate(trans))    # Output: h2ll4 w4rld

# Remove using translate
trans = str.maketrans("", "", "aeiou")
print(text.translate(trans))    # Output: hll 

# Formatting Methods

name = "Alice"
age = 30

# f-strings (Python 3.6+) - RECOMMENDED
print(f"My name is {name} and I am {age} years old")

# format() method
print("My name is {} and I am {} years old".format(name, age))
print("My name is {0} and I am {1} years old".format(name, age))
print("My name is {n} and I am {a} years old".format(n=name, a=age))

# % formatting (old style)
print("My name is %s and I am %d years old" % (name, age))

# Format specifiers
pi = 3.14159
print(f"{pi:.2f}")           # Output: 3.14
print(f"{pi:10.2f}")         # Output: "      3.14"
print(f"{1000000:,}")        # Output: 1,000,000
print(f"{0.25:.2%}")         # Output: 25.00%

# Other Useful Methods

# Check membership
text = "Python Programming"
print("Python" in text)       # Output: True
print("Java" not in text)     # Output: True

# Encode/Decode
text = "Python"
encoded = text.encode("utf-8")
print(encoded)                # Output: b'Python'
decoded = encoded.decode("utf-8")
print(decoded)                # Output: Python

# Expand tabs
text = "a\tb\tc"
print(text.expandtabs(10))    # Output: a         b         c

# Practical Examples

# String Validation

def validate_password(password):
    """Check if password meets criteria"""
    if len(password) < 8:
      return False, "Password is too short"
    if not any(c.isupper() for c in password ):
      return False, "Need upper case letter" 
    if not any(c.islower() for c in password):
        return False, "Need lowercase letter"
    if not any(c.isdigit() for c in password):
        return False, "Need at least one digit"
    return True, "Password valid"

password = "Python123"
is_valid, message = validate_password(password)
print(message)  # Output: Password valid

# String Cleaning

def clean_text(text):
    """Clean and normalize text"""
    # Remove extra whitespace
    text = " ".join(text.split())
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation (simple version)
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    text = "".join(c for c in text if c not in punctuation)
    return text

dirty_text = "  Hello!!!   World...   Python?  "
clean = clean_text(dirty_text)
print(clean)  # Output: hello world python

# String Parsing

# Extract email domains
emails = ["user1@gmail.com", "user2@yahoo.com", "user3@company.co.uk"]
domains = [email.split("@")[1] for email in emails]
print(domains)  # Output: ['gmail.com', 'yahoo.com', 'company.co.uk']

# Parse CSV line
csv_line = "John,Doe,30,New York"
fields = csv_line.split(",")
name, surname, age, city = fields
print(f"{name} {surname} is {age} years old from {city}")