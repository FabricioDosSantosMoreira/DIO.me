import shutil
import os

from pathlib import Path

ROOT_PATH = Path(__file__).parent

print(__file__)
print(ROOT_PATH)


# os.mkdir(ROOT_PATH / 'novo_diretorio') # O / Detecta qual os ta usando e trabalha nisso

arquivo = open(ROOT_PATH / 'novo_arquivo.txt', 'w')
arquivo.close()

os.rename(ROOT_PATH/'novo_arquivo.txt', ROOT_PATH/'arquivo_renomeado.txt')

# os.remove(ROOT_PATH/'arquivo_renomeado.txt')

shutil.move(ROOT_PATH/'arquivo_renomeado.txt', ROOT_PATH/'novo_diretorio')