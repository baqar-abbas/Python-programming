# Python Encapsulation

# Encapsulation is about protecting data inside a class.

# It means keeping data (properties) and methods together in a 
# class, while controlling how the data can be accessed from 
# outside the class.

# This prevents accidental changes to your data and hides the 
# internal details of how your class works.

# Private Properties
# In Python, you can make properties private by using a 
# double underscore __ prefix:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

  def display_age(self):
    print(f"{self.name} is {self.__age} years old.")

p1 = Person("Emil", 25)
print(p1.name)
# print(p1.__age) # This will cause an error
p1.display_age()