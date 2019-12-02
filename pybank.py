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
    # print(total_months)
    total_profit = sum(profit)
    # print(total_profit)

    for e in range(1, len(profit)):
        revenue_change.append((int(profit[e]) - int(profit[e-1])))
    
    revenue_average = sum(revenue_change) / len(revenue_change)
    # print(revenue_average)



