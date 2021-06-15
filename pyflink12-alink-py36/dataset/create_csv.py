import csv

source_file = "source.csv"

with open(source_file, 'w') as f:
    writer = csv.writer(f)
    num = 10
    i = 0
    while i < num:
        writer.writerow([i, "name" + str(i), i % 100, "2020-01-01"])
        i += 1

