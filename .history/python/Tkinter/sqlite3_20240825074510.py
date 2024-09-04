import sqlite3
from sqlite3 import *
conn = sqlite3.connect("C:/Users/kem7/Documents/GitHub/beginning/python/Tkinter")
cun = conn.cursor()
cun.execute("")
conn.close()
cun.close()