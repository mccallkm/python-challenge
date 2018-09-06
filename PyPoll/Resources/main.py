#You will be given a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

#Import File as csv
import os
import csv
import sys

# File path 
csvpath = os.path.join("..","Resources","election_data.csv")

# declaring variables
vote_count = 0
candidates = {}
candidate_percentage = {}
winner = ''
winner_count = 0

# reading file
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)

    # finding total vote count; finding individual vote counts
    for row in csvreader:
        vote_count = vote_count + 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

# percentages for each candidate
for key, value in candidates.items():
    candidate_percentage[key] = round((value/vote_count) * 100, 2)

# finding the winner
for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]

# printing results
print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(vote_count))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidate_percentage[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

# creating new csv file
output_path = os.path.join('..',"Resources","output_electiondata.csv")

with open(output_path, 'w', newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',') 

csvwriter.writerow("Election Results" + "\n")
csvwriter.writerow("Total Votes: " + str(vote_count) + "\n")
for key, value in candidates.items():
    csvwriter.writerow(key + ": " + str(candidate_percentage[key]) + "% (" + str(value) + ") \n")
csvwriter.writerow("Winner: " + winner + "\n")

with open(output_path, 'r') as readfile:
    print(readfile.read())




