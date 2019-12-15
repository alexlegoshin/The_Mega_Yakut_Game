"""This class is responsible for the bot actions"""
from classes.class_Organism import Organism
from physics.physics import gravity


class Simple(Organism):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.on_place = False
        self.on_platform = False
        self.push_on_platform = False  # True if we need to push player clearly on platform if he will go into it
        self.push_under_platform = False

    def move(self):
        if self.on_platform:
            self.on_place = True
        if not self.on_platform and self.on_place:
            self.vx = - self.vx
        if not self.on_place:
            self.vy = gravity(self.vy, self.on_platform)
        self.x += self.vx
        self.y += self.vy
