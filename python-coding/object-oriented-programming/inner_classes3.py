# Python Inner Classes
# An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.

# Inner classes are useful for grouping classes that are only used in one place, making your code more organized.

# Accessing Outer Class from Inner Class
# Inner classes in Python do not automatically have access to the outer class instance.

# If you want the inner class to access the outer class, you need to pass the outer class instance as a parameter:

# Example
# Pass the outer class instance to the inner class:

class Outer:
  def __init__(self):
    self.name = "Emil"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()