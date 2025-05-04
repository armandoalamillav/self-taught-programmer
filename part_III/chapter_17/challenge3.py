# 3. Create a regular expression that matches any word that starts with 
# any character and is followed by two o's. Then use Python's re module to 
# match boo and loo in the sentence The ghost that says boo haunts the loo.

import re

s = "The ghost that says boo haunts the loo."

m = re.findall(".oo", s)

print(m)