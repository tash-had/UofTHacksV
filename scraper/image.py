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

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "uoft-hack-786661112645.json"


def detect_properties(path, color_pairs):
    """Detects image properties in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation

    for color in props.dominant_colors.colors[:3]:
        rgb = color.color.red + color.color.green + color.color.blue
        if rgb >= 720 and color.score > 0.75:  # all white piece of clothing
            color_pairs.append([[]])


        elif rgb >= 720 and 0.60 <= color.score <= 0.75:  # identifying 1 white piece of clothing
            color_pairs.append([[props.dominant_colors.colors[0].color.red,
                                 props.dominant_colors.colors[0].color.green,
                                 props.dominant_colors.colors[0].color.blue],
                                [props.dominant_colors.colors[1].color.red,
                                 props.dominant_colors.colors[1].color.green,
                                 props.dominant_colors.colors[1].color.blue]])

        elif rgb >= 720 and color.score < 0.60:
            if color == props.dominant_colors.colors[0]:
                color_pairs.append([[props.dominant_colors.colors[1].color.red,
                                 props.dominant_colors.colors[1].color.green,
                                 props.dominant_colors.colors[1].color.blue],
                                [props.dominant_colors.colors[2].color.red,
                                 props.dominant_colors.colors[2].color.green,
                                 props.dominant_colors.colors[2].color.blue]
                                ])
            elif color == props.dominant_colors.colors[1]:
                color_pairs.append([[props.dominant_colors.colors[0].color.red,
                                     props.dominant_colors.colors[0].color.green,
                                     props.dominant_colors.colors[0].color.blue],
                                    [props.dominant_colors.colors[2].color.red,
                                     props.dominant_colors.colors[2].color.green,
                                     props.dominant_colors.colors[2].color.blue]
                                    ])
            elif color == props.dominant_colors.colors[2]:
                color_pairs.append([[props.dominant_colors.colors[0].color.red,
                                     props.dominant_colors.colors[0].color.green,
                                     props.dominant_colors.colors[0].color.blue],
                                    [props.dominant_colors.colors[1].color.red,
                                     props.dominant_colors.colors[1].color.green,
                                     props.dominant_colors.colors[1].color.blue]
                                    ])


        # elif rgb >= 720 and color.score >= p:
        #     shutil.copy(path, 'second_image')
        # print('score: {}'.format(color.score))
        # print('\tr: {}'.format(color.color.red))
        # print('\tg: {}'.format(color.color.green))
        # print('\tb: {}'.format(color.color.blue))
        # print('\ta: {}'.format(color.color.alpha))

from server.ColorConversionLibrary import get_general_color

color_pairs = []
counter = 0
big_list = []
for filename in os.listdir("new"):
    print(filename)
    detect_properties('new/' + filename, color_pairs)
    # print(filename, color_pairs[counter])
    sep_color_pair = color_pairs[counter]
    small_list = []
    for li in sep_color_pair:
        if len(li) >=3:
            color = get_general_color(li[0], li[1], li[-1])
            small_list.append(list(color))
    big_list.append(small_list)
    counter += 1

# detect_properties('new_images/hmgoepprod (10).jpeg', color_pairs)
# print(color_pairs)
print('done 1')

def detect_web(path):
    """Detects web annotations given an image."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.web_detection(image=image)
    notes = response.web_detection

    # if notes.pages_with_matching_images:
    #     print('\n{} Pages with matching images retrieved')
    #
    #     for page in notes.pages_with_matching_images:
    #         print('Url   : {}'.format(page.url))
    #
    # if notes.full_matching_images:
    #     print ('\n{} Full Matches found: '.format(
    #            len(notes.full_matching_images)))
    #
    #     for image in notes.full_matching_images:
    #         print('Url  : {}'.format(image.url))
    #
    # if notes.partial_matching_images:
    #     print ('\n{} Partial Matches found: '.format(
    #            len(notes.partial_matching_images)))
    #
    #     for image in notes.partial_matching_images:
    #         print('Url  : {}'.format(image.url))

    if notes.web_entities:
        # print ('\n{} Web entities found: '.format(len(notes.web_entities)))
        return notes.web_entities[0].description
        # print('Score      : {}'.format(notes.web_entities[0].score))
        # print('Description: {}'.format(notes.web_entities[0].description))
        # for entity in notes.web_entities:
        #     print('Score      : {}'.format(entity.score))
        #     print('Description: {}'.format(entity.description))

description_list = []
for filename in os.listdir("new"):
    description = detect_web('new' + '/' + filename)
    description_list.append(description)
# detect_properties('hmgoepprod (1).jpeg')

print('done 2')

import sqlite3
conn = sqlite3.connect('/Users/Rahul/Desktop/UofTHacksV/scraper/db.scraper', check_same_thread=False)
c = conn.cursor()
# c.execute('CREATE TABLE TrainData (id int, colors varchar(255), web_entities varchar(255), broad category varchar(255))')
# conn.commit()

# c.execute('SELECT MAX(id) FROM TrainData')
# recent_primary_key = c.fetchone()
# if recent_primary_key[0] is None:
#     recent_primary_key = 1
# else:
#     recent_primary_key = recent_primary_key[0]

recent_primary_key = 0
for number in range(len(description_list)):
    recent_primary_key += 1
    c.execute("INSERT INTO TrainData VALUES (?, ?, ?, ?)",
              (recent_primary_key, str(big_list[number]), description_list[number], None))
    conn.commit()
#
# c.execute('SELECT MAX(id) FROM TrainData')
# recent_primary_key = c.fetchone()
# if recent_primary_key[0] is None:
#     recent_primary_key = 1
# else:
#     recent_primary_key = recent_primary_key[0]
#
#
# for number in range(len(big_list)):
#     recent_primary_key += 1
#     med_li = str(big_list[number])
#     c.execute("INSERT INTO TrainData (id, colors)",
#               (recent_primary_key, med_li))
#     conn.commit()


