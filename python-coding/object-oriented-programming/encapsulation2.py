# Python Encapsulation

# Encapsulation is about protecting data inside a class.

# Get Private Property Value
# To access a private property, we can create a getter method:

# Example
# Use a getter method to access a private property:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.name)
print(p1.get_age())