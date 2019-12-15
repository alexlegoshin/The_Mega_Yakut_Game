import tkinter as tk
from classes.class_GameApp import GameApp
from sys import exit

# make constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
NUMBER_OF_LEVELS = 2

# make window
root = tk.Tk()
root.title('The Mega Yakut Game')
root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)
canvas.update()

app = GameApp(NUMBER_OF_LEVELS, root, canvas)


def new_game():
    button_new_game.destroy()
    button_load_game.destroy()
    button_exit.destroy()
    save_file = open("saves/save.txt", 'r+')
    save_file.truncate(0)  # Clear save file
    save_file.write('1')
    save_file.close()
    app.new_level_game()


def load_game():
    button_new_game.destroy()
    button_load_game.destroy()
    button_exit.destroy()
    app.load_game()


def exit_from_game():
    exit(0)


button_new_game = tk.Button(canvas, text="New game", width=15, height=3, command=new_game)
button_new_game.pack()
button_load_game = tk.Button(canvas, text="Continue game", width=15, height=3, command=load_game)
button_load_game.pack()
button_exit = tk.Button(canvas, text="Exit", width=15, height=3, command=exit_from_game)
button_exit.pack()

root.mainloop()
