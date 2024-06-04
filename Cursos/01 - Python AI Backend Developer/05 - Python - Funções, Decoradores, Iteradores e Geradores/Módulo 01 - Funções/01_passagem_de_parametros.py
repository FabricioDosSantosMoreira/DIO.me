# - - - - -> Funções: Passagem de Parâmetros

    #   As funções em Python podem receber zero ou mais parâmetros. A passagem de parâmetros 
    # permite que valores sejam transmitidos para uma função, onde podem ser processados e 
    # retornados, se necessário. Existem diferentes formas de passagem de parâmetros, 
    # incluindo passagem por valor e passagem por referência.

 
# - - - - -> Exemplo de passagem de parâmetros:

# - - - -> Passagem por valor:
def duplicar_valor(numero):
    return numero * 2

numero = 5
resultado = duplicar_valor(numero)
print("\nPassagem por valor:")
print(f"Número original: {numero}")
print(f"Resultado: {resultado}")


# - - - -> Passagem por Referência:
def modificar_lista(lista):
    lista.append(4)

lista = [1, 2, 3]
modificar_lista(lista)
print("\nPassagem por referência:")
print(f"Lista original: {lista}")
