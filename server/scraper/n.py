import io
import os
from google.cloud import vision
from google.cloud.vision import types


## User Side

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/tash-had/AndroidStudioProjects/UofTHacksV/scraper/uoft-hack-786661112645.json"


def detect_properties(path):

    print("hey2");
    """Detects image properties in the file."""
    client = vision.ImageAnnotatorClient()
    print("hey3")

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    color = props.dominant_colors.colors[0]
    return color

    # for color in props.dominant_colors.colors[:3]:
    #     rgb = color.color.red + color.color.green + color.color.blue
    #     if rgb >= 720 and color.score > 0.75:  # all white piece of clothing
    #         color_pairs.append([[]])
    #
    #
    #     elif rgb >= 720 and 0.60 <= color.score <= 0.75:  # identifying 1 white piece of clothing
    #         color_pairs.append([[props.dominant_colors.colors[0].color.red,
    #                              props.dominant_colors.colors[0].color.green,
    #                              props.dominant_colors.colors[0].color.blue],
    #                             [props.dominant_colors.colors[1].color.red,
    #                              props.dominant_colors.colors[1].color.green,
    #                              props.dominant_colors.colors[1].color.blue]])
    #
    #     elif rgb >= 720 and color.score < 0.60:
    #         if color == props.dominant_colors.colors[0]:
    #             color_pairs.append([[props.dominant_colors.colors[1].color.red,
    #                              props.dominant_colors.colors[1].color.green,
    #                              props.dominant_colors.colors[1].color.blue],
    #                             [props.dominant_colors.colors[2].color.red,
    #                              props.dominant_colors.colors[2].color.green,
    #                              props.dominant_colors.colors[2].color.blue]
    #                             ])
    #         elif color == props.dominant_colors.colors[1]:
    #             color_pairs.append([[props.dominant_colors.colors[0].color.red,
    #                                  props.dominant_colors.colors[0].color.green,
    #                                  props.dominant_colors.colors[0].color.blue],
    #                                 [props.dominant_colors.colors[2].color.red,
    #                                  props.dominant_colors.colors[2].color.green,
    #                                  props.dominant_colors.colors[2].color.blue]
    #                                 ])
    #         elif color == props.dominant_colors.colors[2]:
    #             color_pairs.append([[props.dominant_colors.colors[0].color.red,
    #                                  props.dominant_colors.colors[0].color.green,
    #                                  props.dominant_colors.colors[0].color.blue],
    #                                 [props.dominant_colors.colors[1].color.red,
    #                                  props.dominant_colors.colors[1].color.green,
    #                                  props.dominant_colors.colors[1].color.blue]
    #                                 ])


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

