# - - - - - > Métodos da classe 'tuple':

#                 A classe 'tuple' em Python possui vários métodos que permitem realizar 
#             operações com objetos do tipo tupla.


# - - - - > Exemplos dos Métodos Úteis da Classe 'tuple':
print("\nExemplos dos Métodos Úteis da Classe 'tuple':")

# - - - > Exemplo do Método 'count()':
tupla: tuple = (1, 2, 3, 4, 1, 2, 1)

ocorrencias = tupla.count(1)
print(f"\nExemplo do Método 'count()': {ocorrencias}")


# - - - > Exemplo do Método 'index()':
tupla: tuple = (1, 2, 3, 4, 1, 2, 1)

indice = tupla.index(2)
print(f"\nExemplo do Método 'index()': {indice}")


# - - - > Exemplo do Método 'len()':
tupla: tuple = (1, 2, 3, 4, 1, 2, 1)

tamanho = len(tupla)
print(f"\nExemplo do Método 'len()': {tamanho}")


# - - - > Exemplo do Método 'sorted()':
tupla_desordenada: tuple = (3, 1, 4, 1, 5, 9, 2)

tupla_ordenada: tuple = tuple(sorted(tupla_desordenada))
print(f"\nExemplo do Método 'sorted()': {tupla_ordenada}")


# - - - > Exemplo do Método 'max()':
tupla: tuple = (1, 2, 3, 4, 1, 2, 1)

maior_elemento = max(tupla)
print(f"\nExemplo do Método 'max()': {maior_elemento}")


# - - - > Exemplo do Método 'min()':
tupla: tuple = (1, 2, 3, 4, 1, 2, 1)

menor_elemento = min(tupla)
print(f"\nExemplo do Método 'min()': {menor_elemento}")
