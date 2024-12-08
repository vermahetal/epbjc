import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('SELECT nome FROM cast WHERE nome = ("Shin Min Ah")')

resultados = cursor.fetchall()
for cast in resultados:
    print(cast)

conn.close()