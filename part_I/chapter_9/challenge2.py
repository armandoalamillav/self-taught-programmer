# Write a program that asks a user a question, 
# and saves their answer to a file.

answer = input ("What is your name? ")

with open("ch2.txt", "w") as f:
    f.write(answer)
