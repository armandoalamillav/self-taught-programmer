# write an algorithm that returns the number of times each character occurs in a string. 
# The algorithm will iterate character by character through the string, and keep track of 
# how many times each character occurs in a dictionary:

def cc(word):
    char_counts = {}
    for c in word:
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    return char_counts

w1 = "dynasty"
print(cc(w1))