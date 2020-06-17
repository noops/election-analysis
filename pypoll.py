#data we need to retrieve
#total number of votes cast
#complete list of candidates who received votes
#total number of votes each candidate received
#percentage of votes each candidate won
#winner of election based on popular vote 


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # To do: read and analyze the data here. 

    # read and print header row
    headers = next(file_reader)
    print(headers)
    
