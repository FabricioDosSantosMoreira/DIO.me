# - - - - - > Geradores:
#                 Geradores são funções que produzem uma sequência de resultados em vez de um 
#             único valor. Eles são especialmente úteis para gerar grandes volumes de dados 
#             que não precisam ser armazenados na memória ao mesmo tempo.


# - - - - > Exemplo de Geradores:
print("\nExemplo de Geradores:")

from typing import Generator

# - - - > Criando um Gerador:
def gerar_numeros(n: int) -> Generator[int, None, None]:
    for i in range(n):

        # NOTE: Cada vez que yield é chamado, a função retorna o próximo valor na sequência e 
        # suspende sua execução até que o próximo valor seja solicitado.
        yield i


# - - - > Usando o Gerador:
print("\nUsando o Gerador:")

gerador: Generator[int, ]  = gerar_numeros(10)

for n in gerador:
    print(f"Número: {n}")

for n in gerar_numeros(5):
    print(f"Número: {n}")
