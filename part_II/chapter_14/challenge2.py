# 2. Change the Square class so that when you print a Square object, 
# a message prints telling you the len of each of the four sides of the shape. 
# For example, if you create a square with Square(29) and print it, 
# Python should print 29 by 29 by 29 by 29.

class Square:
    
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self.side)
    
    def __repr__(self):
        return f"{self.side} by {self.side} by {self.side} by {self.side}"

s1 = Square(3)

print(s1)
