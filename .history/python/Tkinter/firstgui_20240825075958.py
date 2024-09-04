import sqlite3
conn = sqlite3.connect('greg.db')
cun = conn.cursor()
cun.execute('''CREATE TABLE IF NOT EXISTS greg
            (parents TEXT, children TEXT, grandchildren TEXT)''')
data = cun.execute('''SELECT parents,children FROM greg''')
for i in data:
    print(i[0][0])

conn.close()