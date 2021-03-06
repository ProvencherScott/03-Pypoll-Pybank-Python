#Import the file and file path
import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

#establish lists
votes = []
county = []
candidates = []
percentage_votes = []
khan = []
correy = []
li = []
otooley = []

#Print csv to look at the data
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
   
#vote count
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])
    total_votes = (len(votes))
    # print(total_votes)
#vote per candidate
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)

#Percentages
    khan_perc = round(((khan_votes / total_votes)*100),2)
    correy_perc = round(((correy_votes / total_votes)*100),2)
    li_perc = round(((li_votes / total_votes)*100),2)
    otooley_perc = round(((otooley_votes / total_votes)*100),2)

#Winner options
    if khan_perc > max(correy_perc, li_perc, otooley_perc):
        winner = "Khan"
    elif correy_perc > max(khan_perc, li_perc, otooley_perc):
        winner = "Correy"
    elif li_perc > max(khan_perc, correy_perc, otooley_perc):
        winner = "Li"
    elif otooley_perc > max(khan_perc, correy_perc, li_perc):
        winner = "O'Tooley"

#Results
    print(f"Election Results") 
    print(f"-------------------------------------" )
    print(f"Total Votes: {total_votes}")
    print(f"-------------------------------------" )
    print(f"Khan: {khan_perc}% ({khan_votes})")
    print(f"Correy: {correy_perc}% ({correy_votes})") 
    print(f"Li: {li_perc}% ({li_votes})")
    print(f"O'Tooley: {otooley_perc}% ({otooley_votes})")
    print(f"-------------------------------------" )
    print(f"Winner: {winner}")
    print(f"----------------------------" )


output = os.path.join("Analysis","pypoll_analysis.txt")

with open(output, "w") as poll_results:
    poll_results.write("Election Results\n")
    poll_results.write("-------------------------------------\n")
    poll_results.write("Total Votes: {}\n".format(total_votes))
    poll_results.write("-------------------------------------\n")
    poll_results.write(("{}\n".format('Khan')))
    poll_results.write(("{}\n".format('Correy')))
    poll_results.write(("{}\n".format('Li')))
    poll_results.write(("{}\n".format("O'Tooley")))
    poll_results.write("-------------------------------------\n")
    poll_results.write('Winner: {}'.format(winner))
    poll_results.write("-------------------------------------\n")
