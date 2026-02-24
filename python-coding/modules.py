from helpers import add, multiply

def main():
    print('hello from inside the main function, in the app file')

    result = add(2, 3)
    print(f"2 + 3 = {result}")

    result = multiply(4, 5)
    print(f"4 * 5 = {result}")

if __name__ == "__main__":
    main()