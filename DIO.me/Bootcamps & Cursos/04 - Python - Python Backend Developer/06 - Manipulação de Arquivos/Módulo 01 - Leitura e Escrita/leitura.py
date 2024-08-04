# - - - - - > Leitura de Arquivos:
#                 A leitura de arquivos é um processo comum em muitos programas Python, 
#             permitindo que você acesse e manipule o conteúdo de arquivos externos. 
#             O Python fornece várias maneiras de ler arquivos, dependendo dos 
#             requisitos específicos do seu programa.


# - - - - > Exemplos de Leitura de Arquivos:
print("\nExemplos de Leitura de Arquivos:")

from pathlib import Path

ROOT_PATH: Path = Path(__file__).parent
caminho: Path = Path(ROOT_PATH / "util/lorem.txt")

# - - - > Abrindo e Lendo Todo um Arquivo:
print("\nAbrindo e Lendo Todo um Arquivo:")

with open(caminho, 'r', encoding='utf-8') as arquivo:
    
    # NOTE: Lê todo o arquivo
    conteudo = arquivo.read()  
    print(f"\nConteúdo do arquivo: \n{conteudo}")


# - - - > Abrindo e Lendo Linhas de um Arquivo:
print("\nAbrindo e Lendo Linhas de um Arquivo:")

with open(caminho, 'r', encoding='utf-8') as arquivo:

    # NOTE: Retorna uma lista com o conteúdo de cada linha
    linhas = arquivo.readlines() 

    print("\nLinhas do arquivo:")
    for linha in linhas:
        # NOTE: O 'strip()' remove espaços em branco extras, como quebras de linha
        print(linha.strip()) 


# - - - > Abrindo e Lendo um Arquivo Linha por Linha:
print("\nAbrindo e Lendo um Arquivo Linha por Linha:")

with open(caminho, 'r', encoding='utf-8') as arquivo:

    print("\nConteúdo do arquivo linha por linha:")
    while len((linha := arquivo.readline())):
        # NOTE: O 'strip()' remove espaços em branco extras, como quebras de linha
        print(linha.strip())
