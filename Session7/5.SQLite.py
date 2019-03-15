# import sqlite3
# conn = sqlite3.connect('my_db.db')
# c = conn.cursor()
# c.execute("CREATE TABLE phone (name text, phone text)")
# c.execute("INSERT INTO phone VALUES ('John', '123456')")
# conn.commit()
# conn.close()



import sqlite3
conn = sqlite3.connect('my_db.db')
c = conn.cursor()
c.execute('SELECT name, phone FROM phone')
print(c.fetchall())
conn.close()