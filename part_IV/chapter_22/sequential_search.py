# Sequential search is a search done in a list (or similar) in which you iterate through
# every single item on that list

def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found

nl = [1, 2, 3, 4, 5]
n1 = 8

s1 = ss(nl, n1)
print(s1)
