# - - - - - > Operadores de Associação:
#                 Os operadores de associação são utilizados para verificar se um valor está 
#             presente em uma sequência (como uma lista, tupla, conjunto, ou dicionário).


# - - - - > Exemplos de Operadores Associação:
print("\nExemplos de Operadores Associação:")

# - - - > Operador de associação (in): 
# NOTE: Verifica se um elemento está presente em uma sequência.
#       Retorna True se estiver presente, caso contrário, retorna False.
lista: list = [1, 2, 3, 4, 5]

print("\nOperador de associação (in):")
print(f"Resultado [3 in lista]: {3 in lista}")  
print(f"Resultado [6 in lista]: {6 in lista}")  


# - - - > Operador de Associação (not in): 
# NOTE: Verifica se um elemento não está presente em uma sequência.    
#       Retorna True se não estiver presente, caso contrário, retorna False.
lista: list = [1, 2, 3, 4, 5]

print("\nOperador de associação (not in):")
print(f"Resultado [3 not in lista]: {3 not in lista}")  
print(f"Resultado [6 not in lista]: {6 not in lista}")  


# Usando operadores de associação em strings
texto: str = "Olá, mundo!"

print("\nUsando operadores de associação em strings:")
print(f"Resultado ['mundo' in texto]: {'mundo' in texto}") 
print(f"Resultado ['Python' not in texto]: {'Python' not in texto}")  


# Usando operadores de associação em dicionários
dicionario: dict = {"a": 1, "b": 2, "c": 3}

print("\nUsando operadores de associação em dicionários:")
print(f"Resultado ['a' in dicionario]: {'a' in dicionario}") 
print(f"Resultado ['d' not in dicionario]: {'d' not in dicionario}")  


# Usando operadores de associação em conjuntos
conjunto: set = {1, 2, 3, 4, 5}

print("\nUsando operadores de associação em conjuntos:")
print(f"Resultado [3 in conjunto]: {3 in conjunto}")
print(f"Resultado [6 not in conjunto]: {6 not in conjunto}")  


# Usando operadores de associação em tuplas
tupla: tuple = (1, 2, 3, 4, 5)

print("\nUsando operadores de associação em tuplas:")
print(f"Resultado [3 in tupla]: {3 in tupla}")  
print(f"Resultado [6 not in tupla]: {6 not in tupla}")  
