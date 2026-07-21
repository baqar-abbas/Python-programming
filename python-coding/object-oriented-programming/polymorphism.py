class Shape:
    def area(self):
        print("Area is not defined")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Rectangle area: {self.length * self.width}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Circle area: {3.14159 * self.radius * self.radius:.2f}")


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print(f"Triangle area: {0.5 * self.base * self.height}")


shapes = [
    Rectangle(10, 5),
    Circle(7),
    Triangle(8, 6)
]

for shape in shapes:
    shape.area()