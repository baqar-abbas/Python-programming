# User Input Validation

def get_valid_age():
    while True:
        age_input = input("Enter your age: ")
        if not age_input:
            print("Age cannot be empty.")
        elif not age_input.isdigit():
            print("Age must be a number.")
        elif int(age_input) <= 0:
            print("Age must be a positive number.")
        else:
            return int(age_input)
        
age = get_valid_age()
print(f"Your age is {age}")

# Menu System

def show_menu():
    print("\n1. View Profile")
    print("2. Edit Profile")
    print("3. Logout")
    print("4. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        print("Viewing profile...")
    elif choice == "2":
        print("Editing profile...")
    elif choice == "3":
        print("Logging out...")
    elif choice == "4":
        print("Exiting...")
    else:
        print("Invalid option. Please try again.")

show_menu()

# Login System

def login_system():
    users = {
        "admin": "password123",
        "user": "pass456"
    }
    
    username = input("Username: ")
    password = input("Password: ")
    
    if username in users:
        if users[username] == password:
            print(f"Welcome, {username}!")
            return True
        else:
            print("Incorrect password")
    else:
        print("User not found")
    return False

login_system()