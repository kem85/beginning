import tkinter as tk
from tkinter import messagebox
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\n")
        time.sleep(1)
        t -= 1
    print('Lift off!')

def start_countdown():
    try:
        t = int(entry.get())
        countdown(t)
        messagebox.showinfo("Countdown", "Lift off!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

root = tk.Tk()
root.title("Countdown Timer")

entry_label = tk.Label(root, text="Enter the time in seconds:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Start Countdown", command=start_countdown)
start_button.pack()

root.mainloop()