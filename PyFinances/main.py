#Jason Johnson's PyFinances code. Tested successfully on Python 3.7.4.
# Cell 617-999-6639

# import dependencies

import csv, os, operator, sys
from numpy import diff

# Path to collect data from Resources folder

budget = os.path.join("Resources", "budget_data.csv")
with open(budget, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # remove the column headers
    next(csvreader)
    # create a dictionary from the csv
    budget_dict = {rows[0]:rows[1] for rows in csvreader}
    
# Break the dictionary into tuples.
net_month = [(k, v) for k, v in budget_dict.items()]

# break the tuples into lists.
net, month = zip(*net_month)

# change net into integers
net = [int(i) for i in net]

# figure out the changes in profit/loss from month to month
net_change = diff(net)
a = 0
net_change_adj = a + net_change

#Create dictionary of the net change and the date.
net_change_by_date = dict(zip(month, net_change_adj))

# Find total months.
total_months = (csvreader.line_num) - 1

# Sum all of the monthly net values.
sum_net = sum(net)

# Average all of the monthly net values.
avg_net_change = round((sum(net_change) / len(net_change)),2)

#perform a lookup of the value that matches these keys in dictionary
gr_increase_month = max(net_change_by_date.items(), key=operator.itemgetter(1))[0]
greatest_increase = max(net_change_by_date.items(), key=operator.itemgetter(1))[1]
gr_drop_month = min(net_change_by_date.items(), key=operator.itemgetter(1))[0]
greatest_drop = min(net_change_by_date.items(), key=operator.itemgetter(1))[1]

# print the output requested
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(sum_net)}")
print(f"Average Change: ${str(avg_net_change)}")
print(f"Greatest Incrase in Profits: {str(gr_increase_month)} (${str(greatest_increase)})")
print(f"Greatest Incrase in Profits: {str(gr_drop_month)} (${str(greatest_drop)})")


# save the output requested
filename = open("pyfinances_results.txt", "w")
sys.stdout = filename

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(sum_net)}")
print(f"Average Change: ${str(avg_net_change)}")
print(f"Greatest Incrase in Profits: {str(gr_increase_month)} (${str(greatest_increase)})")
print(f"Greatest Incrase in Profits: {str(gr_drop_month)} (${str(greatest_drop)})")