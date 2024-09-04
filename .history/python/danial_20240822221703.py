import Tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.toolbar = tk.Frame(self, borderwidth=1, relief="raised")
        self.labels = tk.Frame(self, borderwidth=1, relief="raised")
        self.text = tk.Text(self, width=80, height=20)

        self.toolbar.pack(side="top", fill="x")
        self.labels.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)

        for i in range(5):
            button = tk.Button(self.toolbar, text="Button %d" %i)
            button.pack(side="left")


        for i in range(5):
            label = tk.Label(self.labels, text="Label %d" %i)
            label.pack(side="top", fill="x", padx=8)

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()