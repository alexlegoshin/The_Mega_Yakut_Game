# importing necessary modules
import tkinter as tk
from PIL import Image, ImageTk

# class body
class Player:

    def __init__(self, canvas, x, y, height, width):
        """
        Target class constructor
        """
        self.canvas = canvas
        self.live = 1
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        img = Image.open("importtest.png")
        render = ImageTk.PhotoImage(img)
        self.id = canvas.create_image(400, 400, image=render)
        self.id_ = render

    def move(self, velocity):
        if velocity < 0:
            self.canvas.move(self.id, velocity, 0)
