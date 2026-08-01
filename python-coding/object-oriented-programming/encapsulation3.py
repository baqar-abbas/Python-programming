# Python Encapsulation

# Encapsulation is about protecting data inside a class.

# Get Private Property Value
# To access a private property, we can create a getter method:

# Example
# Use a getter method to access a private property:

# Set Private Property Value
# To modify a private property, you can create a setter method.

# The setter method can also validate the value before setting it:

# Example
# Use a setter method to change a private property:

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Please enter a valid age")


p1 = Person("Tobias", 25)
print(p1.name)
print(p1.get_age())
p1.set_age(30)
print(p1.get_age())