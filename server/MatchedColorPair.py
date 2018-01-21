# Input - Dataset, list of lists in the format [[1st color, second color], [third color, fourth color]], [[match]]

# Weightings for each match

class MatchedPair:
    """ Pair of matched colours"""

    def __init__(self, color_one, color_two):
        """
        Initialize a matched color pair.

        :param color_one: Color
        :param color_two: Color
        """
        self.color_one, self.color_two, self.weight = color_one, color_two, 1

    def __str__(self):
        return str(self.color_one) + " | " + str(self.color_two)

    def __eq__(self, other):
        return ((self.color_one == other.color_one and self.color_two == other.color_two) or
                (self.color_one == other.color_two and self.color_two == other.color_one))

    def find_weight(self, total_matches):
        """

        Return weight of this matched pair within total data_set.

        :return: None
        """
        self.weight = total_matches.count(self) / len(total_matches)
