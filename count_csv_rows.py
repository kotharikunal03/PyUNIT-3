import csv

with open("file.csv") as f:
    reader = csv.reader(f)
    count = sum(1 for row in reader)

print(count)