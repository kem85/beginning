import ttkbootstrap as ttk

# traditional approach
root = ttk.tk()
style = ttk.Style("darkly")

# new approach
root = ttk.Window(themename="darkly")