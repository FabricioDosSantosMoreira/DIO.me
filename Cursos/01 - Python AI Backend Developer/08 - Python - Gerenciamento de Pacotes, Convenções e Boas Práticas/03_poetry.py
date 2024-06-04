# - - - - -> poetry:

    #   Poetry é uma ferramenta de gerenciamento de dependências e empacotamento 
    # para projetos em Python. Ele visa simplificar e facilitar o processo de 
    # desenvolvimento, distribuição e publicação de pacotes Python.


# - - - - -> Instalação do poetry:

    #   Para instalar o poetry, você pode usar o comando pip no terminal:

    #   pip install poetry


# - - - - -> Uso do poetry:

    #   Após a instalação, você pode criar um novo projeto com poetry usando o comando:

    #   poetry new nome_do_projeto

    #   Isso criará uma estrutura básica para o projeto, incluindo arquivos de 
    # configuração pyproject.toml e um diretório para o código-fonte.

    #   Em seguida, você pode adicionar dependências ao seu projeto usando o comando:

    #   poetry add nome_da_dependencia

    #   Isso adicionará a dependência ao arquivo pyproject.toml e instalará a 
    # dependência no ambiente virtual do projeto.

    #   Você pode também adicionar dependências de desenvolvimento usando o comando:

    #   poetry add --dev nome_da_dependencia

    #   Isso adicionará a dependência como uma dependência de desenvolvimento.

    #   Para instalar todas as dependências do projeto, você pode executar:

    #   poetry install

    #   Isso instalará todas as dependências listadas no arquivo pyproject.toml.

    #   Para executar um script ou comando dentro do ambiente virtual do poetry, 
    # você pode usar o comando run:

    #   poetry run nome_do_comando

    #   Isso garante que o comando seja executado dentro do contexto do ambiente 
    # virtual do projeto.

    #   Para publicar um pacote no PyPI usando poetry, você pode usar o comando:

    #   poetry publish --build

    #   Isso construirá o pacote e o publicará no PyPI.

    #   Essas são apenas algumas das funcionalidades básicas do poetry. Ele 
    # oferece muitos recursos adicionais para gerenciar projetos Python de 
    # forma eficaz e eficiente.


# - - - - -> Exemplo de uso do poetry:

    #   Aqui está um exemplo simples de como usar o poetry para criar e gerenciar 
    # um projeto Python:

    #   poetry new my_project
    #   cd my_project
    #   poetry add requests
    #   poetry add --dev pytest
    #   poetry install
    #   poetry run python my_script.py
    #   poetry publish --build

    #   Este exemplo cria um novo projeto chamado "my_project", adiciona a 
    # dependência "requests" e a dependência de desenvolvimento "pytest", 
    # instala todas as dependências, executa um script Python dentro do ambiente 
    # virtual do poetry e publica o pacote no PyPI.

