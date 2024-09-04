import sqlite3
conn = sqlite3.connect('greg.db')
cun = conn.cursor()
cun.execute('''CREATE TABLE IF NOT EXISTS greg
            (parents TEXT, children TEXT, grandchildren TEXT)''')
data = [
('city 1', 'MAC', 'distrct 1'),
('city 2', 'PSE', 'distrct 2', 15642),
('city 3', 'ZWE', 'distrct 3', 11642),
('city 4', 'USA', 'distrct 4', 14612),
('city 5', 'USA', 'distrct 5', 17672),
]
conn.commit()
conn.close()