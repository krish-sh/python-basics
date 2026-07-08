# with open("data.txt", "r") as f:
#     for line in f:
#         print(line.strip())

import csv


# with open("students.csv", ) as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#           print(row["Name"],row["Score"])

data = [
    ["Name", "Age"],
    ["Ali", 20],
    ["Sara", 21]
]
with open("out.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerows(data)