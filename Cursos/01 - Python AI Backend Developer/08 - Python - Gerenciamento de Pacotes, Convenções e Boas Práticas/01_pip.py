# - - - - -> Instalação de Pacotes com pip:
    #   O pip é um sistema de gerenciamento de pacotes utilizado para instalar e 
    # gerenciar bibliotecas e pacotes em Python. Com o pip, é possível instalar 
    # facilmente pacotes disponíveis no repositório Python Package Index (PyPI) 
    # ou de outros repositórios.


# - - - - -> Exemplo de Instalação de Pacotes com pip:

# - - - -> Instalação de um pacote específico:
#   Para instalar um pacote específico, basta executar o comando 'pip install' 
# seguido do nome do pacote desejado.

# Exemplo:
# pip install requests
# NOTE: Este comando instala o pacote 'requests'.


# - - - -> Instalação a partir de um arquivo requirements.txt:
#   É possível instalar múltiplos pacotes de uma vez utilizando um arquivo 
# requirements.txt. Este arquivo contém uma lista dos pacotes a serem instalados, 
# um por linha, e pode ser criado manualmente ou gerado automaticamente.

# Exemplo:
# pip install -r requirements.txt

# NOTE: Este comando instala todos os pacotes listados no arquivo requirements.txt.


# - - - -> Instalação de uma versão específica de um pacote:
#   Em algumas situações, pode ser necessário instalar uma versão específica de um 
# pacote. Isso pode ser feito especificando o nome do pacote seguido do sinal de 
# igual (=) e a versão desejada.

# Exemplo:
# pip install numpy==1.19.3
# NOTE: Este comando instala a versão 1.19.3 do pacote 'numpy'.


# - - - -> Instalação de pacotes em ambiente virtual (virtualenv):
#   Para isolar as dependências de um projeto, é comum criar ambientes virtuais 
# utilizando o virtualenv. Dentro de um ambiente virtual, as instalações de 
# pacotes são isoladas do sistema global.

# Exemplo:
# pip install virtualenv
# virtualenv myenv
# source myenv/bin/activate
# pip install requests

# NOTE: Este conjunto de comandos cria um ambiente virtual chamado 'myenv' e instala o 
# pacote 'requests' dentro dele.


# - - - -> Atualização de um pacote:
#   Para atualizar um pacote já instalado para a versão mais recente disponível, 
# basta utilizar o comando 'pip install' seguido do nome do pacote.

# Exemplo:
# pip install --upgrade requests

# NOTE: Este comando atualiza o pacote 'requests' para a versão mais recente.


# - - - -> Desinstalação de um pacote:
#   Para desinstalar um pacote, basta utilizar o comando 'pip uninstall' seguido 
# do nome do pacote.

# Exemplo:
# pip uninstall requests

# NOTE: Este comando desinstala o pacote 'requests'.


# - - - -> Listagem de pacotes instalados:
#   Para listar todos os pacotes instalados no ambiente, basta utilizar o 
# comando 'pip list'.

# Exemplo:
# pip list

# NOTE: Este comando lista todos os pacotes instalados no ambiente.
