import sqlite3
conn = sqlite3.connect('accounts.db')
num1 = '15'
num2 = '62'
num3 = '70'
num4 = '44'
num5 = '33'
num6 = '22'
num7 = '12'
num8 = '66'
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
    ggg = (num[i],num[i+1])
    cun.executemany(sql, ggg)
conn.commit()
data = cun.execute('''SELECT cata,ID FROM database''')
for i in data:
    print(i)

conn.close()