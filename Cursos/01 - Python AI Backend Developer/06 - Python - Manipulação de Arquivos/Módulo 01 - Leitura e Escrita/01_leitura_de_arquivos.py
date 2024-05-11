# - - - - -> Leitura de Arquivos:

    #   A leitura de arquivos é um processo comum em muitos programas Python, permitindo que
    # você acesse e manipule o conteúdo de arquivos externos. O Python fornece várias 
    # maneiras de ler arquivos, dependendo dos requisitos específicos do seu programa.


# - - - - -> Exemplo de Leitura de Arquivos:

# - - - -> Abrir e ler todo um arquivo:
arquivo = "./utils/lorem.txt"

with open(arquivo, 'r', encoding='utf-8') as arquivo:

    conteudo = arquivo.read()  # Lê todo o arquivo
    print(f"\nConteúdo do arquivo: \n{conteudo}")


# - - - -> Abrir e ler linhas de um arquivo:
arquivo = "./utils/lorem.txt"

with open(arquivo, 'r', encoding='utf-8') as arquivo:

    linhas = arquivo.readlines()  # Retorna uma lista com o conteúdo de cada linha
    print("\nLinhas do arquivo:")
    for linha in linhas:
        print(linha.strip())  # strip() remove espaços em branco extras, como quebras de linha


# - - - -> Abrir e ler um arquivo linha por linha:
arquivo = "./utils/lorem.txt"

with open(arquivo, 'r', encoding='utf-8') as arquivo:

    print("\nConteúdo do arquivo linha por linha:")
    while len((linha := arquivo.readline())):
        print(linha.strip()) # strip() remove espaços em branco extras, como quebras de linha


# - - - -> Tips:

    # arquivo.read() Lê todo o arquivo
    # arquivo.readline() Retorna linha a linha
    # arquivo.readlines() Retorna uma lista contendo as str de cada linha

    # while len((linha := arquivo.readline())):
    #     print(linha)

    # Usando a palavra-chave 'with' não é necessário fechar o 
    # arquivo usando 'arquivo.close()' toda vez. O 'with' sempre
    # fechará o arquivo, mesmo em casos de erro

    # 'arquivo.seek(0)' volta ao início do arquivo para recomeçar a leitura
