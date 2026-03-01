# writing data t0 files

characters = ["Mario", "Luigi", "Peach", "Yoshi", "Bowser", "Toad"]

def write_to_file():
    # open the file in write mode
    file = open("characters2.txt", "w+")
    # write the characters to the file
    for character in characters:
        file.write(character + "\n")

    # read the contents of the file
    file.seek(0)  # move the cursor to the beginning of the file
    content = file.read()
    print(content)

    # close the file
    file.close()

    return

def main():
    write_to_file()
    return

if __name__ == "__main__":
    main()
