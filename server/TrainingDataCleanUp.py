import sqlite3
import pickle
from server.Color import Color
from server.MatchedColorPair import MatchedPair

conn = sqlite3.connect('/Users/Saivv/Documents/UofTHacksQuickDressed/UofTHacksV/server/scraper/db.scraper', check_same_thread=False)
c = conn.cursor()
c.execute('SELECT colors FROM TrainData')
y = c.fetchall()

new_data = []
total_matched_pairs = []
distinct_colors = []
distinct_matched_pairs = []
weights = []

for i in y[6:]:
    cleaned_once = i[0].replace('[', '')
    cleaned_twice = cleaned_once.replace(']', '')
    new_array = cleaned_twice.split(",")
    new_match = []
    almost_done = []
    for item in new_array:
        if item != '':
            new_match.append(float(item))
    if len(new_match) > 0:
        almost_done.append(tuple(new_match[0:3]))
        almost_done.append(tuple(new_match[3:]))
    if len(almost_done) > 0:
        new_data.append(almost_done)

for object1 in new_data:
    color1 = Color(object1[0][0], object1[0][1], object1[0][2])
    color2 = Color(object1[1][0], object1[1][1], object1[1][2])
    matched_pair = MatchedPair(color1, color2)
    total_matched_pairs.append(matched_pair)


for matched_pair in total_matched_pairs:
    if not(matched_pair.color_one in distinct_colors):
        distinct_colors.append(matched_pair.color_one)
    if not(matched_pair.color_two in distinct_colors):
        distinct_colors.append(matched_pair.color_two)
    if not( matched_pair in distinct_matched_pairs):
        distinct_matched_pairs.append(matched_pair)


for item in distinct_matched_pairs:
    item.find_weight(total_matched_pairs)


with open('server/total_distinct_pairs.bin', 'wb') as f:
    pickle.dump(distinct_matched_pairs, f)
with open('server/total_matched_pairs.bin', 'wb') as f:
    pickle.dump(total_matched_pairs, f)

