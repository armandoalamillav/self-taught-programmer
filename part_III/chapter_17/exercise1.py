import re 

l = "Beautiful is better than ugly."
l2 = "Simple is better than complex."

matches = re.findall("Beautiful", l)

matches2 = re.findall("simple", l2, re.IGNORECASE)

print(matches)
print(matches2)

# findall: its parameters are a regular expression, then a string and returns a list of matches
# findall: you can also pass a final parameter like re.IGNORECASE