# Write a program that lets the user ask your height, color or author and 
# returns the result from the dictionary you created on challenge3.py

armando = {
    "height": "180", 
    "author": "JK Rowling", 
    "color": "black"
}

question = input("Select height, author or color: ")

if question in armando:
    q = armando[question]
    print(q)
else:
    print("Invalid question, try height, author or color")