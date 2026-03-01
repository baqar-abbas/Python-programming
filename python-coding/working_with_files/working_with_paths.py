from pathlib import Path

file = open("characters.txt", "r")

def create_path():
    
    # create a path object
    script_dir = Path(__file__).parent
    # print the path
    print(script_dir)
    # check if the path exists
    print(script_dir.exists())
    # # check if the path is a file
    print(script_dir.is_file())

    path = script_dir / "characters"

    path.mkdir(parents=True, exist_ok=True)

    file.close()

def main():
    create_path()
    return

if __name__ == "__main__":
    main()