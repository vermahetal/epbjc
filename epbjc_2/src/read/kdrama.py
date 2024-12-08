import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('SELECT nome FROM kdrama')

resultados = cursor.fetchall()
for kdrama in resultados:
    print (kdrama)

conn.close()  