# Import gcloud
import os,time
from PIL import Image
from google.cloud import storage


##
#img = Image.open('/home/pi/Documents/pi-face-recognition/image_processed.jpg')

#newImage = img.resize((800, 600), Image.ANTIALIAS)         

#newImage.save('/home/pi/Pictures/Door.JPEG', optimize=True, quality=95)
##

# Enable Storage
client = storage.Client.from_service_account_json(
        '/home/pi/Documents/Door-Secure-21c89e84f000.json')

# Reference an existing bucket.
bucket = client.get_bucket('door-4186f.appspot.com')

blob = bucket.blob("New.jpg")

blob.upload_from_filename('/home/pi/Documents/pi-face-recognition/image_processed.jpg')

print('File {} uploaded to {}.'.format(
    'image_processed.jpg',
    'New.jpg'))
