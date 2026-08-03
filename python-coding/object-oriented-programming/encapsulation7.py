# Python Encapsulation

# Encapsulation is about protecting data inside a class.

# Name Mangling
# Name mangling is how Python implements private properties and methods.

# When you use double underscores __, Python automatically renames it internally by adding _ClassName in front.

# For example, __age becomes _Person__age.

# Example
# See how Python mangles the name:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended!

# Note: While you can access private properties using the mangled 
# name, it's not recommended. It defeats the purpose of 
# encapsulation.