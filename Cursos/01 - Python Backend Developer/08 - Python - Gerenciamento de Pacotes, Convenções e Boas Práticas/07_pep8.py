# - - - - -> Recomendações da PEP8:

# - - - - -> Introdução:
    #   A PEP8 é uma guia de estilo para código Python, que visa melhorar a legibilidade 
    # e consistência do código fonte. Ela define recomendações sobre formatação, 
    # convenções de nomes, comentários, entre outros aspectos.


# - - - - -> Recomendações Gerais:
    #   Algumas recomendações gerais da PEP8 incluem:
    #   - Utilizar indentação de 4 espaços.
    #   - Limitar linhas a 79 caracteres.
    #   - Utilizar espaços em vez de tabs.
    #   - Separar funções e classes por duas linhas em branco.


# - - - - -> Nomeação de Variáveis e Funções:
    #   Seguir as seguintes convenções de nomeação:
    #   - Utilizar snake_case para nomes de variáveis e funções.
    #   - Utilizar NOMES_DE_CONSTANTES_COM_LETRAS_MAIUSCULAS para constantes.


# - - - - -> Comentários:
    #   Comentar o código de forma clara e concisa, seguindo estas recomendações:
    #   - Utilizar comentários para explicar o código quando necessário.
    #   - Limitar linhas de comentário a 72 caracteres.
    #   - Utilizar docstrings para documentar funções e módulos.


# - - - - -> Exemplo de Script com Recomendações da PEP8:

# - - - -> Importação de Módulos:
import os  # Importação do módulo 'os'


# - - - -> Definição de Constantes:
ARQUIVO_PADRAO = 'dados.txt'  # Constante para o nome do arquivo padrão


# - - - -> Definição de Funções:
def ler_arquivo(nome_arquivo):
    """
    Função para ler o conteúdo de um arquivo.

    Args:
        nome_arquivo (str): Nome do arquivo a ser lido.

    Returns:
        str: Conteúdo do arquivo.
    """
    with open(nome_arquivo, 'r') as file:
        return file.read()


def escrever_arquivo(nome_arquivo, conteudo):
    """
    Função para escrever conteúdo em um arquivo.

    Args:
        nome_arquivo (str): Nome do arquivo a ser escrito.
        conteudo (str): Conteúdo a ser escrito no arquivo.
    """
    with open(nome_arquivo, 'w') as file:
        file.write(conteudo)


# - - - -> Uso das Funções:
conteudo_arquivo = ler_arquivo(ARQUIVO_PADRAO)  # Lendo o arquivo padrão
print(conteudo_arquivo)

escrever_arquivo(ARQUIVO_PADRAO, "Novo conteúdo")  # Escrevendo no arquivo padrão
print("Conteúdo do arquivo atualizado")
