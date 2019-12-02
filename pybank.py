import os
import csv 

filepath = os.path.join("..", "Python_Challenge", "budget_data.csv")

with open(filepath, "r") as in_file:
    in_csv = csv.reader(in_file)
    csv_header = next(in_csv)
    # print(f"Header: {csv_header}")

    profit = []
    months = []
    revenue_change = []


    for row in in_csv:
        profit.append(int(row[1]))
        months.append(row[0])
    
    total_months = len(months)
    total_profit = sum(profit)
    
    for e in range(1, len(profit)):
        revenue_change.append((int(profit[e]) - int(profit[e-1])))
    
    revenue_average = sum(revenue_change) / len(revenue_change)
    greatest_increase = max(revenue_change)
    greatest_decrease = min(revenue_change)
  

    print("Financial Analysis")
    print("__________________________")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(round(revenue_average, 2)))
    print("Greatest Profit Increase: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    print("Greatest Profit Decrease: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))

  


    





