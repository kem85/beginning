import sqlite3
conn = sqlite3.connect("C:/Users/kem7/Documents/GitHub/beginning/python/Tkinter/greg.db")
cun = conn.cursor()
cun.execute('''CREATE TABLE IF NOT EXISTS greg
            (parents TEXT, children TEXT, grandchildren TEXT''')
conn.close()
cun.close()