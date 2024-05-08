import csv 
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / 'usuarios.csv', 'w', encoding='utf-8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['Id', 'Nome'])
        escritor.writerow(['0', 'Fabrício'])
        escritor.writerow(['1', 'João'])

except IOError as exc:
    print(f"Erro ao criar o arquivo: {exc}")



try:
    with open(ROOT_PATH / 'usuarios.csv', 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        
        for row in leitor:
            print(row)

except IOError as exc:
    print(f"Erro ao criar o arquivo: {exc}")



# Tip
try:
    with open(ROOT_PATH / "usuarios.csv", newline="", encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader.fieldnames) # printa o cabeçalho
        for row in reader:
            print(f"Id: {row['Id']}")
            print(f"Nome: {row['Nome']}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")