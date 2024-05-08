# Os operadores de associação são utilizados para verificar se um valor está 
# presente em uma sequência (como uma lista, tupla, conjunto, ou dicionário)


# Operador "in": verifica se um elemento está presente em uma sequência.
# Retorna True se estiver presente, caso contrário, retorna False.
lista = [1, 2, 3, 4, 5]
print("3 in lista", 3 in lista)  # Saída: True
print("6 in lista", 6 in lista)  # Saída: False
print()

# Operador "not in": verifica se um elemento não está presente em uma sequência.
# Retorna True se não estiver presente, caso contrário, retorna False.
print("3 not in lista", 3 not in lista)  # Saída: False
print("6 not in lista", 6 not in lista)  # Saída: True
print()

# Usando operadores de associação em strings
texto = "Olá, mundo!"
print("""mundo" in texto""", "mundo" in texto)  # Saída: True
print("""Python" not in texto""", "Python" not in texto)  # Saída: True
print()

# Usando operadores de associação em dicionários
dicionario = {"a": 1, "b": 2, "c": 3}
print(""""a" in dicionario""", "a" in dicionario)  # Saída: True
print(""""d" not in dicionario""","d" not in dicionario)  # Saída: True
print()

# Usando operadores de associação em conjuntos
conjunto = {1, 2, 3, 4, 5}
print("3 in conjunto", 3 in conjunto)  # Saída: True
print("6 not in conjunto", 6 not in conjunto)  # Saída: True
print()

# Usando operadores de associação em tuplas
tupla = (1, 2, 3, 4, 5)
print("3 in tupla", 3 in tupla)  # Saída: True
print("6 not in tupla", 6 not in tupla)  # Saída: True
print()