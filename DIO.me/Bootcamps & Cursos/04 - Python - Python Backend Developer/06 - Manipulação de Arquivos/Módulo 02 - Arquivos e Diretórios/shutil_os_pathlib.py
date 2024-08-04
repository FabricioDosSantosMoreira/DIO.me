# - - - - - > Manipulação de Arquivos e Diretórios:
#                 Os módulos 'os', 'shutil' e 'pathlib' são amplamente utilizados para manipulação 
#             de arquivos e diretórios em Python. Eles oferecem diversas funções e métodos para 
#             realizar operações como criação, leitura, escrita, exclusão, renomeação e navegação 
#             em arquivos e diretórios no sistema de arquivos.

# - - - - > Módulo 'os':
#               O módulo 'os' fornece uma interface para interagir com o sistema operacional. Ele 
#           permite realizar operações relacionadas ao sistema operacional, como manipulação de 
#           diretórios, execução de comandos do sistema e manipulação de variáveis de ambiente.

# - - - - > Módulo 'shutil':
#               O módulo 'shutil' fornece operações de alto nível para manipulação de arquivos e 
#           diretórios. Ele oferece funções para copiar, mover, renomear e excluir arquivos e 
#           diretórios de forma mais conveniente.

# - - - - > Módulo 'pathlib':
#               O módulo 'pathlib' fornece uma API orientada a objetos para manipulação de caminhos 
#           de arquivos e diretórios. Ele oferece uma forma mais intuitiva e eficiente de 
#           trabalhar com caminhos do que as funções disponíveis nos módulos 'os' e 'shutil'.


from pathlib import Path

ROOT_PATH: Path = Path(__file__).parent


# - - - - > Exemplos de Utilização do Módulo 'os':
print("\nExemplos de Utilização do Módulo 'os':")

import os

# - - - > Exemplo de Criação de Diretório:
print("\nExemplo de Criação de Diretório:")

os.makedirs(ROOT_PATH / "util/diretorio_exemplo", exist_ok=True)


# - - - > Exemplo de Listagem de Arquivos em um Diretório:
print("\nExemplo de Listagem de Arquivos em um Diretório:")

print(f"Arquivos no diretório '/util': {os.listdir(ROOT_PATH / "util")}")


# - - - > Exemplo de Listagem de drives:
print("\nExemplo de Listagem de drives:")

print(f"Drives: {os.listdrives()}")


# - - - > Exemplo de Renomeação de Arquivo:
print("\nExemplo de Renomeação de Arquivo:")

os.rename(src=ROOT_PATH / "util/texto.txt", dst=ROOT_PATH / "util/texto_renomeado.txt")


# - - - > Exemplo de Exclusão de Arquivo:
print("\nExemplo de Exclusão de Arquivo:")

os.remove(ROOT_PATH / "util/texto_renomeado.txt")



# - - - - > Exemplos de Utilização do Módulo 'shutil':
print("\nExemplos de Utilização do Módulo 'shutil':")

import shutil

# - - - > Exemplo de Cópia de Arquivo:
print("\nExemplo de Cópia de Arquivo:")

shutil.copy(src=ROOT_PATH / "util/lorem.txt", dst=ROOT_PATH / "copia_lorem.txt")


# - - -> Exemplo de Movimentação de Arquivo:
print("\nExemplo de Movimentação de Arquivo:")

shutil.move(ROOT_PATH / "copia_lorem.txt", ROOT_PATH / "util/diretorio_exemplo")


# - - -> Exemplo de Exclusão de diretório:
print("\nExemplo de Exclusão de diretório:")

shutil.rmtree(ROOT_PATH / "util/diretorio_exemplo")



# - - - - > Exemplos de Utilização do Módulo 'pathlib':
print("\nExemplos de Utilização do Módulo 'pathlib':")

from pathlib import Path

# - - - > Exemplo de Criação de Caminho:
print("\nExemplo de Criação de Caminho:")

caminho: Path = Path(ROOT_PATH / "util/lorem.txt")
print(f"\nCaminho: {caminho}")


# - - - > Exemplo de Verificação de Existência:
print("\nExemplo de Verificação de Existência:")

print(f"Verificação de existência: {caminho.exists()}")


# - - - > Exemplo de Leitura do Nome do Arquivo:
print("\nExemplo de Leitura do Nome do Arquivo:")

print(f"Nome do arquivo: {caminho.name}")


# - - - > Exemplo de Obtenção do Diretório Pai:
print("\nExemplo de Obtenção do Diretório Pai:")

print(f"Diretório pai: {caminho.parent}")


# - - - > Exemplo de Obtenção da Extensão do Arquivo:
print("\nExemplo de Obtenção da Extensão do Arquivo:")

print(f"Extensão do arquivo: {caminho.suffix}")
