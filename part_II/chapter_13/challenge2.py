# 2. Define a method in your Square class called change_size 
# that allows you to pass in a number that increases or 
# decreases (if the number is negative) each side of a Square object by that number.

class Square:
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        return self.side * 4
    
    def change_size(self, new_size):
        self.side += new_size

a_square = Square(4)
print(a_square.calculate_perimeter())

a_square.change_size(-2)
print(a_square.calculate_perimeter())

