import os
import csv

pypoll_file = os.path.join("election_data.csv")

# create a dictionary. candidate name and number of votes will be stored


# Set the counter as 0
total_vote = received_vote = 0

# create a candidate list and number of votes as empty
candidate_list = []
received_vote = []

# Read the pypoll file and skip the header
with open(pypoll_file,"r",newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ",")
    file_header = next(csvreader,None)
 
    d = dict()
	# Iterate over each row[2] in line 
	for row in csvreader: 
        

		# Check if the row[2] is already in dictionary 
		if row[2] in d: 
			# Increment count of row[2] by 1 
			d[row[2]] = d[row[2]] + 1
		else: 
			# Add the row[2] to dictionary with count 1 
			d[row[2]] = 1


        #A complete list of candidates who received votes
        #if candidate_name not in candidate_list:
        #    candidate_list.append(candidate_name)

        # Count candidates in the list
        #number_of_candidate = len(candidate_list)
    
        # For each candidate, count the number of votes

        #for candidate in candidate_list:
        #    if candidate == candidate_name:
        #        received_vote = received_vote + 1
                #The percentage of votes each candidate won
        #        vote_percentage = round(received_vote / total_vote * 100,2)

            # Iterate over each word in line 

        #if candidate_name in vote_summary: 
            # Increment count of word by 1 
            #vote_summary[candidate_name] = vote_summary[candidate_name] + 1
        #else: 
            # Add the word to dictionary with count 1 
        #    vote_summary[candidate_name] = 1
  

for key in list(vote_summary.keys()): 
    print(key, ":", vote_summary[key]) 
        ""
        #counter = int(0)
        #while counter < number_of_candidate:
        #        if candidate_list[int(counter)] == candidate_name:
        #            received_vote = received_vote + 1
        #            counter = counter + 1

                    
        
        # The total number of votes each candidate won
        #if candidates_voted[0] == row[2]:
        #    candidate1_total = candidate1_total + 1

        


      # The winner of the election based on popular vote.
"""
# Print the contents of dictionary 
	for key in list(vote_summary.keys()): 
		print(key, ":", vote_summary[key]) 

#print(total_vote)
#print(candidate_list)
#print(candidate, received_vote, vote_percentage)

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
