import sqlite3
conn = sqlite3.connect('accounts.db')
ggg = [('15','62',),('6','10',),]
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
cun.execute(sql, ggg)
conn.commit()
data = cun.execute('''SELECT cata,ID FROM database''')
for i in data:
    print(i)

conn.close()