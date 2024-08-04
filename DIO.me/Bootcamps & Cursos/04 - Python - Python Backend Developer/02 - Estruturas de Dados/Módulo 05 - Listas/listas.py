# - - - - - > Listas: Criação, Acesso e Modificação

#                 As listas são estruturas de dados em Python que podem armazenar uma coleção ordenada de 
#             elementos. Elas são mutáveis, o que significa que os elementos podem ser 
#             alterados, adicionados ou removidos.


# - - - - > Exemplos de Criação, Acesso e Modificação de Listas:
print("\nExemplos de Criação, Acesso e Modificação de Listas:")


# - - - > Exemplos de Criação de Listas:
print("\nExemplo de Criação de Listas:")

lista_inteiros: list = [1, 2, 3, 4, 5]
print(f"Lista de inteiros: {lista_inteiros}")

lista_strings: list = ['a', 'b', 'c', 'd', 'e', 'abcde']
print(f"Lista de strings:{lista_strings}")

lista_mista: list = [1, 'a', True, 3.14]
print(f"Lista mista: {lista_mista}")


# - - - > Exemplos de Acesso de Listas:
print("\nExemplo de Acesso de Listas:")

lista: list = [1, 2, 3, 4, 5]

primeiro_elemento = lista[0]
print(f"Primeiro elemento: {primeiro_elemento}")

ultimo_elemento = lista[-1]
print(f"Último elemento: {ultimo_elemento}")

sublista = lista[1:3]
print(f"Sublista: {sublista}")


# - - - > Exemplos de Modificação de Listas:
print("\nExemplo de Modificação de Listas:")

lista: list = [1, 2, 3, 4, 5]

lista[0] = 10
print(f"Lista após modificação: {lista}")

lista_mista: list = [1, 'a', True, 3.14]

del lista_mista[2]
print(f"Lista após remoção: {lista_mista}")
