# - - - - -> Conjuntos: Criação, Acesso e Modificação

# Conjuntos (sets) são coleções não ordenadas de elementos únicos.
# Eles são úteis para realizar operações como união, interseção e diferença entre conjuntos.

# - - -> Criação de um conjunto:
conjunto = {1, 2, 3, 4, 5}
print("\nCriação de um conjunto:", conjunto)
print(type(conjunto))

# - - -> Acesso a elementos de um conjunto:
# Como conjuntos não são ordenados, não é possível acessar elementos por índice.
# No entanto, pode-se verificar a existência de um elemento utilizando operadores de pertencimento.
elemento = 3
if elemento in conjunto:
    print("\nO elemento", elemento, "pertence ao conjunto.")
else:
    print("\nO elemento", elemento, "não pertence ao conjunto.")

# - - -> Modificação de um conjunto:
# Adicionando elementos:
conjunto.add(6)
print("\nAdicionando um elemento ao conjunto:", conjunto)

# Removendo elementos:
conjunto.remove(3)
print("\nRemovendo um elemento do conjunto:", conjunto)

# Lembre-se de que os conjuntos não permitem elementos duplicados, então adicionar um elemento já existente não terá efeito:
conjunto.add(6)
print("\nAdicionando um elemento já existente ao conjunto:", conjunto)

# Para adicionar vários elementos de uma vez, pode-se usar o método update():
conjunto.update({7, 8, 9})
print("\nAdicionando múltiplos elementos ao conjunto:", conjunto)

# - - -> Observação:
# Como os conjuntos são coleções não ordenadas, não é possível acessar elementos por índice.
# Além disso, os elementos de um conjunto não são indexados, portanto, não é possível modificar elementos individuais diretamente.

