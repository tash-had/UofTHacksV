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
        # print(numpy.sqrt((r - color[0]) ** 2 + (g - color[1]) ** 2 +
        #                  (b - color[2]) ** 2), color)
        if (numpy.sqrt((r - color[0]) ** 2 + (g - color[1]) ** 2 +
                         (b - color[2]) ** 2) <= 60):
            return color[0], color[1], color[2]

    for color in basic_color_list:
        # print(numpy.sqrt((r - color[0]) ** 2 + (g - color[1]) ** 2 +
        #                  (b - color[2]) ** 2), color)
        if (numpy.sqrt((r - color[0]) ** 2 + (g - color[1]) ** 2 +
                               (b - color[2]) ** 2) <= 111):
            return color[0], color[1], color[2]

    return "Mans failed me fam"


import sqlite3
conn = sqlite3.connect('/Users/Rahul/Desktop/UofTHacksV/scraper/db.scraper', check_same_thread=False)
c = conn.cursor()
# c.execute('CREATE TABLE TrainData (id int, colors varchar(255), web_entities varchar(255), broad category varchar(255))')
# conn.commit()

description_list = [2,3,4,5,6]
big_list = [[[2,3,4,5,6], [2,3,4,5,6]], [[2,3,4,5,6], [2,3,4,5,6]], [[2,3,4,5,6], [2,3,4,5,6]], [[2,3,4,5,6], [2,3,4,5,6]], [[2,3,4,5,6], [2,3,4,5,6]],]

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
