# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exists

# "a" - Append - will create a file if the specified file does not exists

# "w" - Write - will create a file if the specified file does not exists

# Create a new file if it does not exist:
with open("myfile.txt", "x") as f:  # Open the file in create mode
    f.write("Hello World!")  # Write content to the file

# Open and read the file after the creating:
with open("myfile.txt", "r") as f:
    print(f.read())