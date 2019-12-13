import os
import csv

pypoll_file = os.path.join("election_data.csv")
total_vote = 0
candidate_list = []
vote_count = 0

found = True

with open(pypoll_file,"r",newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ",")
    file_header = next(csvreader)

    for row in csvreader:
        #The total number of votes cast
        total_vote = total_vote + 1
        
        # Set row[2] as candidate name
        candidate_name = row[2]

        # A complete list of candidates who received votes
        if not candidate_name in candidate_list:
            candidate_list.append(candidate_name)

        #The total number of votes each candidate won
        for candidate in candidate_list:
            if candidate_list[0] == candidate_name:
                vote_count = vote_count + 1


        
        # The percentage of votes each candidate won


        

        # The winner of the election based on popular vote.

print(total_vote)
print(candidate_list)
print(candidate_name, vote_count)

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
