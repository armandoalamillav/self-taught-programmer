# 4. Make a Hexagon class with a method called calculate_perimeter 
# that calculates and returns its perimeter. 
# Then create a Hexagon object, call calculate_perimeter on it, and print the result.

class Hexagon():
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return (self.side * 6)
    
hex = Hexagon(4)
print(hex.calculate_perimeter())