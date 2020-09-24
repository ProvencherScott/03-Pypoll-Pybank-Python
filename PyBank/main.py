import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#establish lists
months = []
profit_losses = []
profit_loss_differential = []

print (csvpath)

# Open and Read the CSV file
with open(csvpath, 'r') as csvfile:
    # split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # Total months can be calculated by taking a count of the rows in a list
    for row in csvreader:
    # capture row[0] as the list
        months.append(row[0])
        # use length to get the total count of the list months
        
        # capture row[1] as the list
        profit_losses.append(int(row[1]))
        # use sum to get the net total of the list profit_losses
        
    # need to print length of months at the end.
    # print(len(months))

    # Need to print the net total at the end.
    # print(sum(profit_losses))

    # (len(profit_losses))
    # looping over the above list
    for i in range(1,len(profit_losses)):
        # print(i)
        # print(profit_losses[i])
        # print(profit_losses[i-1])
        profit_loss_differential.append(profit_losses[i] - profit_losses[i-1])
        Total = sum(profit_loss_differential)

    # This is correct. Need to print this at the end.
    # print(int(sum(profit_loss_differential)/len(profit_loss_differential)))  
    # print(profit_loss_differential[0])

    # the greatest increase in profits over the period
    profit_increase = max(profit_loss_differential)
    # print(profit_increase)

    # the greatest decrease in profits over the period
    profit_decrease = min(profit_loss_differential)
    # print(profit_decrease)

    # Print Results

    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total profits: {sum(profit_losses)}")
    print(f"Average Change: ${int(sum(profit_loss_differential)/len(profit_loss_differential))}")
    print(f"Greatest Increase in Profits: ${max(profit_loss_differential)}")
    print(f"Greatest Decrease in Profits: ${min(profit_loss_differential)}")

    

    









 