# Create a module named cubed with a function that takes a 
# number as a parameter, and returns the number cubed. Import 
# and call the function from another module.

import cubed

number = input("Give me a number to be squared: ")

result = cubed.cube(int(number))

print(result)