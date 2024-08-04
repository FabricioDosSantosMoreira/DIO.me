# │
# ├───────> Gerenciamento de Pacotes com 'pipenv':
# │
# │             O pipenv é uma ferramenta de gerenciamento de pacotes Python que
# │         combina as  funcionalidades do pip (para instalação de pacotes) e do 
# │         virtualenv (para criação de ambientes virtuais). Ele simplifica o 
# │         processo de gerenciamento de dependências e ambiente de desenvolvimento,  
# │         garantindo que as versões corretas dos pacotes sejam instaladas e  
# │         mantendo um controle organizado das dependências do projeto.
# │
# │
# └───┬───> Exemplos de Utilização do 'pipenv':
#     │
#     ├───> Exemplo de Instalação:
#     │         
#     │         Para instalar o pipenv, você pode usar o pip, que é o gerenciador de 
#     │     pacotes padrão do Python. Abra o terminal e execute o seguinte comando:
#     │         
#     │         * pip install pipenv
#     │         NOTE: Este comando instala o pacote 'pipenv'
#     │
#     ├───> Exemplo de Criação de um Ambiente Virtual:
#     │         
#     │         Para criar um novo ambiente virtual, navegue até o diretório do seu 
#     │     projeto e execute:
#     │         
#     │         * pipenv install
#     │         NOTE: Isso criará um ambiente virtual e um arquivo 'pipfile' que lista 
#     │         todas as dependências do seu projeto
#     │ 
#     ├───> Exemplo de Instalação de Pacotes:
#     │         
#     │         Você pode instalar pacotes Python no seu ambiente virtual usando o 
#     │     comando:
#     │         
#     │         * pipenv install requests
#     │         NOTE: Isso instalará o pacote 'requests' e atualizará automaticamente o 
#     │         arquivo 'pipfile'
#     │ 
#     ├───> Exemplo de Ativação do Ambiente Virtual:
#     │        
#     │         Para ativar o ambiente virtual, você pode usar o comando:
#     │         
#     │         * pipenv shell
#     │         NOTE: Isso ativará o ambiente virtual e você poderá trabalhar com as 
#     │         dependências instaladas no seu projeto
#     │
#     ├───> Exemplo de Desativação do Ambiente Virtual:
#     │        
#     │         Para sair do ambiente virtual, basta digitar 'exit' ou pressionar 
#     │     'Ctrl + D' no terminal.
#     │
#     ├───> Exemplo de Remoção de Pacotes:
#     │      
#     │         Para remover um pacote do ambiente virtual, use o comando:
#     │        
#     │         * pipenv uninstall requests
#     │         NOTE: Isso removerá o pacote 'requests' e atualizará o arquivo 'pipfile'
#─────┘
