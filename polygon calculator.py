# Base class for geometrical shapes
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclass for Rectangles
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Subclass for Squares (a special case of Rectangle)
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

# Usage examples
rectangle = Rectangle(5, 10)
square = Square(7)

print("Rectangle Area:", rectangle.area())          
print("Rectangle Perimeter:", rectangle.perimeter())  

print("Square Area:", square.area())                
print("Square Perimeter:", square.perimeter())        