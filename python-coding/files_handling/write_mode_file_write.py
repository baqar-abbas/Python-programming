# Overwrite Existing Content
# To overwrite the existing content to the file, use the w parameter:

with open("demofile2.txt", "w") as f:  # Open the file in write mode
    f.write("Woops! I have deleted the content!")  # Overwrite the content of the file

#open and read the file after the overwriting:
with open("demofile2.txt", "r") as f:  # Open the file in read mode
    print(f.read())  # Read and print the content of the file