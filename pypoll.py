#data we need to retrieve
#total number of votes cast
#complete list of candidates who received votes
#total number of votes each candidate received
#percentage of votes each candidate won
#winner of election based on popular vote 


# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter to 0
total_votes = 0

#delcare a candidate options list to hold all candidates
candidate_options = []

#empty dictionary to store candidate names with how many votes they have received
candidate_votes = {}

#variables to tracking winning stats
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #read headers row
    headers = next(file_reader)

    #print each row from csv file
    for row in file_reader:
        #add to total vote count
        total_votes += 1
        #delcare a candidate list
        candidate_name = row[2]

        #if statement to only add unique candidate names to candidate options list
        if candidate_name not in candidate_options:
            #add candidate name to candidate options list
            candidate_options.append(candidate_name)
            #begin tracking specific candidate vote count
            candidate_votes[candidate_name] = 0

        #add votes to specific candidate vote count
        candidate_votes[candidate_name] += 1    



    #determine percentage of votes for each candidate by iterating thru candidate list
    for candidate in candidate_votes:
        #retrieve vote count of candidate
        votes = candidate_votes[candidate]
        #calc percentage of votes
        vote_percentage = float(votes)/float(total_votes) * 100
        
        print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        #determine winner and if votes is greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if this is true, set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #set winning_candidate = to candidate
            winning_candidate = candidate

    #print results of analysis
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)    





   
    
