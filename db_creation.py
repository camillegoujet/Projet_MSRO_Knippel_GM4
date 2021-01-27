import sqlite3

conn = sqlite3.connect('sqli_db.db')

c = conn.cursor()

c.execute('''CREATE TABLE users
(username TEXT, password TEXT)''')

c.execute('''INSERT INTO users
VALUES('user1','mdpUser1')''')
c.execute('''INSERT INTO users
VALUES('admin','mdpAdmin')''')
conn.commit()

conn.close()