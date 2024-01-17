import json
import csv

# Specify the path to your JSON file
json_file_path = 'AS\AS_1.json'

# Load the JSON file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Extract text values
text_values = []

for region_id, region_data in data["_via_img_metadata"].items():
    for region in region_data["regions"]:
        if "text" in region["region_attributes"]:
            text_value = region["region_attributes"]["text"]
            text_values.append(text_value)

print(text_values)
# Specify the CSV file path where you want to store the text values
csv_file_path = 'key_values.csv'

# Write the text values to a CSV file
with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the header
    csv_writer.writerow(['Key'])
    
    # Write the text values
    for text_value in text_values:
        csv_writer.writerow([text_value])

print(f'Text values extracted and stored in {csv_file_path}')