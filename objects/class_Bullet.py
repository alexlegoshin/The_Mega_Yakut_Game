""" This dog does not die!"""

from classes.class_Organism import Organism
from physics.physics import gravity


class Bullet:

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.on_place = False
        self.on_platform = False
        self.push_on_platform = False  # True if we need to push player clearly on platform if he will go into it
        self.push_under_platform = False
        self.counter = 0  # counter to understand if bot has jumped from platform
        self.live = 100

    def move(self):
        if self.on_platform:
            self.on_place = True
            self.counter += 1
        if not self.on_place and (self.counter % 2 == 0):
            self.vy = gravity(self.vy, self.on_platform)
        elif not self.on_platform and (self.counter % 2 != 0):
            self.vy = -10
            self.on_place = False
            self.counter += 1
        self.x += self.vx
        self.y += self.vy
        self.live -= 1

