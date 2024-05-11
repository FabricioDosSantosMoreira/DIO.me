# - - - - -> Geradores:

    #   Geradores são funções que produzem uma sequência de resultados em vez de um 
    # único valor. Eles são especialmente úteis para gerar grandes volumes de dados 
    # que não precisam ser armazenados na memória ao mesmo tempo.


# - - - - -> Exemplo de Geradores:

# - - - -> Função Geradora:
def gerar_numeros(n):
    for i in range(n):
        yield i


# - - - -> Utilização do Gerador:
gerador = gerar_numeros(5)
print("\nUtilização do Gerador:")
for numero in gerador:
    print(f"\t{numero}")
