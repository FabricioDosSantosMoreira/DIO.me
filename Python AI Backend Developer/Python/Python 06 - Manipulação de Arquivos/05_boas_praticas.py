from pathlib import Path

ROOT_PATH = Path(__file__).parent


# O arquivo sempre fecha com 'with', evitando desperdicio de memoria em caso de erros
with open(ROOT_PATH / 'lorem.txt', 'r') as arquivo:
    print(arquivo.read())


try:
    with open(ROOT_PATH / 'a.txt', 'r') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print("\nERRO AO ABRIR O ARQUIVO")
    print(exc)



try:
    with open(ROOT_PATH / 'encodingutf8.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('Aprendendo a manipular')
except IOError as exc:
    print("\nERRO AO ABRIR O ARQUIVO")
    print(exc)
