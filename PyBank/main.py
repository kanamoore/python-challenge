import os
import csv

PyBank_file = os.path.join("budget_data.csv")
# Set variables
net_total = months_count = greatest_increase =  greatest_decrease = 0
greatest_increase_month = greatest_decrease_month = ("")

# open the budget data file
with open(PyBank_file,"r",newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    file_header = next(csvreader)

    for row in csvreader:
        #the total number of months included in the dataset
        months_count = months_count + 1

        #The net total amount of "Profit/Losses" over the entire period
        net_total = int(net_total) + int(row[1])

        #The average of the changes in "Profit/Losses" over the entire period
        average_change = round(net_total / months_count,2)

        #The greatest increase in profits (date and amount) over the entire period
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0] 

        #The greatest decrease in losses (date and amount) over the entire period
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0] 

# Create an output file
output_file = os.path.join("pybank_ result.csv")
with open(output_file,"w",newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([f'Total Months: {months_count}'])
    writer.writerow([f'Total: {net_total}'])
    writer.writerow([f'Average Change : {average_change}'])
    writer.writerow([f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})'])
    writer.writerow([f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})'])


print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {months_count}')
print(f'Total: {net_total}')
print(f'Average Change : {average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')


"""
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)

"""