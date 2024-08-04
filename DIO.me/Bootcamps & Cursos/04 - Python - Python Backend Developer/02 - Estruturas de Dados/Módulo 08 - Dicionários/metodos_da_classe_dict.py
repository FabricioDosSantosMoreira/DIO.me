# - - - - - > Métodos da Classe 'dict':

#                 Os dicionários em Python são estruturas de dados poderosas que mapeiam chaves a valores.
#             Existem diversos métodos úteis disponíveis para manipular dicionários em Python.


# - - - - > Exemplos dos Métodos Úteis da Classe 'dict':
print("\nExemplos dos Métodos Úteis da Classe 'dict':")

# - - - > Exemplo do Método 'keys()':
dicionario: dict = {'a': 1, 'b': 2, 'c': 3}

chaves = dicionario.keys()
print(f"\nExemplo do Método 'keys()': {chaves}")


# - - - > Exemplo do Método 'values()':
dicionario: dict = {'a': 1, 'b': 2, 'c': 3}

valores = dicionario.values()
print(f"\nExemplo do Método 'values()': {valores}")


# - - - > Exemplo do Método 'items()':
dicionario: dict = {'a': 1, 'b': 2, 'c': 3}

itens = dicionario.items()
print(f"\nExemplo do Método 'items()': {itens}")


# - - - > Exemplo do Método 'get()':
dicionario: dict = {'a': 1, 'b': 2, 'c': 3}

valor = dicionario.get('a', None)
print(f"\nExemplo do Método 'get()': {valor}")


# - - - > Exemplo do Método 'pop()':
dicionario: dict = {'a': 1, 'b': 2, 'c': 3}

elemento = dicionario.pop('b')
print(f"\nExemplo do Método 'pop()': {elemento}")
print(f"Váriavel 'dicionario' após 'pop()': {dicionario}")



# - - - > Exemplo do Método 'popitem()':
dicionario: dict = {'a': 1, 'b': 2, 'c': 3}

item = dicionario.popitem()
print(f"\nExemplo do Método 'popitem()': {item}")
print(f"Váriavel 'dicionario' após 'popitem()': {dicionario}")


# - - - > Exemplo do Método 'clear()':
dicionario: dict = {'a': 1, 'b': 2, 'c': 3}

dicionario.clear()
print(f"\nExemplo do Método 'clear()': {dicionario}")


# - - - > Exemplo do Método 'update()':
dicionario_1 = {'a': 1, 'b': 2}
dicionario_2 = {'b': 3, 'c': 4}

dicionario_1.update(dicionario_2)
print(f"\nExemplo do Método 'update()': {dicionario_1}")


# - - - > Exemplo do Método 'copy()':
dicionario: dict = {'a': 1, 'b': 2, 'c': 3}

copia_dicionario = dicionario.copy()
print(f"\nExemplo do Método 'copy()': {copia_dicionario}")
