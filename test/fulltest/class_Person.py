# importing necessary modules


# class body
class Person:

    def __init__(self, canv, x, y, height, width):
        """
        Person class constructor
        """
        self.canvas = canv
        self.live = 1
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.id = self.canvas.create_rectangle(x, y, x + width, y + height, fill="Green")

    def move(self, velocity):
        if velocity < 0:
            self.canvas.move(self.id, velocity, 0)
