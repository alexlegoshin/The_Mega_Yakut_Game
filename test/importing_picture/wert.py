from tkinter import *
import tkinter as tk
from random import randrange as rnd, choice, uniform
import time
import socket
import os
from PIL import Image, ImageTk
from time import sleep

root = Tk()
root.title("Outer Space Flyer")
root.geometry("900x500")

canv = Canvas(root, bg='black')
canv.pack(fill=BOTH, expand=1)

n = 1
score = 0

times = 0
gamespeed = 25

# РџР»Р°РЅРµС‚РєРё
# Р›РёСЃС‚С‹ СЃ РЅРѕРјРµСЂР°РјРё РѕР±СЉРµРєС‚РѕРІ; СЃ РёС… СЂР°РґРёСѓСЃР°РјРё; РєРѕРѕСЂРґРёРЅР°С‚Р°РјРё РїРѕ Ox; РїРѕ Oy; СЃ РїРѕР·РёС†РёСЏРјРё РѕР±СЉРµРєС‚РѕРІ; СЃ РёС… С†РІРµС‚Р°РјРё
plutons = []
rad = []
xplut = []
yplut = []
posplut = []
colorplut = []


def planetadd():

    global plutons, rad
    global xplut, yplut, posplut, colorplut
    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    rd = 100
    y = -100
    minnum = 0

    # Р•СЃР»Рё РѕР±СЉРµРєС‚РѕРІ РјРµРЅСЊС€Рµ РґРµСЃСЏС‚Рё
    if len(rad) < 10:
        momental1 = rnd(1, 4)
        posplut.append(momental1)
        x = momental1 * 240
        rad.append(rd)
        xplut.append(x)
        yplut.append(y)
        momental2 = choice(colors)
        colorplut.append(momental2)
        plutons.append(canv.create_oval(x - rd, y, x, y + rd, fill=momental2, width=0, tags=minnum))

    # Р•СЃР»Рё РѕР±СЉРµРєС‚РѕРІ 10 РёР»Рё Р±РѕР»РµРµ
    else:

        for minnum in range(len(rad)):
            if rad[minnum] == 0:
                break
        if rad[minnum] == 0:
            posplut[minnum] = rnd(1, 4)
            x = posplut[minnum] * 240
            rad[minnum] = rd
            xplut[minnum] = x
            yplut[minnum] = y
            colorplut[minnum] = choice(colors)
            plutons[minnum] = canv.create_oval(x - rd, y, x, y + rd, fill=colorplut[minnum], width=0, tags=minnum)

def planetgrowth(pnum):
    # pnum - РЅРѕРјРµСЂ РѕР±СЉРµРєС‚Р°, РєРѕС‚РѕСЂС‹Р№ РґРѕР»Р¶РµРЅ СѓРІРµР»РёС‡РёС‚СЊСЃСЏ

    global plutons, rad
    global xplut, yplut, posplut, colorplut

    # Р•СЃР»Рё РѕР±СЉРµРєС‚ РЅР° СЌРєСЂР°РЅРµ
    if yplut[pnum] < 800:
        canv.delete(plutons[pnum])
        rad[pnum] += 5
        xplut[pnum] += 2.5
        if posplut[pnum] == 1:
            xplut[pnum] -= 2
        elif posplut[pnum] == 3:
            xplut[pnum] += 2
        yplut[pnum] += 15
        plutons[pnum] = canv.create_oval(xplut[pnum] - rad[pnum], yplut[pnum], xplut[pnum],
                                         yplut[pnum] + rad[pnum], fill=colorplut[pnum], width=0, tags=pnum)

    # Р•СЃР»Рё РѕР±СЉРµРєС‚ СѓР»РµС‚РµР» Р·Р° РїСЂРµРґРµР»С‹ СЌРєСЂР°РЅР°
    else:
        canv.delete(plutons[pnum])
        rad[pnum] = 0

def movinginfront():
    global gamespeed
    gamespeed -= 0.0025
    for i in range(len(rad)):
        planetgrowth(i)

def game():
    global times, gamespeed
    movinginfront()
    if times == round(gamespeed):
        times = 0
        planetadd()
    times += 1
    root.after(100, game)

def leftclick(event):
    game()

def rightclick(event):
    movinginfront()

def main_menu():
    global button_new_game, button_exit, difficulty
    difficulty = 0
    button_new_game = Button(canv, text="New game", width=15, height=3, command=new_game)
    button_new_game.pack()
    button_exit = Button(canv, text="Exit", width=15, height=3, command=exit)
    button_exit.pack()

canv.bind('<Button-1>', leftclick)
canv.bind('<Return>', rightclick)

def func(event = None):
    run = app()

def app():
    img = Image.open("spaceshipmain.png")
    render = ImageTk.PhotoImage(img)
    initil = Label(root, image = render)
    initil.image = render
    x_ = 10
    y_ = 10
    '''while x_ < 100:
        initil.config(image = '')
        initil.place(x = x_, y = y_)
        initil = Label(root, image = render)
        initil.image = render
        x_ += 5
        y_ += 5'''
    initil.place(x = x_, y = y_)
    
    

root.bind('a',func)
mainloop()