# - - - - - > Dicionários: Criação, Acesso e Modificação

#                 Os dicionários são estruturas de dados em Python que armazenam 
#             pares de chave-valor. Eles são úteis para mapear um conjunto 
#             de chaves a um conjunto de valores correspondentes.


# - - - - > Exemplos de Criação, Acesso e Modificação de Dicionários:
print("\nExemplos de Criação, Acesso e Modificação de Dicionários:")


# - - - > Exemplos de Criação de Dicionários:
print(f"\nExemplos de Criação de Dicionários:")

dicionario_inteiros: dict = {1: 1, 2: 2, 3: 3}
print(f"Dicionário de inteiros: {dicionario_inteiros}")

dicionario_strings: dict = {'nome': "João", 'idade': "30", 'cidade': "São Paulo"}
print(f"Dicionário de strings: {dicionario_strings}")

dicionario_misto: dict = {'inteiro': 1, 'letra': "a", 'booleano': True, "float": 3.14}
print(f"Dicionário misto: {dicionario_misto}")


# - - - > Exemplos de Acesso de Dicionários:
print(f"\nExemplo de Acesso de Dicionários:")

dicionario: dict = {'nome': "João", 'idade': "30", 'cidade': "São Paulo"}

elemento = dicionario['nome']
print(f"Elemento na chave 'nome': {elemento}")

elemento = dicionario['idade']
print(f"Elemento na chave 'idade': {elemento}")

elemento = dicionario['cidade']
print(f"Elemento na chave 'cidade': {elemento}")


# - - - > Exemplos de Modificação de Dicionários:
print("\nExemplo de Modificação de Dicionários:")

dicionario: dict = {'nome': "João", 'idade': "30", 'cidade': "São Paulo"}

dicionario['idade'] = 35
print(f"Dicionário após modificação: {dicionario}")

dicionario['profissao'] = 'Engenheiro'
print(f"Dicionário após modificação: {dicionario}")

del dicionario['cidade']
print(f"Dicionário após remoção: {dicionario}")
