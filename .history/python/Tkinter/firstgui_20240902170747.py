import sqlite3
conn = sqlite3.connect('accounts.db')
width = '15'
height = '10'
lenbutton = '500'
ID = ['15','62','6','10']
lst = [width,height,lenbutton]
cun = conn.cursor()
cun.execute('''CREATE TABLE IF NOT EXISTS database (
    cata     TEXT,
    ID       TEXT,
    [order]  TEXT,
    suborder TEXT,
    name     TEXT,
    email    TEXT,
    password TEXT,
    color    TEXT DEFAULT ('6e40c0') 
);''')
sql = ''' INSERT INTO database(cata,ID)
              VALUES(?,?) '''
for i in range(4):
    g = (lst[i],)
    s = (ID[i],)
    cun.execute(sql, g)
    cun.execute(sql, s)
conn.commit()
data = cun.execute('''SELECT cata FROM database''')
for i in data:
    print(i)

conn.close()