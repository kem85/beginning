import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *
from tkinter import *
root = Tk()
windowWidth = 700
windowHeight = 500
screenWidth = root.winfo_screenwidth()   # Current monitor is 1920
screenHeight = root.winfo_screenheight() # x 1080

# find the center point
centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)

# set the position of the window to the center of the screen
root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
root.mainloop()