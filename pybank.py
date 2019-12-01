import os
import csv 

filepath = os.path.join("..", "Python_Challenge", "budget_data.csv")

with open(filepath, "r") as in_file:
    in_csv = csv.reader(in_file)

    header = next(in_csv)
    print(header)
    
    # for row in in_csv:
    #     print(row)
