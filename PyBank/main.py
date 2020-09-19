#import modules for increased abilities
import os
import csv

#create the path to get to the file I need to read
csvpath = os.path.join('resources', 'budget-data.csv')

#open the file
with open(csvpath) as csvfile:
    #call csv.reader, tell it what to read & identify delimiters, print title
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #identify header using 'next' function (reads one line)
    csv_header = next(csvreader)
 

    #count number of months
    #create empy list called rows
    rows = []
    #for each variable 'row' in the file 'csvreader', append the list rows to store data as a string for index [0] and a float for index [1]
    for row in csvreader:
        rows.append([row[0], float(row[1])])

    #set variable 'months' to be equal to the length of the list 'rows', and print
    months = len(rows)
  

    #each row is a list of 2 values (month, profit/loss), change_in_pl is a float that is read for each row
    #assign variable 
    # 'first_row' to start at index [0] of the list 'rows'
    first_row = rows [0]  
    #assign variable 'total' to start at 0 - so I have a strting point for adding values together
    total = 0
    #sets 'prev_month_profits_losses' to start at the value of first_row [1]
    prev_month_profits_losses = first_row [1]
    #sets an initial value for the greatest increase row that each subsequent row will be compared to
    greatest_increase_row = first_row
    #sets an initial value for the greatest decrease row that each subsequent row will be compared to
    greatest_decrease_row = first_row
    #sets initial value for total_change to 0 so that values can be added later
    total_change_in_pl = 0

    #a loop that reads the data for each row 
    for row in rows:
        #stores the float value found in [1] for each row as the variable profits_losses
        profits_losses = float(row[1])
        #tracks the change in the new profits_losses value and compares it to that of the previous month, storing the difference as the variable 'change'
        change_in_pl = profits_losses - prev_month_profits_losses 
        #sets the variable 'month' as equal to the information found in index [0]
        month = row[0]

        #adds the value found in [1], stored as the variable 'profits_losses', to the running total of all index [1] values
        total += profits_losses
        
        #adds the difference between this row's [1] and the previous row's, stored as the variable 'change', to the running total of all changes between index [1] values
        total_change_in_pl += change_in_pl

        #compares the most recent value for 'change' to the current greatest positive change, store whichever number is greater 
        if change_in_pl > greatest_increase_row [1]:
            greatest_increase_row = [month, change_in_pl]
     
        #compares the most recent value for 'change' to the current greatest negative change, store whichever number is less
        if change_in_pl < greatest_decrease_row [1]:
            greatest_decrease_row= [month, change_in_pl]

        #sets the value of this row's profits_losses to be stored now as prev_month_profits_losses, resetting for the next row to be compared
        prev_month_profits_losses = profits_losses

    #prints values calculated 
    print(f"""
    Financial Analysis
    ---------------------------------------
    Total Months: {months}   
    Total Profits: ${total}
    Average of Change in Profits: ${total_change_in_pl / (months - 1):.2f}
    Greatest Change in Profits: {greatest_increase_row[0]} {greatest_increase_row[1]}
    Greatest Decrease in Profits: {greatest_decrease_row[0]} {greatest_decrease_row[1]}
    """)

#create path to open output file
output_file = os.path.join('analysis','results.txt') 

#Open the output file and print results
with open(output_file, "w") as text_file:
    text_file.write (f"Financial Analysis\n")
    text_file.write (f"-------------------------------\n")       
    text_file.write (f"Total Months: " + str(months) + "\n")
    text_file.write (f"Total Profits: {total}\n")
    text_file.write (f"Average of Change in Profits: {total_change_in_pl / (months - 1):.2f}\n")
    text_file.write (f"Greatest Increase in Profits: {greatest_increase_row[0]} {greatest_increase_row[1]}\n")
    text_file.write (f"Greatest Decrease in Profits: {greatest_decrease_row[0]} {greatest_decrease_row[1]}\n")      
    
     

# references:
# https://stackoverflow.com/questions/16108526/count-how-many-records-are-in-a-csv-python
# class activites, slideshows, askBCS app, study group with classmates, Python documentation