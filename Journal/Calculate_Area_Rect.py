class calculateAreaRect:
    def __init__(self, length, width):
        self.length = length  # public attribute
        self.width = width
        self._area = 0.0  # non-public attribute

    def _calculateArea(self):  # non-public method
        self._area = self.length * self.width

    def getArea(self):  # public method
        self._calculateArea()  # call the _calcualateArea method
        return self._area  # returns the area of the rectangle


