from Color import Color
import numpy


basic_color_list = [(0, 0, 0), (0, 0, 127.5), (0, 0, 255), (0, 127.5, 0), (0, 127.5, 127.5), (0, 127.5, 255),
                    (0, 255, 0), (0, 255, 127.5), (0, 255, 255), (127.5, 0, 0), (127.5, 0, 127.5), (127.5, 0, 255),
                    (127.5, 127.5, 0), (127.5, 127.5, 127.5), (127.5, 127.5, 255), (127.5, 255, 0),
                    (127.5, 255, 127.5), (127.5, 255, 255), (255, 0, 0), (255, 0, 127.5), (255, 0, 255),
                    (255, 127.5, 0), (255, 127.5, 127.5), (255, 127.5, 255), (255, 255, 0), (255, 255, 127.5),
                    (255, 255, 255)]


def get_general_color(r, g, b):
    """
    Find the closest general color to the given Color object.

    :param r: int
    :param g: int
    :param b: int
    :return: Color object
    """

    for color in basic_color_list:
        print(numpy.sqrt((r - color[0]) ** 2 + (g - color[1]) ** 2 +
                         (b - color[2]) ** 2), color)
        if (numpy.sqrt((r - color[0]) ** 2 + (g - color[1]) ** 2 +
                         (b - color[2]) ** 2) <= 60):
            return Color(color[0], color[1], color[2])

    for color in basic_color_list:
        print(numpy.sqrt((r - color[0]) ** 2 + (g - color[1]) ** 2 +
                         (b - color[2]) ** 2), color)
        if (numpy.sqrt((r - color[0]) ** 2 + (g - color[1]) ** 2 +
                               (b - color[2]) ** 2) <= 111):
            return Color(color[0], color[1], color[2])

    return "Mans failed me fam"


