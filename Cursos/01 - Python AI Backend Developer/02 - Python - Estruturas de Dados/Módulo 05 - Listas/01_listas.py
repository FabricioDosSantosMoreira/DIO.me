# - - - - -> Listas: Criação, Acesso e Modificação

    # As listas são estruturas de dados em Python que podem armazenar uma coleção ordenada de elementos.
    # Elas são mutáveis, o que significa que os elementos podem ser alterados, adicionados ou removidos.


# - - - -> Criação de Listas:
print("\nCriação de Listas:")

lista_numeros = [1, 2, 3, 4, 5]
print("\nLista de números:", lista_numeros)

lista_strings = ['a', 'b', 'c', 'd', 'e', 'abcde']
print("\nLista de strings:", lista_strings)

lista_mista = [1, 'a', True, 3.14]
print("\nLista mista:", lista_mista)


# - - - -> Acesso de Listas:
print("\nAcesso de Listas:")

primeiro_elemento = lista_numeros[0]
print("\nPrimeiro elemento da lista de números:", primeiro_elemento)

ultimo_elemento = lista_strings[-1]
print("\nÚltimo elemento da lista de strings:", ultimo_elemento)

sublista = lista_mista[1:3]
print("\nSublista da lista mista:", sublista)


# - - - -> Modificação de Listas:
lista_numeros[0] = 10
print("\nLista de números após modificação:", lista_numeros)

del lista_mista[2]
print("\nLista mista após remoção:", lista_mista)
