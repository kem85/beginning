import sqlite3
conn = sqlite3.connect('accounts.db')
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
conn.commit()
data = cun.execute('''SELECT cata,ID FROM database''')
for i in data:
    print(i)

conn.close()