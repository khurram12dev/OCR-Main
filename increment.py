import json

# Load the JSON data from the file
with open('AVID\AVID_1.json', 'r') as json_file:
    data = json.load(json_file)

# Define the amount by which you want to increase the width
increase_by_width = 60
increase_by_height = 50
increase_by_x = 0
increase_by_y = 0

# Loop through each region and update the "width" attribute
for image_id, image_data in data['_via_img_metadata'].items():
    for region in image_data['regions']:
        if 'shape_attributes' in region and 'width' in region['shape_attributes']:
            region['shape_attributes']['width'] += increase_by_width
            region['shape_attributes']['height'] += increase_by_height
            region['shape_attributes']['x'] += increase_by_x
            region['shape_attributes']['x'] += increase_by_y

# Save the updated JSON back to a file
with open('AVID\AVID_1.json', 'w') as updated_json_file:
    json.dump(data, updated_json_file, indent=4)

print("JSON file updated successfully.")