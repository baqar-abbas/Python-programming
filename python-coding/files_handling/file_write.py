# Python File Write
# Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

with open("demofile.txt", "a") as f:  # Open the file in append mode
    f.write(" Now the file has more content!")  # Append content to the file

#open and read the file after the appending:
with open("demofile.txt", "r") as f:  # Open the file in read mode
    print(f.read())  # Read and print the content of the file

