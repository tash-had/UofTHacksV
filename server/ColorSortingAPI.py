import math
from server.Clothing import Clothing
from server.Color import Color
import pickle
from server.MatchedColorPair import MatchedPair

def distinct_matched_pairs_to_weights(distinct_matched_pairs):
    l = []
    for item in distinct_matched_pairs:
        l.append(item.weight)
    return l


# FEED THIS FUNCTION A SHIRT COLOUR
def get_corresponding_color(color_to_match, distinct_matched_pairs):
    weights = distinct_matched_pairs_to_weights(distinct_matched_pairs)
    color_weight_indices = []
    for ind in range(len(distinct_matched_pairs)):
        if distinct_matched_pairs[ind].color_one == color_to_match or \
                        distinct_matched_pairs[ind].color_two == color_to_match:
            color_weight_indices.append(ind)
    color_weights = []
    for ind in color_weight_indices:
        color_weights.append(weights[ind])
    max_weight = max(color_weights)
    max_index = -1
    for ind in range(len(color_weights)):
        if color_weights[ind] == max_weight:
            max_index = ind
            break
    max_pair = distinct_matched_pairs[max_index]
    if max_pair.color_one == color_to_match:
        return max_pair.color_two
    else:
        return max_pair.color_one


def find_corresponding_clothing(list_of_clothes, color_to_match):
    euclidian_distances = []

    for clothing in list_of_clothes:
        distance = math.sqrt((clothing.color.r - color_to_match.r)**2 + (clothing.color.g - color_to_match.g)**2
                             + (clothing.color.b - color_to_match.b)**2)
        euclidian_distances.append(distance)
    min_distance = min(euclidian_distances)
    for ind in range(len(euclidian_distances)):
        if euclidian_distances[ind] == min_distance:
            return list_of_clothes[ind]

if __name__ == "__main__":

    pickle_in = open("server/total_matched_pairs.bin", "rb")
    shirt = Clothing(Color(0, 32, 32), "shirt", 14)
    total_matched_pairs = pickle.load(pickle_in)
    print(total_matched_pairs)