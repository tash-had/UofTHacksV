"""
Library to modify colors.
"""


class Color:
    """
    A color class that has a name attribute, and an associated RGB value."
    """

    def __init__(self, r, g, b):
        """
        Initialize a Color object.

        :param r: int
        :param g: int
        :param b: int
        """
        self.r, self.g, self.b = r, g, b

    def __str__(self):
        """
        Return a string method.

        :return: String
        """
        return str(self.r) + ' ' + str(self.g) + ' ' + str(self.b)

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b
