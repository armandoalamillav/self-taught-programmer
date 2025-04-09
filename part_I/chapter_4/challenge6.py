def input_squared(x):
    """
    Asks user for a number
    Returns the square of an input
    parameter x: int
    return x**2
    """
    
    print(x**2)

x = input("Give me a number, I'll square it: ")
input_squared(int(x))



def string_function(s):
    """
    Asks user for an input
    Prints back the input
    """
    print(s)

s = input("Give me a string: ")
string_function(s)



def parameters(x, y, z, a=1, b=2):
    """
    Asks user for three numbers
    Adds the user's input
    It also has two optional parameters a=1 and b=2
    It adds the user's input + a + b
    Returns the result of the addition 
    """
    print(x+y+z+a+b)

x = input("Give me a number: ")
y = input("Give me a number: ")
z = input("Give me a number: ")

parameters(int(x), int(y), int(z))



def divide(x):
    """
    Returns a number divided by 2
    """
    return x / 2

def mult4(x):
    """
    Takes a number and multiply it by 4
    """
    return x * 4

x = input("Give me a number: ")
result1= divide(int(x))
print("Result of your number/2 = ", result1)

result2= mult4(result1)
print("First result x 4 = ", result2)



def string_convert(s):
    """
    Asks the user for an input
    Tries to convert the input to float
    If it can't convert it, raise an error
    If it can convert it, it prints the new float value
    """
    try:
        result = float(s)
        print(result)
    except ValueError:
        print("I need a number")


x = input("Give me some input: ")

y = string_convert(x)