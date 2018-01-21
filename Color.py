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
        return self.r, self.g, self.b
