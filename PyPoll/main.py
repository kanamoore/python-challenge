import os, csv

# Set the file path
pypoll_file = os.path.join("Resources","election_data.csv")

# Set the first value 
total_vote = 0
candidate_votes = {}
candidate_list = []
percentage_voted_list = []
winner = ""
winner_votes_count = 0

with open(pypoll_file,"r",newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ",")
    file_header = next(csvreader)

    for row in csvreader:
        # Count toal number of votes (count rows without header)
        total_vote = total_vote + 1
        
        # Set row[2] as candidate name for readability
        candidate_name = row[2]
        
        # If candidate name is already in the list, then keep adding one to get the vote count
        if candidate_name in candidate_list:
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

        # If candidate name is not in the list, put the name in the list 
        else:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 1

        # Loop through each candidate in vote summary and get he percentage of votes each candidate won
        for candidate in candidate_votes:
            #if candidate not in percentage_voted_list:
            votes = candidate_votes[candidate_name]
            #    percentage_voted = round((int(votes)/ total_vote * 100),2)
            #    percentage_voted_list.append(percentage_voted)

        # Determine the winner by comparing votes count for each candidate
            if (votes > winner_votes_count):
                winner_votes_count = votes
                winner= candidate
    
        # Ideal format is vote_summary = {"name" : ["vote_percentage", "vote_count"]

    # Show the result in terminal
    print(len(percentage_voted_list))
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes :  {total_vote}')
    print("-------------------------")
    for key in list(candidate_votes.keys()):
        print(f'{key} : ({candidate_votes[key]})')
    print("-------------------------")
    print(f'Winner : {winner}')
    print("-------------------------")

    # Export the result as csv file
output_file = os.path.join("pypoll_result.csv")
with open(output_file,"w",newline="") as datafile:
    csvwriter = csv.writer(datafile)

    csvwriter.writerow("Election Results")
    csvwriter.writerow("-------------------------")
    csvwriter.writerow(f'Total Votes :  {total_vote}')
    csvwriter.writerow("-------------------------")
    for key in list(candidate_votes.keys()):
        csvwriter.writerow(f'{key} : ({candidate_votes[key]})')
    csvwriter.writerow("-------------------------")
    csvwriter.writerow(f'Winner : {winner}')
    csvwriter.writerow("-------------------------")

    
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
