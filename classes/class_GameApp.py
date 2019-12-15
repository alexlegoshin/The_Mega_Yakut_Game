"""This class is responsible for move from one level to new one and start it"""

from classes.class_Level import Level
import load_level as load
from tkinter import ALL, Button
from sys import platform, exit
from time import clock


class GameApp:

    def __init__(self, number_of_levels, root, canvas):
        self.number_of_levels = number_of_levels
        self.root = root
        self.canvas = canvas
        self.number_of_current_level = 1
        self.current_level = ''
        self.pause_status = False
        self.button_resume = ''
        self.button_exit = ''
        if platform == "win32" or platform == "cygwin":
            self.key_left = 37
            self.key_right = 39
            self.key_up = 38
            self.key_space = 32
        elif platform == "linux" or platform == "linux2" or platform == "linux3":
            self.key_left = 113
            self.key_right = 114
            self.key_up = 111
            self.key_space = 65
        elif platform == "darwin":
            self.key_left = 113
            self.key_right = 114
            self.key_up = 111
            self.key_space = 65
        clock()  # For Windows, because there clock() returns time since first time when this function is called

    def new_level_game(self):
        """This method will start new level"""
        self.canvas.delete(ALL)
        parameters = load.load_level(self.number_of_current_level)  # Argument - number of the level
        self.current_level = Level(self.canvas, parameters[0], parameters[1],
                                   parameters[2], parameters[3], parameters[4])
        self.start_game()

    def bind_all(self):
        self.root.bind("<KeyPress>", self.key_interpreter)
        self.root.bind("<KeyRelease>", self.key_release)

    def key_interpreter(self, event):
        if not self.pause_status:
            if event.keycode == self.key_right:
                self.current_level.player.move_right()
            if event.keycode == self.key_left:
                self.current_level.player.move_left()
            if event.keycode == self.key_up and self.current_level.player.on_platform:
                self.current_level.player.jump()
        if event.keycode == self.key_space:
            self.pause()

    def key_release(self, event):
        if event.keycode == 39 or event.keycode == 37:
            self.current_level.player.vx = 0

    def game_tic(self):
        """This is main method of each game"""
        time1 = clock()  # Time before game iteration (before all logical operations)
        if not self.pause_status:
            self.current_level.game()
        player_live = self.current_level.check_for_live()
        time2 = clock()  # Time after game iteration (after all logical operations)
        time = int(24 - (time2 - time1) * 1000)  # This iteration time
        if not self.current_level.end_level and player_live:
            self.root.after(time, self.game_tic)
        elif self.current_level.end_level:
            self.new_level()
        else:
            self.new_level_game()

    def start_game(self):
        self.bind_all()
        self.game_tic()

    def new_level(self):
        """This method will increase number of current level if player finish previous one"""
        if self.number_of_current_level < self.number_of_levels:
            self.number_of_current_level += 1
        save_file = open("saves/save.txt", 'r+')
        save_file.truncate(0)  # Clear save file
        save_file.write(str(self.number_of_current_level))
        save_file.close()
        self.root.after(10000, self.new_level_game)

    def load_game(self):
        save_file = open("saves/save.txt", 'r+')
        self.number_of_current_level = int(save_file.read())
        save_file.close()
        self.new_level_game()

    def save_exit(self):
        exit(0)

    def pause(self):
        if not self.pause_status:
            self.pause_status = True
            self.button_resume = Button(self.canvas, text="Resume", width=15, height=3, command=self.pause)
            self.button_resume.pack()
            self.button_exit = Button(self.canvas, text="Save and exit", width=15, height=3, command=self.save_exit)
            self.button_exit.pack()

        else:
            self.pause_status = False
            self.button_resume.destroy()
            self.button_exit.destroy()
