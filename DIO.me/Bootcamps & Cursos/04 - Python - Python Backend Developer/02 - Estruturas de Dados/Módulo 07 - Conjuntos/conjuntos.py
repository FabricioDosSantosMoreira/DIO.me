# - - - - - > Conjuntos: Criação, Acesso e Modificação

#                 Os conjuntos ou sets são coleções não ordenadas de elementos únicos.
#             Como os conjuntos são coleções não ordenadas, não é possível acessar 
#             elementos por índice. Além disso, os elementos de um conjunto não 
#             são indexados, portanto, não é possível modificar elementos individuais 
#             diretamente. Eles são úteis para realizar operações como união, 
#             interseção e diferença entre conjuntos.


# - - - - > Exemplos de Criação, Acesso e Modificação de Conjuntos:
print("\nExemplos de Criação, Acesso e Modificação de Conjuntos:")


# - - - > Exemplos de Criação de Conjuntos:
print(f"\nExemplos de Criação de Conjuntos:")

conjunto_inteiros: set = {1, 2, 3, 4, 5}
print(f"Conjunto de inteiros: {conjunto_inteiros}")

conjunto_strings: set = {'a', 'b', 'c', 'd', 'e', 'abcde'}
print(f"Conjunto de strings: {conjunto_strings}")

conjunto_misto: set = {1, 'a', True, 3.14}
print(f"Conjunto misto: {conjunto_misto}")


# - - - > Exemplo de Acesso de Conjuntos:
print(f"\nExemplo de Acesso de Conjuntos:")

conjunto: set = {1, 2, 3, 4, 5}

# NOTE: Como conjuntos não são ordenados, não é possível acessar elementos por índice.
# No entanto, pode-se verificar a existência de um elemento utilizando operadores de pertencimento.
elemento: int = 3

if elemento in conjunto:
    print(f"O elemento {elemento} pertence ao conjunto")
else:
    print(f"O elemento {elemento} não pertence ao conjunto")




# - - - > Exemplos de Modificação de Conjuntos:
print("\nExemplo de Modificação de Conjuntos:")

conjunto: set = {1, 2, 3, 4, 5}

conjunto.add(6)
print(f"Conjunto após modificação: {conjunto}")

# NOTE: Lembre-se de que os conjuntos não permitem elementos duplicados, 
# então adicionar um elemento já existente não terá efeito
conjunto.add(6)
print(f"Conjunto após modificação: {conjunto}")

conjunto.update({7, 8, 9})
print(f"Conjunto após modificação: {conjunto}")

conjunto.remove(3)
print(f"Conjunto após remoção: {conjunto}")
