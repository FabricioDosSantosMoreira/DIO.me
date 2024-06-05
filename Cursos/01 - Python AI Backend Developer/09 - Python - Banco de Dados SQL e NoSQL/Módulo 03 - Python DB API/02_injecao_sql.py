import sqlite3
from pathlib import Path
from typing import Any, List, Tuple

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / 'meu_banco.sqlite')
cur = conn.cursor()
cur.row_factory = sqlite3.Row



id_cliente = input("informe o id do cliente: ")
cur.execute(f'SELECT * FROM clientes WHERE id={id_cliente};')
clientes = cur.fetchall()

for cliente in clientes:
    print(dict(cliente))