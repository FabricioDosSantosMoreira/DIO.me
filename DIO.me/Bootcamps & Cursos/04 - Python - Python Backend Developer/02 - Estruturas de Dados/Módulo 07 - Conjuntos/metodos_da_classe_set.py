# - - - - - > Métodos da Classe 'set':

#                 Os conjuntos (sets) em Python são estruturas de dados que armazenam elementos 
#             únicos e não ordenados. Existem diversos métodos disponíveis para manipular 
#             conjuntos e realizar operações com eles.


# - - - - > Exemplos dos Métodos Úteis da Classe 'set':
print("\nExemplos dos Métodos Úteis da Classe 'set':")

# - - - > Exemplo do Método 'add()':
conjunto: set = {1, 2, 3}

conjunto.add(4)
print(f"\nExemplo do Método 'add()': {conjunto}")


# - - - > Exemplo do Método 'remove()':
conjunto: set = {1, 2, 3}

conjunto.remove(2)
print(f"\nExemplo do Método 'remove()': {conjunto}")


# - - - > Exemplo do Método 'discard()':
conjunto: set = {1, 2, 3}

conjunto.discard(2)
print(f"\nExemplo do Método 'discard()': {conjunto}")


# - - - > Exemplo do Método 'pop()':
conjunto: set = {1, 2, 3}

elemento = conjunto.pop()
print(f"\nExemplo do Método 'pop()': {elemento}")
print(f"Váriavel 'conjunto' após 'pop()': {conjunto}")


# - - - > Exemplo do Método 'clear()':
conjunto: set = {1, 2, 3}

conjunto.clear()
print(f"\nExemplo do Método 'clear()': {conjunto}")


# - - - > Exemplo do Método 'copy()':
conjunto: set = {1, 2, 3}

copia_conjunto = conjunto.copy()
print(f"\nExemplo do Método 'copy()': {copia_conjunto}")


# - - - > Exemplo do Método 'union()':
conjunto_1: set = {1, 2, 3}
conjunto_2: set = {3, 4, 5}

uniao = conjunto_1.union(conjunto_2)
print(f"\nExemplo do Método 'union()': {uniao}")


# - - - > Exemplo do Método 'intersection()':
conjunto_1: set = {1, 2, 3, 4}
conjunto_2: set = {3, 4, 5}

intersecao = conjunto_1.intersection(conjunto_2)
print(f"\nExemplo do Método 'intersection()': {intersecao}")


# - - - > Exemplo do Método 'difference()':
conjunto_1: set = {1, 2, 3, 4}
conjunto_2: set = {3, 4, 5}

diferenca = conjunto_1.difference(conjunto_2)
print(f"\nExemplo do Método 'difference()': {diferenca}")


# - - - > Exemplo do Método 'isdisjoint()':
conjunto_1: set = {1, 2, 3}
conjunto_2: set = {4, 5, 6}

is_disjoint = conjunto_1.isdisjoint(conjunto_2)
print(f"\nExemplo do Método 'isdisjoint()': {is_disjoint}")


# - - - > Exemplo do Método 'issubset()':
conjunto_1: set = {1, 2}
conjunto_2: set = {1, 2, 3, 4, 5}

is_subset = conjunto_1.issubset(conjunto_2)
print(f"\nExemplo do Método 'issubset()': {is_subset}")


# - - - > Exemplo do Método 'issuperset()':
conjunto_1: set = {1, 2, 3, 4, 5}
conjunto_2: set = {1, 2}

is_superset = conjunto_1.issuperset(conjunto_2)
print(f"\nExemplo do Método 'issuperset()': {is_superset}")
