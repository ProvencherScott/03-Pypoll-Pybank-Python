import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#establish a list
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
        
    # need to print length at the end.
    # print(len(months))
    print(len(months))

    # Need to print the net total at the end.
    print(sum(profit_losses))

    # (len(profit_losses))
    # looping over the above list
    for i in range(1,len(profit_losses)):
        # print(i)
        # print(profit_losses[i])
        # print(profit_losses[i-1])
        profit_loss_differential.append(profit_losses[i] - profit_losses[i-1])
        Total = sum(profit_loss_differential)

    # This is correct. Need to print this at the end.
    print(int(sum(profit_loss_differential)/len(profit_loss_differential))) 
    print ("what it is")  
    print(profit_loss_differential[0])

    profit_increase = max(profit_loss_differential)
    print(profit_increase)

    profit_decrease = min(profit_loss_differential)
    print(profit_decrease)



    # THIS IS THE LAST STEP PR
     #print(f"Total Months" & {name}")
    # print(f"Total: {str(win_percent)}")
    # print(f"Average Change: {str(loss_percent)}")
    # print(f"DRAW PERCENT: {str(draw_percent)}")
    # print(f"{name} is a {type_of_wrestler}")



    # use sum to get the net total amount of profit/losses
    #profit_losses.append(net_total)


    # testing
    

    
    


    # Define the function and have it accept the 'wrestler_data' as its sole parameter
    # ef print_monthcount(dates_data)

    # For readability, it can help to assign your values to variables with descriptive names
    # date = str(dates_data[0])

    

    #len() is used for length, the total of months
    # For Profits, for loop to go throught the prfits (i + 1)







    