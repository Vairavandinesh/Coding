#Write a Python program to create a class called "Shape" with abstract methods for calculating area and 
# perimeter, and subclasses for "Rectangle", "Circle", and "Triangle".
class Shape:
    def __init__(self):
        self.length=None
        self.breadth=None
        self.height=None
class Rectangle(Shape):
    def __init__(self):
        self.length=None
        self.breadth=None
    def area(self):
        return self.length*self.breadth
    def breadth(self):
        return 2*(self.length+self.breadth)
class Circle(Shape):
    def __init__(self):
        self.radius=None
    def area(self):
        return 3.14*(self.radius**2)
    def perimeter(self):
        return 2*3.14*self.radius
class Triangle(Shape):
    def __init__(self):
        self.length=None
        self.breadth=None
        self.height=None
    def area(self):
        return 0.5*self.breadth*self.height
rect1=Rectangle()
rect1.length=2
rect1.breadth=2
print(rect1.area())
circ1=Circle()
circ1.radius=3
print(circ1.area())
print(circ1.perimeter())

