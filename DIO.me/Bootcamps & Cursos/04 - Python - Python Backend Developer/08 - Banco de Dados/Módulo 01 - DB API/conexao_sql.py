import sqlite3
from pathlib import Path
from typing import Any, List, Tuple

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "util/database.sqlite")
cur = conn.cursor()
cur.row_factory = sqlite3.Row


def criar_tabela(conn: sqlite3.Connection, cur: sqlite3.Cursor) -> None:
    cur.execute(
        'CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150));' 
    )

    conn.commit()


def inserir_registro(conn: sqlite3.Connection, cur: sqlite3.Cursor, nome: str, email: str) -> None:
    data = (nome, email)

    cur.execute(
        "INSERT INTO clientes (nome, email) VALUES (?, ?);", data
    )

    conn.commit()


def atualizar_registro(conn: sqlite3.Connection, cur: sqlite3.Cursor, nome: str, email: str, id: int) -> None:

    data = (nome, email, id)

    cur.execute(
        'UPDATE clientes SET nome=?, email=? WHERE id=?;', data
    )

    conn.commit()


def remover_registro(conn: sqlite3.Connection, cur: sqlite3.Cursor, id: int) -> None:
    data = (id, )

    cur.execute(
        'DELETE FROM clientes WHERE id=?;', data
    )
    
    conn.commit()


def inserir_muitos(conn: sqlite3.Connection, cur: sqlite3.Cursor, data: List[Tuple]):

    cur.executemany(
        'INSERT INTO clientes (nome, email) VALUES (?,?);', data
        )

    conn.commit()


def recuperar_cliente(cur: sqlite3.Cursor, id: int) -> Any:
    
    cur.execute(
        'SELECT * FROM clientes WHERE id=?;', (id, )
    )

    return cur.fetchone()


def listar_clientes(cur: sqlite3.Cursor) -> Any:
    clientes = cur.execute(
        'SELECT * FROM clientes ORDER BY nome ASC;'
    )

    return clientes


criar_tabela(conn, cur)

inserir_registro(conn, cur, 'Teste', 'teste@teste.com')

atualizar_registro(conn, cur, 'Teste 2', 'teste2@teste.com', 1)

remover_registro(conn, cur, 1)

dados: List[Tuple] = [
    ("Usuário 1", "Usuário1@gmail.com"),
    ("Usuário 2", "Usuário2@gmail.com"),
    ("Usuário 3", "Usuário3@gmail.com"),
]

inserir_muitos(conn, cur, dados)

print(f"\nCliente com id=2: {dict(recuperar_cliente(cur, 2))}")

clientes = listar_clientes(cur)
for c in clientes:
    print(f"\nCliente: {dict(c)}")
