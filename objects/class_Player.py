"""This class will operate with coordinate system (x, y), point (0,0) on the left top side of the level

"""

from PIL import Image
from physics.physics import gravity, x_resistance
from classes.class_Organism import Organism


# class body
class Player(Organism):
    def __init__(self, x, y, width, height):
        """
            PLayer class constructor
            Args:
                (x, y) - coordinates of the top left point of the rectangle in which the model is enclosed
                height, width - height and width of this rectangle
        """
        super().__init__(x, y, width, height)
        self.vx = 0
        self.sprite = Image.open("graphics/sprites/player_sprites/player_static_right.png")
        self.direction = "right"
        self.delay = 0
        self.on_platform = False
        self.push_on_platform = False  # True if we need to push player clearly on platform if he will go into it
        self.push_under_platform = False
        self.push_x = False

    def move(self):
        if not self.live:
            self.vx = x_resistance(self.vx)
            self.vy = gravity(self.vy, False)
        else:
            if not self.push_on_platform:
                self.vy = gravity(self.vy, self.on_platform)
        self.x += self.vx
        self.y += self.vy

    def move_left(self):
        if self.live:
            self.vx = -5

    def move_right(self):
        if self.live:
            self.vx = 5

    def jump(self):
        if self.live:
            self.on_platform = False
            self.vy = -10

    def set_sprite(self):
        """This method changes the player's animation depending on the direction of movement """

        if self.live:

            # 1) This makes the 3-part linear running animation (4) cycled
            if self.vx == 0 or self.delay >= 3:
                self.delay = 0

            # 2) This makes the player static after run stopping
            if self.on_platform and self.vx == 0:
                if self.direction == "right":
                    self.sprite = Image.open("graphics/sprites/player_sprites/player_static_right.png")
                else:
                    self.sprite = Image.open("graphics/sprites/player_sprites/player_static_left.png")

            # 3) This makes the player flying when jumping
            if not self.on_platform:
                if self.vx > 0:
                    self.direction = "right"
                    self.sprite = Image.open("graphics/sprites/player_sprites/player_running_right_2.png")
                elif self.vx < 0:
                    self.direction = "left"
                    self.sprite = Image.open("graphics/sprites/player_sprites/player_running_left_2.png")

            # 4) This is a full 3-part running animation
            if self.on_platform and self.vx != 0:
                if self.vx > 0:
                    self.direction = "right"
                    if self.delay <= 1:
                        self.sprite = Image.open("graphics/sprites/player_sprites/player_static_right.png")
                    elif 1 < self.delay < 2:
                        self.sprite = Image.open("graphics/sprites/player_sprites/player_running_right_1.png")
                    else:
                        self.sprite = Image.open("graphics/sprites/player_sprites/player_running_right_2.png")
                else:
                    self.direction = "left"
                    if self.delay <= 1:
                        self.sprite = Image.open("graphics/sprites/player_sprites/player_static_left.png")
                    elif 1 < self.delay < 2:
                        self.sprite = Image.open("graphics/sprites/player_sprites/player_running_left_1.png")
                    else:
                        self.sprite = Image.open("graphics/sprites/player_sprites/player_running_left_2.png")
                self.delay += 0.2

        # 5) This makes the player falling after death
        else:
            if self.direction == "right":
                self.sprite = Image.open("graphics/sprites/player_sprites/player_running_right_2.png")
            else:
                self.sprite = Image.open("graphics/sprites/player_sprites/player_running_left_2.png")
