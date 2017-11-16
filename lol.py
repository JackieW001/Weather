import io
from google.cloud import vision
vision_client = vision.Client.from_service_account_json('key.json')
file_name = 'templates/bigmac.jpg'

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = vision_client.image(
        content=content, )

labels = image.detect_labels()
for label in labels:
    print(label.description)
