# An anagram is a word created by rearranging the letters of another word. 
# The word iceman is an anagram of cinema, because you can rearrange the 
# letters in either word to form the other. You can determine if two words 
# are anagrams by sorting the letters in each word alphabetically and testing if they are the same:

def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    if sorted(word1) == sorted(word2):
        return True
    else:
        return False
    

w1 = "icean"
w2 = "cinema"

print(anagram(w1, w2))