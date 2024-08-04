import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "util/database.sqlite")
cur = conn.cursor()
cur.row_factory = sqlite3.Row


id_cliente: int = input("\nInforme o id do cliente: ") # NOTE: Utilize '1 OR 1=1'

cur.execute(f'SELECT * FROM clientes WHERE id={id_cliente};')
clientes = cur.fetchall()

for c in clientes:
    print(f"\nCliente: {dict(c)}")
