# - - - - -> Ordenação de imports com isort:

# - - - - -> Introdução:
    #   A ordenação de imports é uma prática comum em projetos Python para manter 
    # a consistência e legibilidade do código. O `isort` é uma ferramenta que 
    # automatiza esse processo, organizando os imports de acordo com convenções 
    # estabelecidas.

# - - - - -> Instalação do isort:
    #   Antes de utilizar o `isort`, é necessário instalá-lo. Isso pode ser feito 
    # facilmente via pip, o gerenciador de pacotes do Python, utilizando o 
    # seguinte comando no terminal:
    #
    #   pip install isort

# - - - - -> Uso do isort:
    #   Para ordenar os imports de um arquivo Python, basta executar o `isort` 
    # seguido do caminho para o arquivo. Por exemplo:
    #
    #   isort arquivo.py
    #
    # O `isort` irá reorganizar os imports no arquivo `arquivo.py` de acordo 
    # com as configurações definidas.

# - - - - -> Exemplo de uso do isort:

# - - - -> Antes da ordenação:
import os
import sys
import datetime

# - - - -> Após a ordenação com isort:
import datetime
import os
import sys
