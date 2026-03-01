# appending data to a file

more_characters = ["Diddy Kong", "Donkey Kong", "Wario"]

def append_to_file():
    # open the file in append mode
    file = open("characters2.txt", "a+")
    # write the characters to the file
    for character in more_characters:
        file.write(character + "\n")
    # read the contents of the file
    file.seek(0,0)  # move the cursor to the beginning of the file
    content = file.read()
    print(content)

    # close the file
    file.close()
    return

def main():
    append_to_file()
    return

if __name__ == "__main__":
    main()