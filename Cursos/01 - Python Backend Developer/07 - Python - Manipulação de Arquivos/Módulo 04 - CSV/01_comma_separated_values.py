# - - - - -> Manipulação de Arquivos CSV:

    #   Arquivos CSV (Comma-Separated Values) são arquivos de texto que armazenam dados em formato tabular, 
    # onde cada linha corresponde a uma linha da tabela e os valores de cada linha são separados por vírgulas.


# - - - - -> Exemplo de Manipulação de Arquivos CSV:
from pathlib import Path

import csv

ROOT_PATH = Path(__file__).parent

# - - - -> Escrita em um arquivo CSV:
dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['João', '30', 'São Paulo'],
    ['Maria', '25', 'Rio de Janeiro'],
    ['Pedro', '35', 'Belo Horizonte']
]

try:
    with open(ROOT_PATH / 'dados.csv', 'w', encoding= 'utf-8', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        for linha in dados:
            escritor_csv.writerow(linha)
except IOError as exc:
    print(f"Erro ao criar o arquivo: {exc}")


# - - - -> Leitura de um arquivo CSV:
with open(ROOT_PATH / 'dados.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        print(linha)


# - - - -> Tips:
try:
    with open(ROOT_PATH / "dados.csv", newline="", encoding='utf-8') as arquivo_csv:
        reader = csv.DictReader(arquivo_csv)

        print(reader.fieldnames)    # Cabeçalho do CSV 

        for row in reader:
            print(f"\nNome: {row['Nome']}")
            print(f"Idade: {row['Idade']}")
            print(f"Cidade: {row['Cidade']}")

except Exception as exc:
    print(f"\nExceção: {exc}")
    