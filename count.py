import json
from collections import defaultdict

RPA_list = ['RPA_1', 'RPA_2', 'RPA_3', 'RPA_4', 'RPA_5', 'RPA_6', 'RPA_7', 'RPA_8', 'RPA_9', 
            'RPA_10', 'RPA_11', 'RPA_12', 'RPA_13', 'RPA_14', 'RPA_15', 'RPA_16']

def annot(RPA_list):
    rpa_annotations = []
    for rpa in RPA_list:
        with open(f'RPA_Residential_Purchase_Agreement_and_Joint_Escrow_Instructions/{rpa}.json', 'r') as json_file:
            data = json.load(json_file)
        for image_id, image_data in data['_via_img_metadata'].items():
            for region in image_data['regions']:
                # Pair annotation with image ID
                rpa_annotations.append((region['region_attributes']['text'], rpa))
    return rpa_annotations

annotations = annot(RPA_list)

def count_duplicates(annotations):
    duplicates = defaultdict(dict)
    for annotation, image_id in annotations:
        if annotation in duplicates:
            if image_id in duplicates[annotation]:
                duplicates[annotation][image_id] += 1
            else:
                duplicates[annotation][image_id] = 1
        else:
            duplicates[annotation] = {image_id: 1}
    
    # Filter to keep only duplicates
    return {annotation: ids for annotation, ids in duplicates.items() if len(ids) > 1 or list(ids.values())[0] > 1}

duplicates = count_duplicates(annotations)

for annotation, image_ids in duplicates.items():
    print(f"Annotation: {annotation}, Image IDs: {image_ids}")