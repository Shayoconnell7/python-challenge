import os
import csv
import collections


#tells program where to find the file
csvpath = os.path.join('resources', 'election-data.csv')

#opens the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    #identify header
    csv_header = next(csvreader)
    
    #sets starting value of the variable 'total_votes' to 0 so there is something to add to
    total_votes = 0
    #creates an empty list called 'options' where I will store candidate names
    options = []
    #creates an empty dictionary called 'votes' where I will store key-value pairs for candidate and votes received
    votes = {}
    
    for row in csvreader:
       #counts total number of votes and adds them to the variable 'total_votes'
        total_votes += 1
        #sets the index 2 to be called 'candidate_name
        candidate_name = row[2]

        #if the value found for candidate_name is not already in the list 'options', it will add it 
        # it will also set it as a key in 'votes' with the value of 1 
        if candidate_name not in options:            
            options.append(candidate_name)
            votes[candidate_name] = 1
        #if candidate_name is already in the list, it will add 1 to the running total stored in the value section of the dictionary    
        else:
            votes[candidate_name] += 1
#sets 'results as an emptry string
results = ""
#finds the percentage of total votes received for each candidate
for candidate in options:
        results += f"{candidate}: {votes[candidate]/(total_votes)*100:.3f}% ({votes[candidate]})\n"

#finds the candidate with the most votes and assigns them to the variable 'winner'
for candidate in options:
    if votes[candidate] == max(votes.values()):
        winner = candidate
   
#print results    
print(f"""
Election Results
---------------------------------
Total Votes: {total_votes}  
--------------------------------- 
{results}
---------------------------------
Winner: {winner}
---------------------------------
""")

#path to results output file
output_file = os.path.join('analysis','results.txt') 

#Open the output file and print results
with open(output_file, "w") as text_file:
    text_file.write (f"""
Election Results
---------------------------------
Total Votes: {total_votes}  
--------------------------------- 
{results}
---------------------------------
Winner: {winner}
---------------------------------
""")      
    

#references: class activites, slideshows, askBCS app, study group with classmates, Python documentation