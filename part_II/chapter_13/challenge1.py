# 1. Create Rectangle and Square classes with a method called calculate_perimeter 
# that calculates the perimeter of the shapes they represent. 
# Create Rectangle and Square objects and call the method on both of them.

class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_perimeter(self):
        return (self.base * 2) + (self.height * 2)
    
class Square:
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        return self.side * 4
    

rect = Rectangle(2, 4)
rect_perimeter = rect.calculate_perimeter()
print(rect_perimeter)

sq = Square(4)
sq_perimeter = sq.calculate_perimeter()
print(sq_perimeter)