# - - - - - > Variáveis e Constantes:

# - - - - > Variáveis:

#               Variáveis são espaços de memória reservados para armazenar dados manipuláveis 
#           durante a execução do programa. Elas possuem um nome que as identifica e 
#           um valor associado que pode ser modificado ao longo do programa.


# - - - - > Constantes:

#               Constantes, são valores que não podem ser alterados durante a execução do 
#           programa. No Python, não existe um tipo de dado específico para constantes, 
#           mas a convenção é que nomes de variáveis em letras maiúsculas sejam tratados 
#           como constantes, indicando que seus valores não devem ser modificados.


# - - - - > Exemplos de Variáveis e Constantes:

# - - - > Atribuição de Variáveis:

nome: str = "Fabrício"  # NOTE: Atribuição de variável do tipo 'str'
idade: int = 19         # NOTE: Atribuição de variável do tipo 'int'
altura: float = 1.90    # NOTE: Atribuição de variável do tipo 'float'

# NOTE: Atribuição de mútiplas variáveis em uma linha
nome, idade, altura = "Teste", 30, 1.60 


# - - - > Atribuição de Constantes:

# NOTE: Atribuição de constante do tipo 'list'
ESTADOS_BRASILEIROS: list = ["SP", "RJ", "SC", "RS"] 

# NOTE: Atribuição de mútiplas constantes em uma linha
EXECUTAR, VERIFICAR = True, False 
