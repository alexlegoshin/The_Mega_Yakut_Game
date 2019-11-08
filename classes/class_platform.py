# importing necessary modules


# class body
class platform():

    def __init__(self, canv):
        """
        Target class constructor
        """
        self.canv = canv
        self.live = 1
        self.id = self.canv.create_line(0, 0, 0, 0)