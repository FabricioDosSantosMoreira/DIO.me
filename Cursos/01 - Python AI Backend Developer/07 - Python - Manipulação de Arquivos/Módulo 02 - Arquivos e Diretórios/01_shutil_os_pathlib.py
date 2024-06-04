# - - - - -> Manipulação de Arquivos e Diretórios:

    #   Os módulos 'os', 'shutil' e 'pathlib' são amplamente utilizados para manipulação 
    # de arquivos e diretórios em Python. Eles oferecem diversas funções e métodos para 
    # realizar operações como criação, leitura, escrita, exclusão, renomeação e navegação 
    # em arquivos e diretórios no sistema de arquivos.

# - - - - -> Módulo 'os':

    #   O módulo 'os' fornece uma interface para interagir com o sistema operacional. Ele 
    # permite realizar operações relacionadas ao sistema operacional, como manipulação de 
    # diretórios, execução de comandos do sistema e manipulação de variáveis de ambiente.

# - - - - -> Módulo 'shutil':

    #   O módulo 'shutil' fornece operações de alto nível para manipulação de arquivos e 
    # diretórios. Ele oferece funções para copiar, mover, renomear e excluir arquivos e 
    # diretórios de forma mais conveniente.

# - - - - -> Módulo 'pathlib':

    #   O módulo 'pathlib' fornece uma API orientada a objetos para manipulação de caminhos 
    # de arquivos e diretórios. Ele oferece uma forma mais intuitiva e eficiente de 
    # trabalhar com caminhos do que as funções disponíveis nos módulos 'os' e 'shutil'.


# - - - - -> Exemplos de Utilização dos Módulos 'os', 'shutil' e 'pathlib':

# - - - -> Utilizando o Módulo 'os':
import os

# - - -> Criação de diretórios:
os.makedirs("./utils/diretorio_exemplo", exist_ok=True)


# - - -> Listagem de arquivos em um diretório:
print(f"\nArquivos no diretório './utils': {os.listdir('./utils')}")


# - - -> Listagem de drives:
print(f"\nDrives: {os.listdrives()}")


# - - -> Renomeação de arquivo:
os.rename("./utils/exemplo.txt", "./utils/exemplo_renomeado.txt")


# - - -> Exclusão de arquivo:
os.remove("./utils/exemplo_renomeado.txt")


# - - - -> Utilizando o Módulo 'shutil':
import shutil

# - - -> Cópia de arquivo:
shutil.copy("./utils/lorem.txt", "copia_lorem.txt")


# - - -> Mover arquivo:
shutil.move("copia_lorem.txt", "./utils/")


# Exclusão de diretório
shutil.rmtree("./utils/diretorio_exemplo")


# - - - -> Utilizando o Módulo 'pathlib':
from pathlib import Path

# - - -> Criação de caminho:
caminho = Path("./utils/lorem.txt")
print(f"\nCaminho: {caminho}")


# - - -> Verificação de existência:
print(f"\nVerificação de existência: {caminho.exists()}")


# - - -> Leitura do nome do arquivo:
print(f"\nNome do arquivo: {caminho.name}")


# - - -> Obtenção do diretório pai:
print(f"\nDiretório pai: {caminho.parent}")


# - - -> Obtenção da extensão do arquivo:
print(f"\nExtensão do arquivo: {caminho.suffix}")


# - - - -> Tips:

ROOT_PATH = Path(__file__).parent

print(__file__)
print(ROOT_PATH)

os.mkdir(ROOT_PATH / 'novo_diretorio') # A '/' detecta o separador do sistema operacional

os.rename(ROOT_PATH / 'novo_diretorio', ROOT_PATH / 'diretorio renomeado')
