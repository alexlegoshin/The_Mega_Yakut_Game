"""This class defines static bot's actions"""
from classes.class_Organism import Organism
from objects.class_Player import Player


class Primitive(Organism):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.on_place = False
        self.on_platform = False
        self.push_on_platform = False  # True if we need to push player clearly on platform if he will go into it
        self.push_under_platform = False
        self.shoot_range = 75

    def shoot(self):
        """Shoot if player is in shoot range higher than bot, but there is no limit for number of bullet
         but there is no limit for number of bullets. Actually it doesn't shoot, to shoot create Dog(Bullet) class"""
        if (self.x - Player.x <= self.shoot_range) and (Player.y - self.y >= 0):
            pass
