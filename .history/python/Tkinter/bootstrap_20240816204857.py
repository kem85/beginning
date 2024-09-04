import ttkbootstrap as ttk

# traditional approach
root = ttk.Tk()
style = ttk.Style("darkly")

# new approach
root = ttk.Window(themename="darkly")