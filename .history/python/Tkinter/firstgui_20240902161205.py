import sqlite3
conn = sqlite3.connect('greg.db')
lst = [('aghahya',),("")]
cun = conn.cursor()
cun.execute('''CREATE TABLE IF NOT EXISTS greg
            (parents TEXT, children TEXT, grandchildren TEXT)''')
sql = ''' INSERT INTO greg(children)
              VALUES(?,?,?) '''
cun.execute(sql,lst)
conn.commit()
data = cun.execute('''SELECT children FROM greg''')
for i in data:
    print(i)

conn.close()