#Poll Data
#Create file Paths
import os
import csv

#Create file path
csv_path = os.path.join('Resources', 'election_data.csv')
#csv_path = 'C:\\Users\\Brandon\\Desktop\\UT Bootcamp Challenges\\Module 3 Challenge\\Python_Module-3\\PyPoll\\Resources\\election_data.csv'

#Set Variables
total_votes= 0
candidate_votes = {} 

with open(csv_path,'r') as csv_file:
    csvreader= csv.reader(csv_file, delimiter=",")
    next(csvreader)
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

#Print the Results
print("Election Results")
print(f"---------------------------------------------------------")
#Print Total Votes
print(f"Total Votes: {total_votes}")
print(f"---------------------------------------------------------")
#Print Candidates, votes percentage, votes
for candidate, votes in candidate_votes.items():
    percentage = (votes/total_votes) *100
    print(f"{candidate}:{percentage:.3f}% ({votes})")
print(f"---------------------------------------------------------")
#Print Winner
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
print(f"---------------------------------------------------------")

#Export results to a text file
ouput_file2 = "Financial_Analysis2.txt"
with open(ouput_file2, 'w') as file2:
     file2.write("Election Results\n")
     file2.write("--------------------------------------\n")
     file2.write(f"Total Votes: {total_votes}\n")
     file2.write("--------------------------------------\n")
     for candidate, votes in candidate_votes.items():
         percentage= (votes/total_votes) * 100
         file2.write(f"{candidate}:{percentage:.3f}% ({votes})\n")
     file2.write("--------------------------------------\n")
     file2.write(f"Winnner: {winner}\n")