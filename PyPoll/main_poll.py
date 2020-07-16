import os
import csv

#join to election data csv
election_data = os.path.join("Resources", "election_data.csv")

#create empty lists so we can manipulate data
voter_id = []
county = []
candidate = []

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) 

    print(csv_header)

    for row in csvreader:
        #print(row[0], row[1], row[2])
        voter_id.append(int(row[0]))
        county.append(row[1])
        candidate.append(row[2])

#print header for results output
print("Election Results")
print("--------------------")

#print total number of votes, using voter ID
total_votes = len(voter_id)
print(f"Total Votes: {total_votes}")

#print separating line
print("--------------------")

#get complete list of candidates who received votes
candidates = ["Khan", "Correy", "Li", "O'Tooley"]






