# 3. Take the items in this list of lists: 
# [["Top Gun", "Risky Business", "Minority Report"], 
# ["Titanic", "The Revenant", "Inception"], 
# ["Training Day", "Man on Fire", "Flight"]] 
# and write them to a CSV file. The data from each list 
# should be a row in the file, with each item in the list separated by a comma.

import csv

movies = [["Top Gun", "Risky Business", "Minority Report"], 
          ["Titanic", "The Revenant", "Inception"], 
          ["Training Day", "Man on Fire", "Flight"]]

with open ("ch3.csv", "w") as f:
    writing = csv.writer(f, delimiter=",")
    for movie in movies:
        writing.writerow(movie)
