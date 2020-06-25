## main.py 
## for PyBank
import os
import csv

# open file of dates and data
csvpath = os.path.join("budget_data.csv")
print("\n")
print(csvpath)

# Initialize variables to store data
profit = 0
total_months = 0
max_profit = 0
min_profit = 99999999

print("DATA SYNOPSIS")
print("------------------------")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Count the months by counting the rows 
    next(csvreader) # skip the header
    for row in csvreader:
        # Count the months
        total_months += 1
        # sum and print the net profit
        profit += int(row[1])
        #next(csvreader)
        #for row in csvreader:
        max_profit = max(int(column[1].replace(',', '')) for column in csvreader) 
    for row in csvreader: 
        min_profit = min(float(column[1].replace(',', '')) for column in csvreader)
        #  #min_profit = min(csvreader, key=lambda row: int(row[1]))
print(f"MONTHS: {total_months}")
print(f"PROFIT: {profit}")
avg_change = profit / total_months
print(f"AVERAGE CHANGE: {avg_change}")
        
#for row in csvreader:
#Find greatest increase in profit and print it 
  ## Method 1
#max_profit = max(csvreader, key=lambda row: int(row[1]))                        ## Method 2
print(f"MAX PROFIT: {max_profit}")


print(f"MIN PROFIT: {min_profit}")
print("------------------------")
