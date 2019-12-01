import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

c.execute("""CREATE TABLE users(
                       name text,
                       username text,
                       pass text)""")



#c.execute('INSERT into users VALUES (?,?,?)',(user,name,password))

conn.commit()
conn.close()
