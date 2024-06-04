# - - - - -> Tuplas: Criação, Acesso e Modificação

    # As tuplas são estruturas de dados semelhantes a listas, mas imutáveis, o que significa que não podem ser alteradas após a criação.
    # Elas são criadas usando parênteses () e podem conter elementos de diferentes tipos de dados.

# - - -> Criação de Tupla:
tupla = (1, 2, 3, 4, 5)
print("\nCriação de Tupla:", tupla)
print(type(tupla))

# - - -> Acesso a elementos da Tupla:
primeiro_elemento = tupla[0]
ultimo_elemento = tupla[-1]
print("\nAcesso a elementos da Tupla:")
print("Primeiro elemento:", primeiro_elemento)
print("Último elemento:", ultimo_elemento)

# - - -> Tentativa de modificação da Tupla (imutabilidade):
try:
    tupla[0] = 10  # Isso resultará em um erro, pois as tuplas são imutáveis
except TypeError as e:
    print("\nErro ao modificar a Tupla:", e)

# - - -> Concatenação de Tuplas:
outra_tupla = (6, 7, 8, 9, 10)
tupla_concatenada = tupla + outra_tupla
print("\nConcatenação de Tuplas:", tupla_concatenada)

# - - -> Desempacotamento de Tuplas:
primeiro, segundo, *restante = tupla
print("\nDesempacotamento de Tuplas:")
print("Primeiro elemento:", primeiro)
print("Segundo elemento:", segundo)
print("Restante da Tupla:", restante)
