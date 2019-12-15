"""This class will operate in level coordinate system (x, y), point (0,0) on the left top side of the level"""
from ai.class_Simple import Simple
from PIL import Image


class Dog(Simple):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.sprite = Image.open("graphics/sprites/dog_sprites/dog_static_left.png")
        self.player_in_touch = False
        self.direction = "left"

    def set_sprite(self):
        """This method changes dog animation depending on the direction of movement """

        if self.live:

            # 1) This shows the running sprite
            if not self.on_platform:
                if self.vx > 0:
                    self.direction = "right"
                    self.sprite = Image.open("graphics/sprites/dog_sprites/dog_running_right.png")
                elif self.vx < 0:
                    self.direction = "left"
                    self.sprite = Image.open("graphics/sprites/dog_sprites/dog_running_left.png")

            # 2) This shows attacking sprite
            if self.player_in_touch:
                if self.vx > 0:
                    self.sprite = Image.open("graphics/sprites/dog_sprites/dog_attacking_right.png")
                elif self.vx < 0:
                    self.sprite = Image.open("graphics/sprites/dog_sprites/dog_attacking_left.png")
