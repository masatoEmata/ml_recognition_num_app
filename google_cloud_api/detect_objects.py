# https://cloud.google.com/vision/docs/detect-labels-image-client-libraries

import glob
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
img_paths = glob.glob('../data/zip/*.png')
file_name = os.path.abspath(img_paths[0])
print(file_name)

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)