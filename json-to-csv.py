import json
import csv

# Specify the input JSON file and output CSV file paths
input_json_file = 'C:/Users/laytoja/OneDrive - EY/Documents/Projects/ASS3T/enterprise-attack.json'
output_csv_file = 'C:/Users/laytoja/OneDrive - EY/Documents/Projects/ASS3T/enterprise-attack-converted.csv'

# Read the JSON data from the input file
with open(input_json_file, 'r') as json_file:
    data = json.load(json_file)

# Check if the JSON data is a list of dictionaries
if isinstance(data, list) and all(isinstance(item, dict) for item in data):
    # Extract the keys (column names) from the first dictionary
    column_names = data[0].keys()

    # Write data to the CSV file
    with open(output_csv_file, 'w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.DictWriter(csv_file, fieldnames=column_names)

        # Write the header (column names) to the CSV file
        csv_writer.writeheader()

        # Write each dictionary (row) as a CSV row
        csv_writer.writerows(data)
    print(f'Conversion completed. Data written to {output_csv_file}')
else:
    print('JSON data should be a list of dictionaries for conversion to CSV.')

