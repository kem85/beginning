import sqlite3
conn = sqlite3.connect('accounts.db')
lst = ([])
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
print(lst[num1])
# for i in range(4):
#     ggg = ()
#     cun.executemany(sql, ggg)
conn.commit()
data = cun.execute('''SELECT cata,ID FROM database''')
for i in data:
    print(i)

conn.close()