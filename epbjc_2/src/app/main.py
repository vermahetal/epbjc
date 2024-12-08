#import sqlite3  # Importa a biblioteca SQLite para trabalhar com bases de dados

#conn = sqlite3.connect('database.db')  # Conecta à base de dados SQLite ou cria-a se não existir
#cursor = conn.cursor()  # Cria um objeto cursor para executar comandos SQL

# Executa o comando SQL para criar a tabela 'cast' se não existir
#cursor.execute('''  
#                CREATE TABLE IF NOT EXISTS cast(
#               id INTEGER PRIMARY KEY AUTOINCREMENT,  # Define a chave primária com incremento automático
#               nome TEXT NOT NULL  # Coluna 'nome', que não pode ser nula
#            )
#''')

# Executa o comando SQL para criar a tabela 'genre' se não existir
#cursor.execute('''  
#            CREATE TABLE IF NOT EXISTS genre(
#            id INTEGER PRIMARY KEY AUTOINCREMENT,  # Define a chave primária com incremento automático
#            genre TEXT NOT NULL  # Coluna 'genre', que não pode ser nula
#            )
#''')

# Executa o comando SQL para criar a tabela 'kdrama' se não existir
#cursor.execute('''  
#            CREATE TABLE IF NOT EXISTS kdrama(
#               id INTEGER PRIMARY KEY AUTOINCREMENT,  # Define a chave primária com incremento automático
#               nome TEXT NOT NULL  # Coluna 'nome', que não pode ser nula
#            )
#''')

# Inserir dados nas tabelas

# Inserir nomes na tabela 'cast'
#cursor.execute('INSERT INTO cast (nome) VALUES ("Park Gyu Young")')  
#cursor.execute('INSERT INTO cast (nome) VALUES ("Kang Min Hyuk")')  
#cursor.execute('INSERT INTO cast (nome) VALUES ("Park Seo Joon")')  
#cursor.execute('INSERT INTO cast (nome) VALUES ("Kim Da Mi")')  
#cursor.execute('INSERT INTO cast (nome) VALUES ("Gong Yoo")')  
#cursor.execute('INSERT INTO cast (nome) VALUES ("Kim Go Eun")')  
#cursor.execute('INSERT INTO cast (nome) VALUES ("Hyun Bin")')  
#cursor.execute('INSERT INTO cast (nome) VALUES ("Son Ye Jin")')  
#cursor.execute('INSERT INTO cast (nome) VALUES ("Song Joong Ki")')  
#cursor.execute('INSERT INTO cast (nome) VALUES ("Song Hye Kyo")')  
#cursor.execute('INSERT INTO cast (nome) VALUES ("Jeon Yeo Been")')  
#cursor.execute('INSERT INTO cast (nome) VALUES ("Ok Taec Yeon")')  
#cursor.execute('INSERT INTO cast (nome) VALUES ("Kim Soo Hyun")')  
#cursor.execute('INSERT INTO cast (nome) VALUES ("Jun Ji Hyun")')  
#cursor.execute('INSERT INTO cast (nome) VALUES ("Nam Joo Hyuk")')  

# Inserir géneros na tabela 'genre'
#cursor.execute('INSERT INTO genre (genre) VALUES ("Thriller")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Drama")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Drama")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Romance")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Fantasy")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Romance")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Romance")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Drama")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Action")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Romance")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Romance")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Crime")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Romance")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Sci-Fi")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Romance")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Drama")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Romance")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Drama")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Romance")')  
#cursor.execute('INSERT INTO genre (genre) VALUES ("Comedy")')  

# Inserir nomes na tabela 'kdrama'
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Celebrity")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Itaewon Class")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Goblin")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Crash Landing on You")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Descendants of the Sun")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Vincenzo")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("My Love from the Star")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Start Up")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("The Heirs")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Hometown Cha Cha Cha")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("True Beauty")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Extraordinary Attorney Woo")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Twenty Five Twenty One")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Alchemy of Souls")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Weightlifting Fairy Kim Bok Joo")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Tomorrow")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Mr Sunshine")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Business Proposal")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Signal")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Hotel Del Luna")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Strong Woman Do Bong Soon")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Its Okay to Not Be Okay")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("The Penthouse War in Life")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Doctor Stranger")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("While You Were Sleeping")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Cheese in the Trap")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("The King Eternal Monarch")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Love Alarm")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("The Legend of the Blue Sea")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Moon Lovers Scarlet Heart Ryeo")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Secret Garden")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Pinocchio")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("The World of the Married")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Reply 1988")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Sky Castle")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Prison Playbook")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("My Mister")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Doctor Romantic")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Live")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Her Private Life")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Into the Ring")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("My ID is Gangnam Beauty")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Find Me in Your Memory")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("The Smile Has Left Your Eyes")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("When the Camellia Blooms")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Angel Eyes")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Flower of Evil")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Man to Man")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("Cheer Up")')  
#cursor.execute('INSERT INTO kdrama (nome) VALUES ("The Glory")')  

# Selecionar dados da tabela 'cast' onde o nome é 'Shin Min Ah'
#cursor.execute('SELECT nome FROM cast WHERE nome = ("Shin Min Ah")')  

# Selecionar todos os resultados e imprimir
#resultados = cursor.fetchall()  # Obtém todos os resultados da consulta
#for cast in resultados:  # Para cada linha de resultados, imprime o valor
#    print(cast)

#resultados = cursor.fetchall()  # Obtém todos os resultados da tabela 'genre'
#for genre in resultados:  # Para cada linha de resultados, imprime o valor
#    print(genre)

#resultados = cursor.fetchall()  # Obtém todos os resultados da tabela 'kdrama'
#for kdrama in resultados:  # Para cada linha de resultados, imprime o valor
#    print(kdrama)

# Apagar dados das tabelas
#cursor.execute("DELETE FROM cast WHERE id = 3 AND nome ='Park Seo Joon';")  # Apaga um nome específico da tabela 'cast'
#cursor.execute("DELETE FROM genre WHERE id = 6 AND genre ='Romance';")  # Apaga um género específico da tabela 'genre'
#cursor.execute("DELETE FROM kdrama WHERE nome = 'Celebrity';")  # Apaga um kdrama específico da tabela 'kdrama'

# Commit para aplicar as alterações
#conn.commit()  # Aplica as alterações feitas na base de dados

# Fechar a conexão com a base de dados
#conn.close()  # Fecha a ligação à base de dados
