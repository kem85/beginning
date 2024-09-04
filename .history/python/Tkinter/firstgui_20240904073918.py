import tkinter as tk
from tkinter import ttk

class ScrollableButtonsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scrollable Buttons Example")
        self.geometry("300x400")

        # Create a canvas and a vertical scrollbar for it
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create a frame inside the canvas which will contain the buttons
        self.buttons_frame = ttk.Frame(self.canvas)
        
        # Ensure the frame is anchored to the top-left corner
        self.canvas.create_window((0, 0), window=self.buttons_frame, anchor="nw")

        # Bind the frame's size to update the scroll region
        self.buttons_frame.bind("<Configure>", self.on_frame_configure)

        # Example: Create buttons (change the range to test)
        self.create_buttons(10)  # Start with 10 buttons

    def on_frame_configure(self, event):
        """Reset the scroll region to encompass the inner frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def create_buttons(self, num_buttons):
        """Create a specified number of buttons in the scrollable frame"""
        # Clear existing buttons
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

        # Create new buttons
        for i in range(1, num_buttons + 1):
            btn = ttk.Button(self.buttons_frame, text=f"Button {i}")
            btn.pack(fill='x', padx=5, pady=2)

        # After adding buttons, reset the view to the top
        self.canvas.yview_moveto(0)

if __name__ == "__main__":
    app = ScrollableButtonsApp()
    app.mainloop()
