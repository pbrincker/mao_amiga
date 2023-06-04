import sqlite3
from random import randint

# Cria o banco de dados e a tabela
conn = sqlite3.connect('multas.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cpf TEXT,
        data_nascimento TEXT
    )
''')
c.execute('''
    CREATE TABLE IF NOT EXISTS multas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pessoa_id INTEGER,
        descricao TEXT,
        valor REAL,
        FOREIGN KEY (pessoa_id) REFERENCES pessoas (id)
    )
''')

# Insere informações fictícias para cinco pessoas
pessoas = [
    ("João", "123.456.789-00", "1990-01-01"),
    ("Maria", "987.654.321-00", "1995-02-02"),
    ("Pedro", "111.222.333-00", "1985-03-03"),
    ("Ana", "444.555.666-00", "1987-04-04"),
    ("José", "777.888.999-00", "1992-05-05")
]

for pessoa in pessoas:
    c.execute('INSERT INTO pessoas (nome, cpf, data_nascimento) VALUES (?, ?, ?)', pessoa)

# Insere multas aleatórias para cada pessoa
multas = []
for pessoa_id in range(1, len(pessoas) + 1):
    num_multas = randint(1, 5)
    for _ in range(num_multas):
        descricao = f"Infração {randint(1000, 9999)}"
        valor = round(randint(100, 1000) + randint(1, 99) / 100, 2)
        multas.append((pessoa_id, descricao, valor))

c.executemany('INSERT INTO multas (pessoa_id, descricao, valor) VALUES (?, ?, ?)', multas)

# Salva as alterações no banco de dados e fecha a conexão
conn.commit()
conn.close()
