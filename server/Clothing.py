class Clothing:

    def __init__(self, color, type, id):
        """
        Iniitalize clothing object.

        :param color: Color
        :param type: str
        :param id: int
        """

        self.color, self.type, self.id = color, type, id

    def __str__(self):
        return str(self.type) + ", " + str(self.color)
