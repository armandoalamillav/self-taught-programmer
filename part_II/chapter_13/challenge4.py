# 4. Create a class called Horse and a class called Rider. 
# Use composition to model a horse that has a rider.

class Horse:
    def __init__(self, name, breed, rider):
        self.name = name
        self.breed = breed
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

r1 = Rider("John")

h1 = Horse("Spirit", "Mustang", r1)

print(f"", h1.rider.name)
