import os
from pdf2image import convert_from_path
from PIL import Image

# Input PDF file path
pdf_file = "NewPossibleDocs\[AGAD] Agricultural Addendum.pdf"

# Output folder path
output_folder = 'AGAD'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Convert PDF to images with specified dimensions (width, height)
images = convert_from_path(pdf_file, dpi=400, poppler_path="C:\\poppler\\Library\\bin")

# Save the images in the output folder
for i, image in enumerate(images):
    image_path = os.path.join(output_folder, f'AGAD_{i}.png') 
    image.save(image_path, 'PNG')
    print(image.size)
    print(f"{image_path} Image saved")

print("Successfuly completed")