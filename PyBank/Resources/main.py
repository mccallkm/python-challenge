
#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The total net amount of "Profit/Losses" over the entire period
#The average change in "Profit/Losses" between months over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#Beginning of Python Script to Analyse Results of Budget Data

# Modules 
import os
import csv
import sys

# Set path for file
csvpath = os.path.join("..","Resources","budget_data.csv")

# Attempt to set variables?
total_months = 0
total_netprofit = 0
greatest_incr = -sys.maxsize - 1
greatest_incr_date = ''
greatest_decr = sys.maxsize
greatest_decr_date = ''

# Open and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

 # Loop calculations for data set budget_data.csv  to create total months, total profit, greatest inc/dec in profit
 # and average change
    for row in csvreader:
        total_months = total_months + 1
        total_netprofit = total_netprofit + int(row[1])
        average_change = round((greatest_decr - greatest_incr) /total_months, 2) 
        #print (total_months) - used to check max
        #if total_months >= 86:  
           #total_months = total_months
        if int(row[1]) >= greatest_incr:
            greatest_incr = int(row[1])
            greatest_incr_date = (row[0])
        if int(row[1]) <= greatest_decr:
            greatest_decr = int(row[1])
            greatest_decr_date = (row[0])

# Print results            
print(f"Financial Analysis")
print("--------------------------------------------------")
print (f"Total Months", ":", total_months)
print(f"Total", ":", "$", (total_netprofit))
print(f"Average Change: $" + str(average_change))
print(f"Greatest Increase in Profit: " + greatest_incr_date + " ($" + str(greatest_incr) + ")")
print(f"Greatest Decrease in Profit: " + greatest_decr_date + " ($" + str(greatest_decr) + ")")
print("--------------------------------------------------")

#Create path for output file
output_path = os.path.join('..',"Resources","output_budgetdata.csv")

with open(output_path, 'w', newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',') 

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['---------------------------------------------------------------------------------------------------']) 
    csvwriter.writerow(['Total Months', 'Total', 'Average Change','Greatest Increase in Profit',
    'Greatest Increase in Profit Month','Greatest Decrease in Profit','Greatest Decrease in Profit Month'])
    csvwriter.writerow([str(total_months),str(total_netprofit), str(average_change),str(greatest_incr),str(greatest_incr_date),
    str(greatest_decr), str(greatest_decr_date) ])
    csvwriter.writerow(['---------------------------------------------------------------------------------------------------'])

#Opens the output file in r - read mode and prints to terminal
with open(output_path, 'r') as readfile:
    print(readfile.read())