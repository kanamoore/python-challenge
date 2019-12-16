import os
import csv

pypoll_file = os.path.join("election_data.csv")

# Set the counter as 0
total_vote = 0

# Open the file in read mode 
with open(pypoll_file,"r",newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ",")
	csvheader = next(csvreader)

# Create an empty dictionary 
	vote_summary = {}

	# Iterate over each candidate name in line 
	for row in csvreader: 
		total_vote = total_vote + 1
		
		#Set row[2] as candidate name for readability
		candidate_name = row[2]

		# Check if the candidate_name is already in dictionary
		if candidate_name in vote_summary: 
			# Increment count of candidate_name by 1 
			vote_summary[candidate_name] = vote_summary[candidate_name] + 1
			
		else: 
			# Add the candidate_name to dictionary with count 1 
			vote_summary[candidate_name] = 1


	vote_percentage = float(round(vote_summary[candidate_name] / total_vote * 100,2))

# Print the contents of dictionary 
	for key in list(vote_summary.keys()): 
		print(key, ":", vote_summary[key])