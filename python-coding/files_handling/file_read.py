# Open a File on the Server
# We have the following file, located in the same folder as Python:

f = open("demofile.txt", "rt")  # Open the file in read text mode
content = f.read()  # Read the content of the file
print(f"Content of the demofile.text below")
print(content)  # Print the content to the console

# Close Files
# It is a good practice to always close the file when you are done with it.

# If you are not using the with statement, you must write a close statement in order to close the file:
f.close()  # Close the file when done

# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

print(f"Read only 5 characters from the file")
f = open("demofile.txt", "rt")  # Open the file in read text mode
print(f.read(5))


