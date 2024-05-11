# - - - - -> Boas Práticas em Manipulação de Arquivos:

    #   Boas práticas em manipulação de arquivos envolvem técnicas e convenções para
    # garantir a eficiência, segurança e legibilidade ao lidar com operações de
    # leitura, escrita e manipulação de arquivos no Python.


# - - - - -> Abrindo e Fechando Arquivos:

    #   É importante abrir e fechar arquivos corretamente para liberar recursos
    # do sistema operacional e evitar problemas de manipulação de arquivos abertos.


# - - - - -> Modos de Abertura de Arquivos:

    #   O modo de abertura de arquivo especifica a forma como o arquivo será
    # aberto, seja para leitura ('r'), escrita ('w'), ou ambos ('r+').
    # É fundamental escolher o modo apropriado de acordo com a operação desejada.


# - - - - -> Utilização do Bloco 'with':

    #   O bloco 'with' é uma maneira elegante de lidar com a abertura e fechamento
    # automático de arquivos. Ele garante que o arquivo seja fechado corretamente
    # ao final do bloco, mesmo em caso de exceções.


# - - - - -> Encoding:

    #   O encoding especifica o conjunto de caracteres utilizado para codificar
    # o conteúdo de um arquivo. É importante especificar o encoding correto
    # ao abrir ou escrever em um arquivo para garantir que os caracteres sejam
    # interpretados corretamente.


# - - - - -> Tratamento de Erros:

    #   É crucial implementar tratamento de erros ao lidar com arquivos para
    # lidar com situações inesperadas, como arquivos ausentes, permissões
    # inadequadas ou erros de codificação. O uso de blocos 'try' e 'except'
    # é comum para capturar e tratar exceções durante a manipulação de arquivos.


# - - - - -> Exemplo de Boas Práticas:
from pathlib import Path

ROOT_PATH = Path(__file__).parent


# - - - -> Abrindo e fechando arquivos:
try:
    with open(ROOT_PATH / "Boas Práticas.txt", "r", encoding='utf-8') as arquivo:
        # Realiza operações de leitura no arquivo
        conteudo = arquivo.read()
        print(conteudo)
except Exception as exc:
    print(f"\nExceção: {exc}")

# NOTE: Neste ponto, o arquivo já foi fechado automaticamente pelo bloco 'with'
