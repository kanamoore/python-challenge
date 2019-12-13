import os
import csv

pypoll_file = os.path.join("election_data.csv")
total_vote = 0
candidate_list = []

found = True

with open(pypoll_file,"r",newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ",")
    file_header = next(csvreader)

    for row in csvreader:
        #The total number of votes cast
        total_vote = total_vote + 1
        
        # A complete list of candidates who received votes
        if not row[2] in candidate_list:
            candidate_list.append(row[2])

        # For each candidate, count the number of votes
    for candidate in candidate_list:
        candidate_voted = 0
    
        for record in csvreader:
            if candidate == row[2]:
                candidate_voted = candidate_voted + 1
        
        
        # The total number of votes each candidate won
        #if candidates_voted[0] == row[2]:
        #    candidate1_total = candidate1_total + 1


        
        # The percentage of votes each candidate won


        

        # The winner of the election based on popular vote.

print(total_vote)
print(candidate_list)
print(candidate, candidate_voted)

"""
* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------

"""
