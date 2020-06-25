## main.py
## for PyPoll

import os
import csv

vote_count = 0
khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0

#open file of dates
csvpath = os.path.join("election_data.csv")
print(csvpath)
print("-----------------------------------")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Count the voters by counting the rows 
    next(csvreader) # Skip the headers
    for row in csvreader:
        vote_count = vote_count + 1
        if str(row[2]) == "Khan":
            khan_count += 1
        if str(row[2]) == "Correy":
            correy_count += 1
        if str(row[2]) == "Li":
            li_count += 1
        if str(row[2]) == "O'Tooley":
            otooley_count += 1
    #list = [khan_count, correy_count, li_count, otooley_count]
    if max(khan_count, correy_count, li_count, otooley_count) == khan_count:
        winner = "Khan"
    if max(khan_count, correy_count, li_count, otooley_count) == correy_count:
        winner = "Correy"
    if max(khan_count, correy_count, li_count, otooley_count) == li_count:
        winner = "Li"
    if max(khan_count, correy_count, li_count, otooley_count) == otooley_count:
        winner = "O'Tooley"
    k_percent = 100 * khan_count / vote_count
    c_percent = 100 * correy_count / vote_count
    l_percent = 100 * li_count / vote_count
    o_percent = 100 * otooley_count / vote_count
    print(f"NUMBER OF VOTERS: {vote_count} \n") 
    print(f"Khan: {k_percent}%")
    print(f"Correy: {c_percent}%")
    print(f"Li: {l_percent}%")
    print(f"O'Tooley: {o_percent}")
print("-----------------------------------")
print(f"WINNER: {winner}")

     