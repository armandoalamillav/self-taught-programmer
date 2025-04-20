# 4. Write a program with an infinite loop 
# (with the option to type q to quit) and a list of numbers. 
# Each time through the loop ask the user to
# guess a number on the list and tell them whether or not they guessed correctly.

numbers = [2, 10, 13, 4, 8]


while True:
    user = input("Guess a number or type q to quit: ")
    if user == 'q':
        break
    try:
        user = int(user)
    except ValueError:
        print("please type a number or q to quit")
    if user in numbers:
        print("You guessed correctly")
    else:
        print("Wrong!")
