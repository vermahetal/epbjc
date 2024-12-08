import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS cast(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL
            )
''')

conn.commit()
conn.close()