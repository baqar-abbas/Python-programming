# Personal Library Manager - Version 1.0

import json
import os

# File to store our library data
LIBRARY_FILE = "my_library.json"

def load_library():
    """Load the library from file"""
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r') as file:
            return json.load(file)
    return []  # Return empty list if file doesn't exist

def save_library(library):
    """Save the library to file"""
    with open(LIBRARY_FILE, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    """Add a new book to the library"""
    print("\n📖 Add a New Book")
    print("-" * 30)

    title = input("Title: ")
    author = input("Author: ")
    year = input("Year: ")

    # Create a book dictionary
    book = {
        "title": title,
        "author": author,
        "year": year,
        "read": False  # New books are unread by default
    }

    library.append(book)
    save_library(library)
    print(f"\n✅ '{title}' added to your library!")

def list_books(library):
    """Display all books in the library"""
    if not library:
        print("\n📭 Your library is empty. Add some books!")
        return
    print("\n📚 Your Library")
    print("-" * 50)
    for i, book in enumerate(library, 1):
        read_status = "✅ Read" if book["read"] else "📖 Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {read_status}")

def search_books(library):
    """Search for books by title or author"""
    if not library:
        print("\n📭 Your library is empty. Add some books first!")
        return
    
    print("\n🔍 Search Books")
    print("-" * 30)
    search_term = input("Enter title or author to search: ").lower()       

    found_books = []
    for book in library:
        if (search_term in book["title"].lower() or 
            search_term in book["author"].lower()):
            found_books.append(book)

    if found_books:
        print(f"\nFound {len(found_books)} book(s):")
        for i, book in enumerate(found_books, 1):
            read_status = "✅ Read" if book["read"] else "📖 Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {read_status}")
    else:
        print("No books found matching your search.")

def mark_read(library):
    """Mark a book as read"""
    if not library:
        print("\n📭 Your library is empty!")
        return
    
    list_books(library)
    try:
        book_num = int(input("\nEnter the number of the book you've read: ")) - 1
        if 0 <= book_num < len(library):
            library[book_num]["read"] = True
            save_library(library)
            print(f"✅ Marked '{library[book_num]['title']}' as read!")
        else:
            print("❌ Invalid book number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def delete_book(library):
    """Delete a book from the library"""
    if not library:
        print("\n📭 Your library is empty!")
        return
    
    list_books(library)
    try:
        book_num = int(input("\nEnter the number of the book to delete: ")) - 1
        if 0 <= book_num < len(library):
            removed = library.pop(book_num)
            save_library(library)
            print(f"🗑️ Deleted '{removed['title']}' from your library!")
        else:
            print("❌ Invalid book number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def main():
    """Main program loop"""
    library = load_library()
    
    while True:
        print("\n" + "="*50)
        print("        📚 PERSONAL LIBRARY MANAGER")
        print("="*50)
        print("1. 📖 Add a book")
        print("2. 📋 List all books")
        print("3. 🔍 Search books")
        print("4. ✅ Mark book as read")
        print("5. 🗑️ Delete a book")
        print("6. 🚪 Exit")
        print("="*50)
        
        choice = input("Choose an option (1-6): ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            list_books(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            mark_read(library)
        elif choice == "5":
            delete_book(library)
        elif choice == "6":
            print("\n👋 Thanks for using Library Manager! Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-6.")
        
        input("\nPress Enter to continue...")  # Pause before showing menu again

# Start the program
if __name__ == "__main__":
    main()

# Output:

# python library_manager.py

# ==================================================
#         📚 PERSONAL LIBRARY MANAGER
# ==================================================
# 1. 📖 Add a book
# 2. 📋 List all books
# 3. 🔍 Search books
# 4. ✅ Mark book as read
# 5. 🗑️ Delete a book
# 6. 🚪 Exit
# ==================================================
# Choose an option (1-6): 3

# 🔍 Search Books
# ------------------------------
# Enter title or author to search: Let US C

# Found 1 book(s):
# 1. Let US C by Robert Lafore (1993) - ✅ Read

# Press Enter to continue...

