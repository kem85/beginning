import sqlite3
conn = sqlite3.connect('accounts.db')
width = '15'
height = '10'
lenbutton = '500'
lst = [width,height,lenbutton]
cun = conn.cursor()
cun.execute('''CREATE TABLE database (
    cata     TEXT,
    ID       TEXT,
    [order]  TEXT,
    suborder TEXT,
    name     TEXT,
    email    TEXT,
    password TEXT,
    color    TEXT DEFAULT ('6e40c0') 
);''')
sql = ''' INSERT INTO database(cata)
              VALUES(?) '''
for i,ls in enumerate(lst):
    g = (lst[i],)
    cun.execute(sql, g)
conn.commit()
data = cun.execute('''SELECT children FROM database''')
for i in data:
    print(i)

conn.close()