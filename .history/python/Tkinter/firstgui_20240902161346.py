import sqlite3
conn = sqlite3.connect('greg.db')
lst = ['xzx','ahwah']
cun = conn.cursor()
cun.execute('''CREATE TABLE IF NOT EXISTS greg
            (parents TEXT, children TEXT, grandchildren TEXT)''')
sql = ''' INSERT INTO greg(children)
              VALUES(?) '''
for i in range(len(lst)):
    cun.execute(sql,i)
conn.commit()
data = cun.execute('''SELECT children,grandchildren FROM greg''')
for i in data:
    print(i)

conn.close()