# Recursive algorithms rely on functions that call themselves. 
# Any problem you can solve iteratively can be solved recursively
# You write a recursive algorithm inside of a function. 
# The function must have a base case: a condition that ends a 
# recursive algorithm to stop it from continuing forever.

# Three laws of recursion: 
# 1. A recursive algorithm must have a base case.
# 2. A recursive algorithm must change its state and move toward the base case.
# 3. A recursive algorithm must call itself, recursively.

def bottles_of_beer(bob):
    """Prints 99 Bottle of Beer on the Wall lyrics.
    :param bob: Must be a positive integer"""

    # Rule 1, define a base case
    if bob < 1:
        print("No more bottles of beer on the wall. No more bottles of beer")
        return
    
    tmp = bob
    
    # Rule 2 change state and move toward the base case
    bob -= 1

    print("""{} bottles of beer on the wall. {} bottles of beer. Take one down, pass
          it around, {} bottle of beer on the wall""".format(tmp, tmp, bob))
    
    # Rule 3, call itself, recursively
    bottles_of_beer(bob) 

bottles_of_beer(99)