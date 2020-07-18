import os
import csv
import statistics
from statistics import mode

#join to election data csv
election_data = os.path.join("Resources", "election_data.csv")

#create empty lists so we can manipulate data
voter_id = []
county = []
candidate = []

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) 

    #print(csv_header)

    for row in csvreader:
        #print(row[0], row[1], row[2])
        voter_id.append(int(row[0]))
        county.append(row[1])
        candidate.append(row[2])
poll_data_zip = zip(voter_id, county, candidate)

#print header for results output
print("Election Results")
print("-------------------------")

#print total number of votes, using voter ID
total_votes = len(voter_id)
print(f"Total Votes: {total_votes}")

#print separating line
print("-------------------------")

#get complete list of candidates who received votes
candidate_list_set = set(candidate)
unique_candidate_list = (list(candidate_list_set))
#for names in unique_candidate_list:
    #print(names)

#get count and percentage of how many votes each candidate receieved by doing a list.count
li_count = candidate.count("Li")
li_percent = (li_count/total_votes)*100
print(f'Li: {round(li_percent, 3)}% ({li_count})')

khan_count = candidate.count("Khan")
khan_percent = (khan_count/total_votes)*100
print(f'Khan: {round(khan_percent, 3)}% ({khan_count})')

correy_count = candidate.count("Correy")
correy_percent = (correy_count/total_votes)*100
print(f'Correy: {round(correy_percent, 3)}% ({correy_count})')

otooley_count = candidate.count("O'Tooley")
otooley_percent = (otooley_count/total_votes)*100
print(f"O'Tooley: {round(otooley_percent, 3)}% ({otooley_count})")

#print separting line
print("-------------------------")

#find the winner of the election by popular vote
def popular_vote(candidate):
    return(mode(candidate))
print(f'Winner: {popular_vote(candidate)}')

#print analysis table ending line
print("-------------------------")

#print to .txt file

fh = open("poll_results.txt", "w")
fh.write('Election Results' + '\n' + 'Total Votes: ' + str(total_votes) + '\n' + 'Li: ' + str(round(li_percent, 3)) + " " + str(li_count) + '\n'
          + 'Khan: ' + str(round(khan_percent, 3)) + " " + str(khan_count) + '\n'
		  + 'Correy: ' + str(round(correy_percent, 3)) + " " + str(correy_count) + '\n'
		  + "O'Tooley: " + str(round(otooley_percent, 3)) + " " + str(correy_count) + '\n' + "Winner: Khan")
fh.close()



