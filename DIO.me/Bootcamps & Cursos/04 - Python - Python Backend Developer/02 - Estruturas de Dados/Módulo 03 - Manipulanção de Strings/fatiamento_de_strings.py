# - - - - - > Fatiamento de Strings:

#                 Fatiamento ou Slicing de strings é o processo de extrair partes específicas 
#             de uma string. É feito especificando um intervalo de índices, permitindo 
#             acessar substrings da string original.

#             NOTE: Quando for fazer um fatiamento informe: [start: stop: step]
#                       - Início (start);
#                       - Fim (stop);
#                       - Passo (step).


# - - - - > Exemplos de Fatiamento de Strings:
print("\nExemplos de Fatiamento de Strings:")

texto: str = "Python é uma linguagem de programação"

# - - - > Exemplo de Fatiamento de Strings Simples:
substring = texto[7:18] # NOTE: Fatiando do índice 7 até o índice 17(18 - 1)

print(f"\nExemplo de Fatiamento de Strings Simples: {substring}")


# - - - > Exemplo de Fatiamento de Strings com Índices Negativos:
substring = texto[-8:-1] # NOTE: Fatiando do 8º caractere do final até o 2º caractere do final

print(f"\nExemplo de Fatiamento de Strings com Índices Negativos: {substring}")


# - - - > Exemplo de Fatiamento com Passo:
substring = texto[::2] # NOTE: Fatiando com um passo de 2

print(f"\nExemplo de Fatiamento com Passo: {substring}")


# - - - > Exemplo de Fatiamento Invertido:
substring = texto[::-1] # NOTE: Fatiando de trás para frente

print(f"\nExemplo de Fatiamento Invertido: {substring}")
