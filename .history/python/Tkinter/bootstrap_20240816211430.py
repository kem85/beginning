import tkinter as tk
from tkinter import scrolledtext
 
class GUI(object):
     
    def __init__(self, root):
         
        self.root = root
        self.root.title('Sensors')
         
        windowWidth = 700
        windowHeight = 500
         
        # get the screen dimension
        screenWidth = root.winfo_screenwidth()   # Current monitor is 1920
        screenHeight = root.winfo_screenheight() # x 1080
 
        # find the center point
        centerX = int(screenWidth/2 - windowWidth / 2)
        centerY = int(screenHeight/2 - windowHeight / 2)
 
        # set the position of the window to the center of the screen
        root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
        root.resizable(False,False)
         
        ### On main menu
        self.sensors = tk.Button(root, text='Sensors',height=3, width=10, font=('Helvetica',15), borderwidth=5, command=self.Sensors)
        self.options = tk.Button(root, text='Options',height=3, width=10, font=('Helvetica',15), borderwidth=5, command=self.Options)
         
         
        ### In sensor menu
        self.addSensorBtn = tk.Button(root, text='Add Sensor')
        self.ReturnMenu = tk.Button(root, text="Return to Main Menu", font=('Helvetica'), command=self.MainMenu)
        
        self.frame = tk.Frame(root).grid(row=0,column=0)
        self.canvas = tk.Canvas(self.frame,bg='gray75')
        self.vsb = tk.Scrollbar(self.frame, orient='vertical', command=self.canvas.yview)
         
        self.MainMenu()
         
    def GridConfig(self):
        root.rowconfigure(0,weight=3)
        root.rowconfigure(1,weight=1)
        root.columnconfigure((0,2), weight=1)
         
    def MainMenu(self):
         self.GridConfig()
         self.RemoveAll()
         self.sensors.grid(column=0, row=1, sticky='NE')
         self.options.grid(column=2, row=1, sticky='NW')
          
    def Sensors(self) :
        self.RemoveAll()
         
        self.canvas.grid(column=0,row=0,columnspan=3,sticky='NEWS')
        self.vsb.grid(row=0, column=3, sticky='NSE')
        self.canvas.configure(yscrollcommand=self.vsb.set, scrollregion=self.canvas.bbox('all'))
         
        self.addSensorBtn.grid(column=2,row=1, sticky='NEWS')        
        self.ReturnMenu.grid(column=0, row=1,sticky='NEWS')
     
    def Options(self):
        self.RemoveAll()
        self.GridConfig()
        self.ReturnMenu.grid(column=1, row=1)
     
    def RemoveAll(self):
        self.vsb.grid_remove()
        self.canvas.grid_remove()
        self.addSensorBtn.grid_remove()
        self.sensors.grid_remove()
        self.options.grid_remove()
        self.ReturnMenu.grid_remove()
class ScrolledCanvas():
    def __init__(self, parent, color='brown'):
        canv = Canvas(parent, bg=color, relief=SUNKEN)
        canv.config(width=300, height=200)                
 
        ##---------- scrollregion has to be larger than canvas size
        ##           otherwise it just stays in the visible canvas
        canv.config(scrollregion=(0,0,300, 1000))         
        canv.config(highlightthickness=0)                 
 
        ybar = Scrollbar(parent)
        ybar.config(command=canv.yview)                   
        ## connect the two widgets together
        canv.config(yscrollcommand=ybar.set)              
        ybar.pack(side=RIGHT, fill=Y)                     
        canv.pack(side=LEFT, expand=YES, fill=BOTH)       
 
        for ctr in range(10):
            frm = Frame(parent,width=960, height=100,bg="#cfcfcf",bd=2)
            frm.config(relief=SUNKEN)
            Label(frm, text="Frame #"+str(ctr+1)).grid()
            canv.create_window(10,10+(100*ctr),anchor=NW, window=frm)
 
if __name__ == '__main__':
   root=Tk()
   ScrolledCanvas(root)
   root.mainloop() 