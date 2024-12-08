import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM kdrama WHERE nome = 'Celebrity';")

conn.commit()
conn.close()