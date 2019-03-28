import os
import csv

electioncsv = "election_data.CSV"

totalvotes = 0
#maybe this should be a dictionary

candidates = {}
percentages ={}

with open(electioncsv, newline="") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader)
    
    for row in csvreader:
        
        totalvotes += 1
        
    #print(totalvotes)
        
        if row[2] in candidates:
            candidates[row[2]] += 1
            
            
        else:
            
            candidates[row[2]] = 1
            
            
#print(candidates)
            
print("Election Results")
print("-----------------------")
print(f"Total Votes: {totalvotes}")
print("-----------------------")

for key in candidates:
    
    
    if key in percentages:
        percentages[key] = (candidates[key]/totalvotes)*100
        
    else:
        percentages[key] = (candidates[key]/totalvotes)*100
        
    winner = max(percentages.keys(), key = (lambda x: percentages[x]))
        
    print(f"{key}: {(candidates[key]/totalvotes)*100}% ({candidates[key]})")
    
print("-----------------------")

#print(percentages)



print(f"Winner: {winner}")





