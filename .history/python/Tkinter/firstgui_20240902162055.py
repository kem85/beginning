import sqlite3
conn = sqlite3.connect('greg.db')
width = '15'
height = '10'
lenbutton = '500'
# lst = [(width,),(height,),(lenbutton,),]
lst = [width,height,lenbutton]
cun = conn.cursor()
cun.execute('''CREATE TABLE IF NOT EXISTS greg
            (parents TEXT, children TEXT, grandchildren TEXT)''')
sql = ''' INSERT INTO greg(children)
              VALUES(?) '''
for i,ls in enumerate(lst):
    g = (lst[i],)
    cun.execute(sql, g)
conn.commit()
data = cun.execute('''SELECT children FROM greg''')
for i in data:
    print(i)

conn.close()