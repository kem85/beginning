import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# traditional approach
root = ttk.tk()
style = ttk.Style("darkly")

# new approach
root = ttk.Window(themename="darkly")