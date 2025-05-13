# A palindrome is a word spelled the same way forward and backward. 
# You can write an algorithm that checks if a word is a palindrome by 
# reversing all the letters in the word and testing if the reversed word and 
# the original word are the same. If they are, the word is a palindrome:

def palindrome(word):
    word = word.lower()

    if word[::-1] == word:
        return True
    else:
        return False
    
w = "Anitalavalatina"
p = palindrome(w)

print(p)
