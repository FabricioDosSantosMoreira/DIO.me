# - - - - -> Métodos da classe Tuple:

# A classe Tuple em Python possui vários métodos que permitem realizar operações com objetos do tipo tupla.

# - - -> Método: count()
# O método count() retorna o número de ocorrências de um determinado valor em uma tupla.

tupla = (1, 2, 3, 4, 1, 2, 1)
valor_ocorrencias = tupla.count(1)
print("\nMétodo count() - Número de ocorrências de 1 na tupla:", valor_ocorrencias)

# - - -> Método: index()
# O método index() retorna o índice da primeira ocorrência de um determinado valor em uma tupla.

indice_primeira_ocorrencia = tupla.index(2)
print("\nMétodo index() - Índice da primeira ocorrência de 2 na tupla:", indice_primeira_ocorrencia)

# - - -> Método: len()
# O método len() retorna o número de elementos em uma tupla.

tamanho_tupla = len(tupla)
print("\nMétodo len() - Tamanho da tupla:", tamanho_tupla)

# - - -> Método: sorted()
# O método sorted() retorna uma nova lista contendo os elementos ordenados de uma tupla.

tupla_desordenada = (3, 1, 4, 1, 5, 9, 2)
tupla_ordenada = tuple(sorted(tupla_desordenada))
print("\nMétodo sorted() - Tupla ordenada:", tupla_ordenada)

# - - -> Método: max()
# O método max() retorna o maior elemento em uma tupla.

maior_elemento = max(tupla_desordenada)
print("\nMétodo max() - Maior elemento na tupla:", maior_elemento)

# - - -> Método: min()
# O método min() retorna o menor elemento em uma tupla.

menor_elemento = min(tupla_desordenada)
print("\nMétodo min() - Menor elemento na tupla:", menor_elemento)
