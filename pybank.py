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




