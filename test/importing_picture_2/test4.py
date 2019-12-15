import tkinter as tk
from objects.class_Player import Player
from PIL import Image, ImageTk

# make window
root = tk.Tk()
root.title('The Mega Yakut Game')
root.geometry('800x600')
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)
player1 = Player(canvas, 300, 300, 100, 100)
# image = ImageTk.PhotoImage(Image.open("importtest.png"))
# canvas.create_image(400, 400, image=image)
root.mainloop()
