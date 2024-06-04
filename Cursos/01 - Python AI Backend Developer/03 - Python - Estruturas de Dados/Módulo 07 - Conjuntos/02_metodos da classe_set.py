# - - - - -> Métodos da Classe Set:

# Os conjuntos (sets) em Python são estruturas de dados que armazenam elementos únicos e não ordenados.
# Existem diversos métodos disponíveis para manipular conjuntos e realizar operações com eles.

# - - -> Método: add()
conjunto = {1, 2, 3}
conjunto.add(4)
print("\nMétodo add():", conjunto)

# - - -> Método: remove()
conjunto = {1, 2, 3}
conjunto.remove(2)
print("\nMétodo remove():", conjunto)

# - - -> Método: discard()
conjunto = {1, 2, 3}
conjunto.discard(2)
print("\nMétodo discard():", conjunto)

# - - -> Método: pop()
conjunto = {1, 2, 3}
elemento_removido = conjunto.pop()
print("\nMétodo pop() - Elemento removido:", elemento_removido)
print("Conjunto após pop():", conjunto)

# - - -> Método: clear()
conjunto = {1, 2, 3}
conjunto.clear()
print("\nMétodo clear() - Conjunto após limpar:", conjunto)

# - - -> Método: copy()
conjunto_original = {1, 2, 3}
copia_conjunto = conjunto_original.copy()
print("\nMétodo copy() - Cópia do conjunto original:", copia_conjunto)

# - - -> Método: union()
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1.union(conjunto2)
print("\nMétodo union() - União de conjuntos:", uniao)

# - - -> Método: intersection()
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5}
intersecao = conjunto1.intersection(conjunto2)
print("\nMétodo intersection() - Interseção de conjuntos:", intersecao)

# - - -> Método: difference()
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5}
diferenca = conjunto1.difference(conjunto2)
print("\nMétodo difference() - Diferença entre conjuntos:", diferenca)

# - - -> Método: isdisjoint()
conjunto1 = {1, 2, 3}
conjunto2 = {4, 5, 6}
is_disjoint = conjunto1.isdisjoint(conjunto2)
print("\nMétodo isdisjoint() - Os conjuntos são disjuntos?", is_disjoint)

# - - -> Método: issubset()
conjunto1 = {1, 2}
conjunto2 = {1, 2, 3, 4, 5}
is_subset = conjunto1.issubset(conjunto2)
print("\nMétodo issubset() - O conjunto1 é um subconjunto de conjunto2?", is_subset)

# - - -> Método: issuperset()
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {1, 2}
is_superset = conjunto1.issuperset(conjunto2)
print("\nMétodo issuperset() - O conjunto1 é um superconjunto de conjunto2?", is_superset)
