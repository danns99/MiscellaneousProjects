import tkinter as tk
from typing import List
import random
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from plotGraph import plotGraph

global LBL_TIME
global BTN_TARGET
global FRM_GAME
global LBL_POINTS
global LBL_SCORE
global LBL_ACCURACY
global BTN_RESET
global BTN_START
global NUMBER_OF_CLICKS
global RESULTS_PLOT
global INTRO_FRAME
global FRM_INFO

def introduction():
    global BTN_START
    global INTRO_FRAME

    INTRO_FRAME = tk.Frame(master=window,background="white")
    INTRO_FRAME.pack(fill=tk.BOTH, expand=True)

    BTN_START = tk.Button(master=INTRO_FRAME,text='Start',command=game_layout, height=2,width=10)
    BTN_START.place(x=280,y=300)

def game_layout():
    global LBL_POINTS
    global LBL_TIME
    global FRM_GAME
    global BTN_TARGET
    global FRM_INFO
    global INTRO_FRAME

    # Get rid of intro
    INTRO_FRAME.pack_forget()
    INTRO_FRAME.destroy() 
    BTN_START.pack_forget()

    # Display points and time
    FRM_INFO = tk.Frame(master=window,padx=10,pady=10,background="white")
    LBL_POINTS = tk.Label(master=FRM_INFO,text=0,background="white")
    LBL_TIME = tk.Label(master=FRM_INFO, text=10,background="white")

    FRM_INFO.pack(fill=tk.BOTH, side=tk.TOP)
    LBL_POINTS.pack(side=tk.LEFT)
    LBL_TIME.pack(side=tk.RIGHT)

    # Game
    FRM_GAME = tk.Frame(master=window, height=550, width=550, borderwidth=4,background="white")
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
    global LBL_ACCURACY
    global BTN_RESET
    global NUMBER_OF_CLICKS
    global RESULTS_PLOT

    LBL_TIME['text'] -= 1

    if LBL_TIME['text'] == 0:

        BTN_TARGET.place_forget()

        accuracy = round(int(LBL_POINTS['text']) * 100 / NUMBER_OF_CLICKS)

        LBL_SCORE = tk.Label(master=FRM_GAME, text=f"Your score was: {LBL_POINTS['text']}", font=("Arial", 20),background="white")
        LBL_SCORE.pack(side=tk.TOP, pady=6)

        LBL_ACCURACY = tk.Label(master=FRM_GAME, text=f"Your accuracy was: {accuracy}%", font=("Arial", 20),background="white")
        LBL_ACCURACY.pack(side=tk.TOP, pady=6)

        BTN_RESET = tk.Button(master=FRM_GAME, text="Try Again", command=reset, width=10)
        BTN_RESET.pack(side=tk.TOP, pady=6)

        saveScores(int(LBL_POINTS['text']), accuracy)

        fig = plotGraph()
        RESULTS_PLOT = FigureCanvasTkAgg(fig, master=FRM_GAME)
        RESULTS_PLOT.get_tk_widget().pack(pady=15)

        return 0

    LBL_TIME.after(1000, timer)

def reset():
    global LBL_SCORE
    global BTN_RESET
    global FRM_INFO
    global FRM_GAME
    global NUMBER_OF_CLICKS
    global RESULTS_PLOT

    LBL_SCORE.pack_forget()
    BTN_RESET.pack_forget()
    FRM_INFO.pack_forget()
    FRM_GAME.pack_forget()
    RESULTS_PLOT.get_tk_widget().pack_forget()

    game_layout()

    NUMBER_OF_CLICKS = 0

def onClick(event):
    global NUMBER_OF_CLICKS

    NUMBER_OF_CLICKS += 1

def saveScores(numberOfPoints, accuracy):
    textToFile = str(numberOfPoints) + " " + str(accuracy) + "\n"
    
    with open('results.dat', 'a') as f:
        f.write(textToFile)
        f.close()

# Initialise tkinter window
window = tk.Tk()
window.configure(background="white")

# Initialise click counter
NUMBER_OF_CLICKS = 0

# Bind click counter to window
window.bind("<Button-1>", onClick)

# If a results file does not exist, create one
file = open('results.dat', 'a+')
file.close()

# Set window size and geometry
window.title("Target Practice Game")
window.geometry("560x600")

# Display introduction frame
introduction()

# Define functionality of window close button
def disable_event():
   window.quit()
   window.destroy()

window.protocol("WM_DELETE_WINDOW", disable_event)

# Commence main program
window.mainloop()