import os
import csv

budgetcsv = "budget_data.CSV"

#lists to store data
totalmonths = []
nettotal = []
averagechange = []


# Read in the CSV file
with open(budgetcsv, newline="") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader)
    
        
    for row in csvreader:
        
        totalmonths.append(row[0])
        nettotal.append(float(row[1]))
    
    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total: {sum(nettotal)}")
#print(f"Total: {nettotal}")
    print(f"Total Months: {len(totalmonths)}")
    
    
    for i in range(1, len(nettotal)):
        averagechange.append(nettotal[i] - nettotal[i-1])
        avgrevchange = sum(averagechange)/len(averagechange)
            
        maxrevchange = max(averagechange)
            
        minrevchange = min(averagechange)
            
        maxrevmonth = str(totalmonths[averagechange.index(maxrevchange) + 1])
        minrevmonth = str(totalmonths[averagechange.index(minrevchange) + 1])
            
    print("Avereage Revenue Change: $", avgrevchange)
    print("Greatest Increase in Revenue:", maxrevmonth,"($", maxrevchange,")")
    print("Greatest Decrease in Revenue:", minrevmonth,"($", minrevchange,")")
    
    
output_file = os.path.join("budget_output.txt")

#  Open the output file
with open(output_file, "w+", newline="") as datafile:
    
    datafile.write("Financial Analysis")
    datafile.write("\n")
    datafile.write("-----------------------------------")
    datafile.write("\n")
    datafile.write(f"Total: {sum(nettotal)}")
    datafile.write("\n")
    datafile.write(f"Total Months: {len(totalmonths)}")
    datafile.write("\n")
    datafile.write(f"Avereage Revenue Change: ${avgrevchange}")
    datafile.write("\n")
    datafile.write(f"Greatest Increase in Revenue: {maxrevmonth} ($ {maxrevchange} )")
    datafile.write("\n")
    datafile.write(f"Greatest Increase in Revenue: {minrevmonth} ($ {minrevchange} )")
 
        
        
    