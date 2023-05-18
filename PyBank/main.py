#Budget Data
#Create file Paths
import os
import csv

#Create file path
csvpath = os.path.join('Resources', 'budget_data.csv')
#csvpath = "C:\Users\Brandon\Desktop\UT Bootcamp Challenges\Module 3 Challenge\Python_Module-3\PyBank\Resources\budget_data.csv"

#Set variables in the dataset
total_months= 0 
net_total = 0 
changes=[]
previous_value = 0

greatest_increase_date= " "
greatest_increase_amount= float("-inf")

greatest_decrease_date= " "
greatest_decrease_amount= float("inf")

#Be able to read the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    next(csvreader) #this is to skip the first line

    for row in csvreader:
        if row:" " 
        total_months += 1
        net_total += int(row[1])

        current_value = int(row[1])
        if total_months> 1:
            change = current_value - previous_value
            changes.append(change)

            if change> greatest_increase_amount:
                greatest_increase_amount = change
                greatest_increase_date = row[0]

            if change< greatest_decrease_amount:
                greatest_decrease_amount = change
                greatest_decrease_date = row[0]   

        previous_value = current_value
average_change = sum(changes)/len(changes)

#Export results to a text file
ouput_file = "Financial_Analysis.txt"
with open(ouput_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------\n")
    file.write(f"Total number of months: {total_months}\n")
    file.write(f"Net Total Amount of 'Profit/Losses': ${net_total}\n")
    file.write(f"Average change in 'Profit/Losses': ${average_change:.2f}\n")
    file.write(f"Greatest increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    file.write(f"Greatest decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")

#PRINT OUT VALUES
#Total number of months
print(f"Total number of months: {total_months}")
#Total net total amount of "Profit/Losses" over the entire period
print(f"Net Total Amount of 'Profit/Losses': ${net_total}")
#Average Change
print(f"Average change in 'Profit/Losses': (${average_change})")
#Greatest increase in profits (date & month) over the entire period
print(f"Greatest increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
#Greatest decrease in profits (date & month) over the entire period
print(f"Greatest decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")