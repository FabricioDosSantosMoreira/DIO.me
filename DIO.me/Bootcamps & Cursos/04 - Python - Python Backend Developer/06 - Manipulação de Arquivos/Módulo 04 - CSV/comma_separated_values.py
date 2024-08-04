# - - - - - > Manipulação de Arquivos CSV:

#                 Arquivos CSV (Comma-Separated Values) são arquivos de texto 
#             que armazenam dados em formato tabular, onde cada linha 
#             corresponde a uma linha da tabela e os valores de cada 
#             linha são separados por vírgulas.

# - - - - -> Exemplos de Manipulação de Arquivos CSV:
print("\nExemplos de Manipulação de Arquivos CSV:")

from pathlib import Path
from typing import List

import csv

ROOT_PATH: Path = Path(__file__).parent

# - - - > Exemplo de Escrita em um Arquivo CSV:
print("\nExemplo de Escrita em um Arquivo CSV:")

dados: List = [
    ['Nome', 'Idade', 'Cidade'],
    ['João', '30', 'São Paulo'],
    ['Maria', '25', 'Rio de Janeiro'],
    ['Pedro', '35', 'Belo Horizonte']
]

caminho = ROOT_PATH / "dados.csv"

try:
    with open(caminho, 'w', encoding= 'utf-8', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)

        for linha in dados:
            print(f"Escrevendo a linha: {linha}")
            escritor_csv.writerow(linha)

except IOError as exc:
    print(f"\nErro ao criar o arquivo: {exc}")

# - - - > Exemplo de Leitura de um Arquivo CSV:
print("\nExemplo de Leitura de um Arquivo CSV:")

caminho = ROOT_PATH / "dados.csv"

with open(caminho, 'r', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    for linha in leitor_csv:
        print(f"Lendo a linha: {linha}")


# - - - > Exemplo de Leitura de um Arquivo CSV com DictReader:
print("\nExemplo de Leitura de um Arquivo CSV com DictReader:")

caminho = ROOT_PATH / "dados.csv"

try:
    with open(caminho, newline="", encoding='utf-8') as arquivo_csv:
        reader = csv.DictReader(arquivo_csv)

        print(f"Cabeçalho do CSV: {reader.fieldnames}") # NOTE: Cabeçalho do arquivo CSV 

        for row in reader:
            print(f"\nNome: {row['Nome']}")
            print(f"Idade: {row['Idade']}")
            print(f"Cidade: {row['Cidade']}")

except Exception as exc:
    print(f"\nExceção: {exc}")
    