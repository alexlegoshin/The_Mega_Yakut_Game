class Platform:

    def __init__(self, x, y, width, height):
        """
        Platform class constructor
        Args:
            (x, y) - coordinates of the top left point of the rectangle in which the model is enclosed
            length, width - length and width of this rectangle
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
