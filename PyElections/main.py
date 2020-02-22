#Jason Johnson's PyElections code. Tested successfully on Python 3.8.0.
# Cell 617-999-6639

# import dependencies

import csv, os, sys
from collections import Counter

# Path to collect data from Resources folder

election = os.path.join("Resources", "houston_election_data.csv")
with open(election, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# remove the header
    next(csvreader)

# count number of unique elements (votes)
    votes = [row[0] for row in csvreader]

# create a dictionary of the # of votes per candidate
    count = Counter(votes)

# Find total votes cast.
votes_cast = (csvreader.line_num) - 1

# Sort the dictionary by the votes cast.
sorted_count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}

# Break the dictionary into tuples.
candidate_votes = [(k, v) for k, v in sorted_count.items()]

# break the tuples into lists.
candidate, votes = zip(*candidate_votes)

# convert the votes cast for each candidate into percentages.
percent = [round((j / votes_cast)*100, 2) for j in votes]

# print the output requested

print("Houston Mayoral Election Results")
print("-----------------------------------------")
print(f"Total Cast Votes: {str(votes_cast)}")
print("-----------------------------------------")
print(f"{(candidate[0])}: {(percent[0])}% ({(votes[0])})")
print(f"{(candidate[1])}: {(percent[1])}% ({(votes[1])})")
print(f"{(candidate[2])}: {(percent[2])}% ({(votes[2])})")
print(f"{(candidate[3])}: {(percent[3])}% ({(votes[3])})")
print(f"{(candidate[4])}: {(percent[4])}% ({(votes[4])})")
print(f"{(candidate[5])}: {(percent[5])}% ({(votes[5])})")
print(f"{(candidate[6])}: {(percent[6])}% ({(votes[6])})")
print(f"{(candidate[7])}: {(percent[7])}% ({(votes[7])})")
print(f"{(candidate[8])}: {(percent[8])}% ({(votes[8])})")
print(f"{(candidate[9])}: {(percent[9])}% ({(votes[9])})")
print(f"{(candidate[10])}: {(percent[10])}% ({(votes[10])})")
print(f"{(candidate[11])}: {(percent[11])}% ({(votes[11])})")
print("-----------------------------------------")
print(f"1st Advancing Candidate: {(candidate[0])}")
print(f"2nd Advancing Candidate: {(candidate[1])}")
print("-----------------------------------------")


filename = open("houston_election_results.txt", "w")
sys.stdout = filename
print("Houston Mayoral Election Results")
print("-----------------------------------------")
print(f"Total Cast Votes: {str(votes_cast)}")
print("-----------------------------------------")
print(f"{(candidate[0])}: {(percent[0])}% ({(votes[0])})")
print(f"{(candidate[1])}: {(percent[1])}% ({(votes[1])})")
print(f"{(candidate[2])}: {(percent[2])}% ({(votes[2])})")
print(f"{(candidate[3])}: {(percent[3])}% ({(votes[3])})")
print(f"{(candidate[4])}: {(percent[4])}% ({(votes[4])})")
print(f"{(candidate[5])}: {(percent[5])}% ({(votes[5])})")
print(f"{(candidate[6])}: {(percent[6])}% ({(votes[6])})")
print(f"{(candidate[7])}: {(percent[7])}% ({(votes[7])})")
print(f"{(candidate[8])}: {(percent[8])}% ({(votes[8])})")
print(f"{(candidate[9])}: {(percent[9])}% ({(votes[9])})")
print(f"{(candidate[10])}: {(percent[10])}% ({(votes[10])})")
print(f"{(candidate[11])}: {(percent[11])}% ({(votes[11])})")
print("-----------------------------------------")
print(f"1st Advancing Candidate: {(candidate[0])}")
print(f"2nd Advancing Candidate: {(candidate[1])}")
print("-----------------------------------------")