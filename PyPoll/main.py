import os
import csv

electioncsv = "election_data.CSV"

totalvotes = 0
candidates = {}
percentages ={}

with open(electioncsv, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader)
    
    for row in csvreader:
        
        totalvotes += 1
        
        
        if row[2] in candidates:
            candidates[row[2]] += 1
            
            
        else:
            
            candidates[row[2]] = 1
            
output_file = os.path.join("polling_output.txt")

#  Open the output file
with open(output_file, "w+", newline="") as datafile:
            
    print("Election Results")
    datafile.write("Election Results")
    datafile.write("\n")
    print("-----------------------")
    datafile.write("-----------------------")
    datafile.write("\n")
    print(f"Total Votes: {totalvotes}")
    datafile.write(f"Total Votes: {totalvotes}")
    datafile.write("\n")
    print("-----------------------")
    datafile.write("-----------------------")
    datafile.write("\n")

    for key in candidates:
    
        percentages[key] = (candidates[key]/totalvotes)*100
        
        winner = max(percentages.keys(), key = (lambda x: percentages[x]))
        
        percent = (candidates[key]/totalvotes)*100
        percent_new = "%.3f%%" % percent
        
        print(f"{key}: {percent_new} ({candidates[key]})")
        datafile.write(f"{key}: {percent_new} ({candidates[key]})")
        datafile.write("\n")
    
    print("-----------------------")
    datafile.write("-----------------------")
    datafile.write("\n")
    print(f"Winner: {winner}")
    datafile.write(f"Winner: {winner}")
    datafile.write("\n")
    print("-----------------------")
    datafile.write("-----------------------")
    datafile.write("\n")




