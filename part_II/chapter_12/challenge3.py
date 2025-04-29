# 3. Create a Triangle class with a method called area that calculates and returns its area. 
# Then create a Triangle object, call area on it, and print the result.

class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def triangle_area(self):
        return (self.base * self.height) / 2
    
tri = Triangle(4, 2)
print(tri.triangle_area())