import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM cast WHERE id = 3 AND nome = 'Park Seo Joon';")

conn.commit()
conn.close()