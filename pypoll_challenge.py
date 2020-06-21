#data we need to retrieve
#total number of votes cast
#complete list of candidates who received votes
#total number of votes each candidate received
#percentage of votes each candidate won
#winner of election based on popular vote
#number of votes cast from each county
#percentage of votes each county contributed to election


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

#empty dictionary to store candidate names as keys with how many votes they have received as values
candidate_votes = {}

#variables to tracking winning candidate stats
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#variables to track winning county 
winning_county = ""
county_count = 0
county_percentage = 0


#declare a list to hold all counties 
county_list = []

#empty dictionary to store county as key and votes cast as values 
county_votes = {}

#total county votes variable
total_county_votes = 0


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
        #add to total county vote count
        total_county_votes += 1
        #delcare a candidate list
        candidate_name = row[2]
        #declare a county name list
        county_name = row[1]


        #if statement to only add unique candidate names to candidate options list
        if candidate_name not in candidate_options:
            #add candidate name to candidate options list
            candidate_options.append(candidate_name)
            #begin tracking specific candidate vote count
            candidate_votes[candidate_name] = 0

        #add votes to specific candidate vote count
        candidate_votes[candidate_name] += 1

        #if statement to only add unique county names to county_list 
        if county_name not in county_list:
            #add county name to county_list
            county_list.append(county_name)
            # begin tracking specific county vote count
            county_votes[county_name] = 0
        #add votes to specific county vote count
        county_votes[county_name] += 1


    #save our results to a txt.file 
    with open(file_to_save, "w") as txt_file:    


        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        #determine percentage of votes for each county by iterating thru county_votes dictionary
        for county in county_votes:
            #retrieve vote count of county
            votes_county = county_votes[county]
            #calc percentage of votes
            percentage_vote = float(votes_county)/float(total_county_votes) * 100
            #print county results to terminal 
            county_results = (f"{county}: {percentage_vote:.1f}% ({votes_county:,})\n")
            print(county_results)
            #save county_results to our txt.file
            txt_file.write(county_results)
            

            #determine winning county
            if (votes_county > county_count) and (percentage_vote > county_percentage):
                # if this is true, set winning_count = votes and winning_percentage = vote_percentage
                county_count = votes_county
                county_percentage = percentage_vote
                #set winning_candidate = to candidate
                winning_county = county

        

        #print(winning_county_summary)
        winning_county_summary = (
        f"-------------------------\n"    
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
        # Save the winning candidate's name to the text file.
        txt_file.write(winning_county_summary)
        print(winning_county_summary)
               

        #determine percentage of votes for each candidate by iterating thru candidate dictionary
        for candidate in candidate_votes:
            #retrieve vote count of candidate
            votes = candidate_votes[candidate]
            #calc percentage of votes
            vote_percentage = float(votes)/float(total_votes) * 100
            #print candidate results to terminal
            candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            #save candidate_results to our txt.file
            txt_file.write(candidate_results)


            #determine winner and if votes is greater than winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # if this is true, set winning_count = votes and winning_percentage = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                #set winning_candidate = to candidate
                winning_candidate = candidate

        #print(winning_candidate_summary)
        winning_candidate_summary = (
        f"-------------------------\n"    
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)
        print(winning_candidate_summary)
            
        



        


        

        
         


        