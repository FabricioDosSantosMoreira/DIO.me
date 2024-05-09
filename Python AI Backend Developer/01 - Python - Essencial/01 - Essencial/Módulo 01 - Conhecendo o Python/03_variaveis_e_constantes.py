# - - - - -> Variáveis e Constantes:

# - - - -> Variáveis:

    # Variáveis são espaços de memória reservados para armazenar dados manipuláveis 
    # durante a execução do programa. Elas possuem um nome que as identifica e 
    # um valor associado que pode ser modificado ao longo do programa.

# - - - -> Constantes:

    # Constantes, são valores que não podem ser alterados durante a execução do programa. 
    # No Python, não existe um tipo de dado específico para constantes, mas a convenção 
    # é que nomes de variáveis em letras maiúsculas sejam tratados como constantes, 
    # indicando que seus valores não devem ser modificados.


nome: str = "Fabrício"  # Atribuição de variável do tipo str
idade: int = 19 # Atribuição de variável do tipo int
altura: float = 1.90 # Atribuição de variável do tipo float

print(nome, idade, altura)

nome, idade, altura = "Teste", 30, 1.60 # Atribuição de mútiplas variáveis em uma linha

print(nome, idade, altura)


ESTADOS_BRASILEIROS: list = ["SP", "RJ", "SC", "RS"] # Atribuição de constante do tipo list

EXECUTAR, VERIFICAR = True, False # Atribuição de mútiplas constantes em uma linha

print(ESTADOS_BRASILEIROS)

print(EXECUTAR)

print(VERIFICAR)
