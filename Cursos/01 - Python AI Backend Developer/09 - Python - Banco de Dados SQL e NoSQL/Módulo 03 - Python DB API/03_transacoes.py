import sqlite3
from pathlib import Path
from typing import Any, List, Tuple

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / 'meu_banco.sqlite')
cur = conn.cursor()
cur.row_factory = sqlite3.Row


try:
    cur.execute(
        'INSERT INTO clientes (nome, email) VALUES (?, ?)', ('teste 2', 'teste1@teste.com'),
    )

    cur.execute(
        'INSERT INTO clientes (id, nome, email) VALUES (?, ?)', (2, 'teste 3', 'teste1@teste.com'),
    )

    conn.commit()

except Exception as exc:
    print(f"Ops! Occoreu um erro {exc}")
    conn.rollback()

   