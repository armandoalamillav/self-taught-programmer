# 5. Multiply all the numbers in the list 
# [8, 19, 148, 4] with all the numbers in the list 
# [9, 1, 33, 83], and append each result to a third list.

n1 = [8, 19, 148, 4]
n2 = [9, 1, 33, 83]
n3 = []

for number in n1:
    for number2 in n2:
        n3.append(number * number2)

print(n3)