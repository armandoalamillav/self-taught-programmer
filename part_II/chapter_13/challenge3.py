# 3. Create a class called Shape. Define a method in it called what_am_i that 
# prints "I am a shape" when called. Change your Square and Rectangle classes 
# from the previous challenges to inherit from Shape, create Square and Rectangle 
# objects, and call the new method on both of them.

class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_perimeter(self):
        return (self.base * 2) + (self.height * 2)
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        return self.side * 4

a_rect = Rectangle(2, 4)
a_rect.what_am_i()

a_square = Square(4)
a_square.what_am_i()