# - - - - - > Leitura de Arquivos:

#                 A leitura de arquivos é um processo comum em muitos programas Python, 
#             permitindo que você acesse e manipule o conteúdo de arquivos externos. 
#             O Python fornece várias maneiras de ler arquivos, dependendo dos 
#             requisitos específicos do seu programa.


# - - - - > Exemplos de Leitura de Arquivos:
print("\nExemplos de Leitura de Arquivos:")


# - - - > Abrindo e Lendo Todo um Arquivo:
print("\nAbrindo e Lendo Todo um Arquivo:")

arquivo: str = "./util/lorem.txt"

with open(arquivo, 'r', encoding='utf-8') as arquivo:
    
    # NOTE: Lê todo o arquivo
    conteudo = arquivo.read()  

    print(f"\nConteúdo do arquivo: \n{conteudo}")


# - - - > Abrindo e Lendo Linhas de um Arquivo:
print("\nAbrindo e Lendo Linhas de um Arquivo:")

caminho: str = "./util/lorem.txt"

with open(caminho, 'r', encoding='utf-8') as arquivo:

    # NOTE: Retorna uma lista com o conteúdo de cada linha
    linhas = arquivo.readlines() 

    print("\nLinhas do arquivo:")
    for linha in linhas:
        # NOTE: O 'strip()' remove espaços em branco extras, como quebras de linha
        print(linha.strip()) 


# - - - > Abrindo e Lendo um Arquivo Linha por Linha:
print("\nAbrindo e Lendo um Arquivo Linha por Linha:")

caminho: str = "./util/lorem.txt"

with open(caminho, 'r', encoding='utf-8') as arquivo:

    print("\nConteúdo do arquivo linha por linha:")
    while len((linha := arquivo.readline())):
        # NOTE: O 'strip()' remove espaços em branco extras, como quebras de linha
        print(linha.strip())


# - - - - > Dicas Sobre a Leitura de Arquivos:

#           * arquivo.read(): Lê todo o arquivo

#           * arquivo.readline(): Retorna linha a linha

#           * arquivo.readlines(): Retorna uma lista contendo as str de cada linha

#           * operador walrus: Permite a atribuição de uma variável dentro de uma expressão
#           while len((linha := arquivo.readline())):
#               print(linha)

#           * Usando a palavra-chave 'with' não é necessário fechar o 
#             arquivo usando 'arquivo.close()' toda vez. O 'with' sempre
#             fechará o arquivo, mesmo em casos de erro

#           * 'arquivo.seek(0)': Volta ao início do arquivo para recomeçar a leitura
