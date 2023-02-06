
import pandas as pd

# File names
filename = "temp2.csv"
new_data_filename = "out.txt"
import csv


# Read the existing CSV file and store the headers and content
headers = []
content = []
with open(filename, "r") as f:
    reader = csv.reader(f)
    headers = next(reader)
    content = [row for row in reader]

# Read the new data file and store the new data as a list of dictionaries
new_data = []
with open(new_data_filename, "r") as f:
    for line in f:
        row = {}
        for key_value_pair in line.strip().split(','):
            key, value = key_value_pair.strip().split(':')
            row[key.strip()] = value.strip()
        new_data.append(row)

# Append the new data to the existing content, using the headers to fill in missing values
for new_row in new_data:
    row = []
    for header in headers:
        if header in new_row:
            row.append(new_row[header])
        else:
            row.append('0')
    content.append(row)

# Write the result back to the existing file
with open(filename, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(content)
