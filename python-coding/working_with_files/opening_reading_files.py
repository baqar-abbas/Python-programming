# reading files

def read_file():
    # open the file in read mode
    file = open("characters.txt", "r")
    # read the contents of the file
    content = file.read()
    # print the contents of the file
    print(content)

    # read the file line by line
    lines = file.readlines()
    for line in lines:
        print(line)

    # close the file
    file.close()
    return

def main():
    read_file()
    return
    
if __name__ == "__main__":
    main()