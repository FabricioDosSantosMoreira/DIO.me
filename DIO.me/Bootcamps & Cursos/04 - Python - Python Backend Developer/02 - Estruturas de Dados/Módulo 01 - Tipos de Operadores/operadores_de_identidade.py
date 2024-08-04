# - - - - - > Operadores de Identidade:

#                 Os operadores de identidade, is e is not, são utilizados para verificar 
#             se duas variáveis estão se referindo ao mesmo objeto na memória.


# - - - - > Exemplos de Operadores de Identidade:
print("\nExemplos de Operadores de Identidade:")

x: int = 5
y: int = 5
z: list = [1, 2, 3]
w: list = [1, 2, 3]

# - - - > Operador de identidade (is):
# NOTE: retorna True se as duas variáveis apontarem para o mesmo objeto na memória
print("\nOperador de identidade (is):")

# NOTE: 'x' e 'y' apontam para o mesmo objeto na memória, então retorna True
resultado = x is y
print(f"Resultado [x is y]: {resultado}") 

# NOTE: 'z' e 'w' são listas diferentes, mesmo que contenham os mesmos elementos, então retorna False
resultado = z is w
print(f"Resultado [z is w]: {resultado}")  


# - - - > Operador de identidade (is not):
# NOTE: retorna True se as duas variáveis não apontarem para o mesmo objeto na memória
print("\nOperador de identidade (is not):")

# NOTE: 'x' e 'y' apontam para o mesmo objeto na memória, então retorna False
resultado = x is not y
print(f"Resultado [x is not y]: {resultado}")  

# NOTE: 'z' e 'w' são listas diferentes, mesmo que contenham os mesmos elementos, então retorna True
resultado = z is not w
print(f"Resultado [z is not w]: {resultado}")  


# Alterando 'w' para que aponte para o mesmo objeto que 'z'
print("\nDepois de alterar w para apontar para o mesmo objeto que z:")

w = z

# NOTE: Agora 'z' e 'w' apontam para o mesmo objeto, então retorna True
resultado = z is w
print(f"Resultado [z is w]: {resultado}") 
