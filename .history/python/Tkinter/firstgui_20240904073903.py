import tkinter as tk
import ttkbootstrap as ttk

def create_buttons(canvas, frame, count):
    for i in range(count):
        button = ttk.Button(frame, text=f"Button {i}")
        button.grid(row=i//2, column=i%2, padx=5, pady=5)
    # Update scroll region to include all widgets
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def main():
    root = ttk.Window(themename="darkly")
    root.geometry("300x400")

    canvas = tk.Canvas(root, bg="purple")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    create_buttons(canvas, frame, 10)  # Adjust the number of buttons as needed

    root.mainloop()

if __name__ == "__main__":
    main()
