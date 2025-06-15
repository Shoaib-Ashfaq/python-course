import sqlite3
con = sqlite3.connect('database.db')

cur = con.cursor()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)



# cur.execute("PRAGMA table_info(users)")
# print(cur.fetchall())

con.close()
