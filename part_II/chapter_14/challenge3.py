# 3. Write a function that takes two objects as parameters and returns 
# True if they are the same object, and False if not. 

class Dog:
    def __init__(self, name):
        self.name = name
    
    def compare(name1, name2):
        return name1 is name2
    
d1 = Dog("Baloo")

d2 = Dog("Panda")

print(Dog.compare(d1, d2))

d3 = d1

print(Dog.compare(d3, d1))
