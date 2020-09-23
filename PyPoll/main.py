import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#establish a list
votes = []
candidates = []
percentage_votes = []
total_khan = []
total_correy = []
total_li = []
total_otooley = []

print (csvpath)

# Open and Read the CSV file
with open(csvpath, 'r') as csvfile:
    # split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # Total months can be calculated by taking a count of the rows in a list
    for row in csvreader:
        # capture row[0] as the list
        votes.append(row[0])

    print(len(votes))