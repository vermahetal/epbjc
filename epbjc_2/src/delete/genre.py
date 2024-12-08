import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM genre WHERE id = 6 AND genre ='Romance';")

conn.commit()
conn.close()