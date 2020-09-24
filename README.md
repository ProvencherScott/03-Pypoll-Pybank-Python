# Pypoll-Pybank-Python

Imported csv.files to create two scripts in Visual Studio to analyze specific data. Each file contained different information; budget_data.csv pertaining towards financial data (numeric) and election_data.csv pertaining to voters information (non-numeric). The files are located in the Resources folder for PyPoll and Pybank.

Utilized Python functions recently learned in class:

import/output

with open(csvpath, 'r')

append.(row[0])

len()

if and elif 

round(), sum(), min(), max(), print()



## PyBank

Python script results:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period (Calculating the average for this was very difficult. Used the append function to create a 
  profit_loss_differential.)

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period


## PyPoll

Python script results:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.
  
Attempted to create a text file of the results using the With open(output, 'w') function but, I found this to be very difficult. Some of the information converted to a text file 
but not all of the information. Text files are found in the Analysis folder.


 
