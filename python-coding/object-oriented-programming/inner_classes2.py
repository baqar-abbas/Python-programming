# Python Inner Classes
# An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.

# Inner classes are useful for grouping classes that are only used in one place, making your code more organized.

# Accessing Inner Class from the Outside
# To access the inner class, create an object of the outer class, and then create an object of the inner class:

# Example
# Access the inner class and create an object:

class Outer:
  def __init__(self):
    self.name = "Outer"

  class Inner:
    def __init__(self):
      self.name = "Inner"

    def display(self):
      print("Hello from inner class")

outer = Outer()
print(outer.name)
inner = outer.Inner()
print(inner.name)
inner.display()