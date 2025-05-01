# 1. Add a square_list class variable to a class called Square so that every 
# time you create a new Square object, the new object gets added to the list.

class Square:
    
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self.side)

s1 = Square(3)
s2 = Square(4)
s3 = Square(5)

print(Square.square_list)
