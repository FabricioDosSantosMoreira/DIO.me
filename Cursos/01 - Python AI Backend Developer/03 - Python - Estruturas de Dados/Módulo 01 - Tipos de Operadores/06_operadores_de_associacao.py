# - - - - -> Operadores de Associação:

    # Os operadores de associação são utilizados para verificar se um valor está 
    # presente em uma sequência (como uma lista, tupla, conjunto, ou dicionário)


# Operador de Associação 'in': 
# OBS: verifica se um elemento está presente em uma sequência.
    # Retorna True se estiver presente, caso contrário, retorna False.

lista = [1, 2, 3, 4, 5]

print("\nOperador de associação 'in':")
print("3 in lista", 3 in lista)  
print("6 in lista", 6 in lista)  
print()


# Operador de Associação 'not in': 
# OBS: verifica se um elemento não está presente em uma sequência.    
    # Retorna True se não estiver presente, caso contrário, retorna False.

lista = [1, 2, 3, 4, 5]

print("\nOperador de associação 'not in':")
print("3 not in lista", 3 not in lista)  
print("6 not in lista", 6 not in lista)  
print()


# Usando operadores de associação em strings
texto = "Olá, mundo!"

print("\nUsando operadores de associação em strings:")
print(f"mundo in texto: {'mundo' in texto}") 
print(f"Python not in texto: {'Python' not in texto}")  
print()


# Usando operadores de associação em dicionários
dicionario = {"a": 1, "b": 2, "c": 3}

print("\nUsando operadores de associação em dicionários:")
print(f"'a' in dicionario: {'a' in dicionario}") 
print(f"'d' not in dicionario: {'d' not in dicionario}")  
print()


# Usando operadores de associação em conjuntos
conjunto = {1, 2, 3, 4, 5}

print("\nUsando operadores de associação em conjuntos:")
print(f"3 in conjunto: {3 in conjunto}")
print(f"6 not in conjunto: {6 not in conjunto}")  
print()


# Usando operadores de associação em tuplas
tupla = (1, 2, 3, 4, 5)

print("\nUsando operadores de associação em tuplas:")
print(f"3 in tupla: {3 in tupla}")  
print(f"6 not in tupla: {6 not in tupla}")  
print()
