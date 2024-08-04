# - - - - - > Métodos da Classe 'list':

#                 Os métodos da classe 'list' são funções incorporadas que podem ser usadas para 
#             modificar e manipular listas em Python.


# - - - - > Exemplos dos Métodos Úteis da Classe 'list':
print("\nExemplos dos Métodos Úteis da Classe 'list':")

# - - - > Exemplo do Método 'append()':
lista: list = [1, 2, 3]

lista.append(4)
print(f"\nExemplo do Método 'append()' {lista}")


# - - - > Exemplo do Método 'extend()':
lista_1: list = [1, 2, 3]
lista_2: list = [4, 5, 6]

lista_1.extend(lista_2)
print(f"\nExemplo do Método 'extend()':", lista_1)


# - - - > Exemplo do Método 'insert()':
lista: list = [1, 2, 3]

lista.insert(1, 5)
print(f"\nExemplo do Método 'insert()': {lista}")


# - - - > Exemplo do Método 'remove()':
lista: list = [1, 2, 3, 4, 3]

lista.remove(3)
print(f"\nExemplo do Método 'remove()': {lista}")


# - - - > Exemplo do Método 'pop()':
lista: list = [1, 2, 3]

elemento_removido = lista.pop()
print(f"\nExemplo do Método 'pop()': {elemento_removido}")
print(f"Váriavel 'lista' após 'pop()': {lista}")


# - - - > Exemplo do Método 'clear()':
lista: list = [1, 2, 3]

lista.clear()
print(f"\nExemplo do Método 'clear()': {lista}")


# - - - > Exemplo do Método 'index()':
lista: list = [1, 2, 3, 4]

elemento = lista.index(3)
print(f"\nExemplo do Método 'index()': {elemento}")


# - - - > Exemplo do Método 'count()':
lista: list = [1, 2, 3, 3, 4, 3]

ocorrencias = lista.count(3)
print(f"\nExemplo do Método 'count()': {ocorrencias}")


# - - - > Exemplo do Método 'sort()':
lista: list = [3, 2, 1, 4]

lista.sort()
print(f"\nExemplo do Método 'sort()': {lista}")


# - - - > Exemplo do Método 'reverse()':
lista: list = [1, 2, 3, 4]

lista.reverse()
print(f"\nExemplo do Método 'reverse()': {lista}")


# - - - > Exemplo do Método 'copy()':
lista: list = [1, 2, 3]

copia_lista = lista.copy()
print(f"\nExemplo do Método 'copy()': {copia_lista}")
