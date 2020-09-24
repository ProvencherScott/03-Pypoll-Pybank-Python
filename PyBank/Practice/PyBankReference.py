#Import the file and file path
import os
import csv
budget_csv = os.path.join("Resources","budget_data.csv")

#Print csv to look at the data
with open(budget_csv) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  print(next(csvreader))
  month = []
  revenue = []
  revenue_change = []
  monthly_change = []


#![Revenue](Images/revenue-per-lead.png)
#* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. # You will give 
#Months
  for row in csvreader:
    month.append(row[0])
    revenue.append(row[1])
  print(len(month))
  #Revenue
  revenue_int = map(int,revenue)
  total_revenue = (sum(revenue_int))
  print(total_revenue)
  #Avg change
  i = 0
  for i in range(len(revenue) -1):
    profit_loss = int(revenue[i+1]) - int(revenue[i])
    revenue_change.append(profit_loss)
  Total = sum(revenue_change)
  monthly_change = Total / len(revenue_change)
  print(monthly_change)

  # print(profit_loss)
  
  #Greatest Increase
  profit_increase = max(revenue_change)
  print(profit_increase)
  j = revenue_change.index(profit_increase)
  month_increase = month [j+1]

  #Greatest Decrease
  profit_decrease = min(revenue_change)
  print(profit_decrease)
  k = revenue_change.index(profit_decrease)
  month_increase = month [k+1]  