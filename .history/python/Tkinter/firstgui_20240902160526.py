import sqlite3
conn = sqlite3.connect('greg.db')
cun = conn.cursor()
cun.execute('''CREATE TABLE IF NOT EXISTS greg
            (parents TEXT, children TEXT, grandchildren TEXT)''')
sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
cur = conn.cursor()
cur.execute(sql, project)
data = cun.execute('''SELECT parents FROM greg''')
for i in data:
    print(i)

conn.close()