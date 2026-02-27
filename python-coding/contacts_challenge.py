contacts = []

# CHALLENGE - create an add_contact function to add new contacts to the list
# each contact should be a dictionary with a name and email property

def add_contact(name, email):
  contact = {"name": name, "email": email}
  contacts.append(contact)
  return

# CHALLENGE - create a list_contacts function to print out all contacts
# each contact should be printed out on a new line with a name & email
# if there are no contacts yet, print out a "no contacts yet" message

def list_contacts():
  if len(contacts) == 0:
    print("No contacts yet.")
    return
  
  for contact in contacts:
        print(f"Name: {contact['name']} -- Email: {contact['email']}")

  return
  
def main():
  while True:
    print("1. Add Contact")
    print("2. List Contacts")
    print("3. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
            print('You chose option 1.')
            name = input('New contact name: ')
            email = input('New contact email: ')
            add_contact(name, email)
            continue
    elif choice == "2":
      print('You chose option 2.')
      list_contacts()
      continue
    elif choice == "3":
      print("Goodbye!")
      break
    else:
      print("Invalid option, please try again.")

if __name__ == "__main__":
  main()