import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM genre')

resultados = cursor.fetchall()
for genre in resultados:
    print(genre)

conn.close()