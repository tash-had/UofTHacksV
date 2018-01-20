import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


# def implicit():
#     from google.cloud import storage
#
#     # If you don't specify credentials when constructing the client, the
#     # client library will look for credentials in the environment.
#     storage_client = storage.Client()
#
#     # Make an authenticated API request
#     buckets = list(storage_client.list_buckets())
#     print(buckets)
#
#
# # Instantiates a client
# client = vision.ImageAnnotatorClient()
#
# # The name of the image file to annotate
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     'resources/wakeupcat.jpg')
#
# # Loads the image into memory
# with io.open(file_name, 'rb') as image_file:
#     content = image_file.read()
#
# image = types.Image(content=content)
#
# # Performs label detection on the image file
# response = client.label_detection(image=image)
# labels = response.label_annotations
#
# print('Labels:')
# for label in labels:
#     print(label.description)


import os

import google.cloud.storage
#
# GOOGLE_APPLICATION_CREDENTIALS = 'my_project_48949-e778a8049af2.json'
#
# # def explicit_compute_engine(project):
# #     from google.auth import compute_engine
# #     from google.cloud import storage
# #
# #     # Explicitly use Compute Engine credentials. These credentials are
# #     # available on Compute Engine, App Engine Flexible, and Container Engine.
# #     credentials = compute_engine.Credentials()
# #
# #     # Create the client using the credentials and specifying a project ID.
# #     storage_client = storage.Client(credentials=credentials, project=project)
# #
# #     # Make an authenticated API request
# #     buckets = list(storage_client.list_buckets())
# #     print(buckets)
#
# # Create a storage client.
# storage_client = google.cloud.storage.Client()
#
# # TODO (Developer): Replace this with your Cloud Storage bucket name.
# bucket_name = 'uoft-bucket'
# bucket = storage_client.get_bucket(bucket_name)
#
# # TODO (Developer): Replace this with the name of the local file to upload.
# source_file_name = '1.jpeg'
# blob = bucket.blob(os.path.basename(source_file_name))
#
# # Upload the local file to Cloud Storage.
# blob.upload_from_filename(source_file_name)
#
# print('File {} uploaded to {}.'.format(
#     source_file_name,
#     bucket))

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "uoft-hack-786661112645.json"
# def implicit():
#     from google.cloud import storage
#
#     # If you don't specify credentials when constructing the client, the
#     # client library will look for credentials in the environment.
#     storage_client = storage.Client()
#
#     # Make an authenticated API request
#     buckets = list(storage_client.list_buckets())
#     print(buckets)
#
# # Instantiates a client
# client = vision.ImageAnnotatorClient()
#
# # The name of the image file to annotate
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     '1.jpeg')
#
# # Loads the image into memory
# with io.open(file_name, 'rb') as image_file:
#     content = image_file.read()
#
# image = types.Image(content=content)

# Performs label detection on the image file
# response = client.color(image=image)
# labels = response.label_annotations
# response = client.label_detection(image=image)
# labels = response.label_annotations
# print(labels)

# response = client.image_properties(image=image)
# props = response.image_properties_annotation
# # print(props)
# percent = 0.6
# color_list = props
# print(color_list)
# print(color_list.score)
# for c in color_list:
#     print(c)
# color_list = props.dominant_colors.colors
# for color in color_list[:1]:
#     print(color)
    # if
    # if 'score: ' in color:
    #     print(color)
    # rgb = color.red + color.green + color.blue
    # if rgb >= 720 and score >= 0.6

# print('Labels:')
# for label in labels:
#     print(label)

import shutil
import os

def detect_properties(path):
    """Detects image properties in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    print('Properties:')
    p = 0.6

    for color in props.dominant_colors.colors[:3]:
        rgb = color.color.red + color.color.green + color.color.blue
        if rgb >= 720 and color.score >= p:
            # shutil.copy(path, 'second_image')
            color = []
        elif rgb >= 720 and 0.60 <= color.score <= 0.75:
            shutil.copy(path, 'second_image')
        else:
            pass

        # elif rgb >= 720 and color.score >= p:
        #     shutil.copy(path, 'second_image')
        # print('score: {}'.format(color.score))
        # print('\tr: {}'.format(color.color.red))
        # print('\tg: {}'.format(color.color.green))
        # print('\tb: {}'.format(color.color.blue))
        # print('\ta: {}'.format(color.color.alpha))

# for filename in os.listdir("new_images"):
#     detect_properties('new_images' + '/' + filename)
# detect_properties('hmgoepprod (1).jpeg')
