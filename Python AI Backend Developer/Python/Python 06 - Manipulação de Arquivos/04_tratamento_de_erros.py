# IOError
# UnicodeDecodeError
# UnicodeEncodeError
# IsADirectoryError

from pathlib import Path
try:
    arquivo = open('arquivo_nao_existente.txt', 'r')
except FileNotFoundError as exc:
    print("\nArquivo não encontrado!")
    print(exc)



ROOT_PATH = Path(__file__).parent
print(ROOT_PATH)

try:
    arquivo = open(ROOT_PATH / 'novo_diretorio', 'r')
except IsADirectoryError as exc:
    print("\nNão foi possivel abrir o arquivo!")
    print(exc)

except PermissionError as exc:
    print("\nERRO de permisao!")
    print(exc)