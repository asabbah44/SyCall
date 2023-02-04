
import pandas as pd

# File names
filename = "temp.csv"
new_data_filename = "out.txt"


# Read the existing CSV file and store the headers
with open(filename, "r") as f:
    headers = f.readline().strip().split(',')
    content = f.read()

# Read the new data file and store the new data as a dictionary
new_data = {}
with open(new_data_filename, "r") as f:
    for line in f:
        for key_value_pair in line.strip().split(','):
            key, value = key_value_pair.strip().split(':')
            new_data[key.strip()] = value.strip()

# Append the new data to the existing content, using the headers to fill in missing values
row = []
for header in headers:
    if header in new_data:
        row.append(new_data[header])
    else:
        row.append('0')
content += ','.join(row) + '\n'

# Write the result back to the existing file
with open(filename, "w") as f:
    f.write(','.join(headers) + '\n')
    f.write(content)
