# Object-oriented programming (OOP) in Python 
# is a way to structure code by modeling 
# real-world things as objects.

# In OOP:

# A class is a blueprint.
# An object is an instance created from that blueprint.
# Attributes are data (variables) inside an object.
# Methods are actions (functions) inside an object.

class Dog:
    def __init__(self, name, age):
        self.name = name # Attribute: name
        self.age = age    # Attribute: age
    
    def bark(self): # Method: bark
        return f"{self.name} says woof!"
    
# Create an object (instance) of the Dog class
my_dog = Dog("Bruno", 3)
dog2 = Dog("Luna", 5)

print(my_dog.name)  # Output: Bruno
print(my_dog.age)   # Output: 3
print(my_dog.bark()) # Output: Bruno says woof!

print(dog2.name)  # Output: Luna
print(dog2.age)   # Output: 5
print(dog2.bark()) # Output: Luna says woof!

# Core OOP Concepts in Python
# Encapsulation
# Keep data + behavior together in one class.
# Example: Dog keeps name, age, and bark() together.

# Inheritance
# Create a new class from an existing one to reuse code.

class Animal:
    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return "Meow"
    
# Polymorphism
# Different classes can use the same method name differently.

animals = [Cat(), Dog("Tommy", 2)]
for a in animals:
    print(a.speak() if hasattr(a, "speak") else a.bark())

# Abstraction
# Hide internal details, expose only what users need.
# You call dog.bark() without caring how it builds the string.

# Why OOP is useful
# Makes code cleaner and modular
# Easy to reuse and extend
# Better for large projects
# Models real-world systems naturally

# OOP is a powerful way to organize code, making it easier to manage and understand complex systems.

# simple Bank Account program using OOP

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")

# Create Objects
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

# Use Methods
account1.deposit(200)  # Alice's balance: 1200
account1.withdraw(300) # Alice's balance: 900
account1.show_balance() # Alice's balance: 900

account2.deposit(100)  # Bob's balance: 600
account2.withdraw(700) # Insufficient funds
account2.show_balance() # Bob's balance: 600