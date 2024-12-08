Este projeto é um Sistema de Gestão de Base de Dados de K-Dramas que utiliza SQLite, O projeto está organizado em ficheiros Python, cada um responsável por uma tarefa específica. O objetivo é realizar operações CRUD (Criar, Ler, Atualizar, Apagar) em três tabelas:

kdrama: Guarda os nomes das séries de K-Drama.
genre: Guarda os géneros associados às séries (ex.: romance, thriller).
cast: Guarda os nomes dos atores que participaram nas séries.

Create (Criação de Tabelas):
kdrama.py: Cria a tabela kdrama com os nomes das séries.
genre.py: Cria a tabela genre com os géneros.
cast.py: Cria a tabela cast com os nomes dos atores.

Insert (Inserção de Dados):
kdrama.py: Insere os nomes das séries de K-Drama (ex.: Goblin, Itaewon Class).
genre.py: Insere os géneros das séries (ex.: Drama, Romance).
cast.py: Insere os nomes dos atores (ex.: Kim Soo Hyun, Shin Min Ah).

Read (Consulta de Dados):
kdrama.py: Lê e imprime todos os nomes das séries da tabela kdrama.
genre.py: Lê e imprime todos os géneros da tabela genre.
cast.py: Filtra e imprime apenas o nome do ator "Shin Min Ah" na tabela cast.

Update:
Vazio: Ainda não foi implementada nenhuma funcionalidade de atualização.


epbjc/
│
└── src/
│    ├── app/
│    └── main.py       
│
├── create/           
│   ├── kdrama.py     
│   ├── genre.py      
│   └── cast.py       
│
├── insert/           
│   ├── kdrama.py    
│   ├── genre.py      
│   └── cast.py      
│
├── read/            
│   ├── kdrama.py     
│   ├── genre.py      
│   └── cast.py       
│
└── update/ 
│
├── README.md       
├── db.db  
