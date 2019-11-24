#PyBank homework! Trying it without Jupyter for now

import os
import csv
csvpath = os.path.join('03-Python_Homework_PyBank_Resources_budget_data.csv')

months = []
revenue = []
revenue_change = []



with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    csvheader = next(csvreader)
    
    for row in csvreader:
        #Append month
        months.append(row[0])
        monthcounter = 0 + len(months)
        total_months = monthcounter
        #print(total_months)
        
        # #profit/loses total
        revenue.append(row[1])
        integer = [int(x) for x in revenue]
        total_revenue = sum(integer)
        #print(total_revenue)
    
        #revenue change 

        

        # revenue_change = next_revenue - current_revenue
        # current_revenue = revenue_change
        # print(revenue_change)
        #revenue_change.append(change)
        #print(change_number)

        #revenue_change.append(change)

        #greatest increase/decrease 
      


        
        
        #MaxIncreaseInProfits
        
 
        
        



    #print("Financial Analysis")
    #print("__________________")
    #print(f"Total Months: f{total_months}")
    #print(f"Total Revenue: " + "$"  )
    #print("Average Revenue Change: " + "$" + )
    #print("Greater Increase In Revenue: ")
    #print("Greatest Decrease in Revenue: ")


    #output_file=os.path.join("budget_data_file.txt")
    