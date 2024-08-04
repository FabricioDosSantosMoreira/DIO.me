# - - - - - > Tuplas: Criação, Acesso e Modificação

#                 As tuplas são estruturas de dados semelhantes a listas, mas imutáveis, o que significa 
#             que não podem ser alteradas após a criação. Elas são criadas usando parênteses '()' e 
#             podem conter elementos de diferentes tipos de dados.


# - - - - > Exemplos de Criação, Acesso e Modificação de Tuplas:
print("\nExemplos de Criação, Acesso e Modificação de Tuplas:")

# - - - > Exemplos de Criação de Tuplas:
print(f"\nExemplos de Criação de Tuplas:")

tupla_inteiros: tuple = (1, 2, 3, 4, 5)
print(f"Tupla de inteiros: {tupla_inteiros}")

tupla_strings: tuple = ('a', 'b', 'c', 'd', 'e', 'abcde')
print(f"Tupla de strings: {tupla_strings}")

tupla_mista: tuple = (1, 'a', True, 3.14)
print(f"Tupla mista: {tupla_mista}")


# - - - > Exemplos de Acesso de Tuplas:
print("\nExemplos de Acesso de Tuplas:")

tupla: tuple = (1, 2, 3, 4, 5)

primeiro_elemento = tupla[0]
print(f"Primeiro elemento: {primeiro_elemento}")

ultimo_elemento = tupla[-1]
print(f"Último elemento: {ultimo_elemento}")

subtupla = tupla[1:3]
print(f"Subtupla: {subtupla}")

# - - - > Exemplo de Tentativa de Modificação da Tupla (imutabilidade):
print("\nExemplo de Tentativa de Modificação da Tupla (imutabilidade):")

try:
    tupla[0] = 10 # NOTE: Isso resultará em um erro, pois as tuplas são imutáveis
except TypeError as e:
    print("Erro ao Modificar a Tupla:", e)


# - - - > Exemplo de Desempacotamento de Tuplas:
print("\nExemplo de Desempacotamento de Tuplas:")

primeiro, segundo, *restante = tupla

print(f"Primeiro elemento: {primeiro}")
print(f"Segundo elemento: {segundo}")
print(f"Restante da Tupla: {restante}")
