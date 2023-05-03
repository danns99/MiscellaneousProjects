import tkinter as tk
from typing import List
import random
import time

global LBL_TIME
global BTN_TARGET
global FRM_GAME
global LBL_POINTS
global LBL_SCORE
global BTN_RESET
global BTN_START

def introduction():
    global BTN_START
    global INTRO_FRAME

    INTRO_FRAME = tk.Frame(master=window)
    INTRO_FRAME.pack(fill=tk.BOTH, expand=True)

    BTN_START = tk.Button(master=INTRO_FRAME,text='Start',command=game_layout, height=2,width=10)
    BTN_START.place(x=280,y=300)

def game_layout():
    global LBL_POINTS
    global LBL_TIME
    global FRM_GAME
    global BTN_TARGET
    global FRM_INFO

    # Get rid of intro
    INTRO_FRAME.pack_forget()    
    BTN_START.pack_forget()

    # Display points and time
    FRM_INFO = tk.Frame(master=window,padx=10,pady=10)
    LBL_POINTS = tk.Label(master=FRM_INFO,text=0)
    LBL_TIME = tk.Label(master=FRM_INFO, text=10)

    FRM_INFO.pack(fill=tk.BOTH, side=tk.TOP)
    LBL_POINTS.pack(side=tk.LEFT)
    LBL_TIME.pack(side=tk.RIGHT)

    # Game
    FRM_GAME = tk.Frame(master=window, height=550, width=550, relief=tk.SUNKEN, borderwidth=4)
    BTN_TARGET = tk.Button(
        master=FRM_GAME,
        height=5,
        width=5,
        borderwidth=0,
        command=lambda: btn_position(),
        bg="black"
    )

    FRM_GAME.pack()
    BTN_TARGET.place(x=230, y=230)
    
    timer()

def btn_position():
    x_axis=random.randint(0,500)
    y_axis=random.randint(0,500)
    LBL_POINTS['text'] += 1
    BTN_TARGET.place(x=x_axis,y=y_axis)


def timer():
    global LBL_TIME
    global BTN_TARGET
    global FRM_GAME
    global LBL_POINTS
    global LBL_SCORE
    global BTN_RESET

    LBL_TIME['text'] -= 1

    if LBL_TIME['text'] == 0:
        BTN_TARGET.place_forget()

        LBL_SCORE = tk.Label(master=FRM_GAME, text=f"Your score was: {LBL_POINTS['text']}", font=("Arial", 20))
        LBL_SCORE.place(x=150, y=170)

        BTN_RESET = tk.Button(master=FRM_GAME, text="Try Again", command=reset, width=10)
        BTN_RESET.place(x=230, y=220)
        return 0

    LBL_TIME.after(1000, timer)

def reset():
    global LBL_SCORE
    global BTN_RESET
    global FRM_INFO
    global FRM_GAME

    LBL_SCORE.pack_forget()
    BTN_RESET.pack_forget()
    FRM_INFO.pack_forget()
    FRM_GAME.pack_forget()

window = tk.Tk()
window.title("Target Practice Game")
window.geometry("560x600")

introduction()

window.mainloop()