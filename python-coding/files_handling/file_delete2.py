# Python Delete File
# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

import os  # Import the OS module
if os.path.exists("demofile3.txt"):  # Check if file exists
    os.remove("demofile3.txt")  # Delete the file "demofile3.txt"
    print("The file has been deleted")  # Print a message if the file is deleted
else:
    print("The file does not exist")  # Print a message if the file does not exist