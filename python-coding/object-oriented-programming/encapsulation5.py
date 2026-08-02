# Python Encapsulation

# Encapsulation is about protecting data inside a class.

# Protected Properties
# Python also has a convention for protected properties using a single underscore _ prefix:

# Example
# Create a protected property:

class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) # Can access, but shouldn't