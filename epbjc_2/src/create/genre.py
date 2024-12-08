import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS genre(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
               genre TEXT NOT NULL
            )
''')

conn.commit()
conn.close()