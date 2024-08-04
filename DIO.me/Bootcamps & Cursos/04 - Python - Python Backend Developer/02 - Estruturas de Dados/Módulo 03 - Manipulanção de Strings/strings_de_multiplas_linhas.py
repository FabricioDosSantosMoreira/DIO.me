# - - - - - > Strings de Múltiplas Linhas:

#                 Strings de múltiplas linhas são úteis para representar blocos de texto 
#             que se estendem por várias linhas. Elas podem ser definidas usando 
#             três aspas simples (''') ou três aspas duplas (""").


# - - - - > Exemplos de Strings de Múltiplas Linhas:
print("\nExemplos de Strings de Múltiplas Linhas:")

# - - - > Exemplo de String com Três Aspas Simples ('''):
print("\nExemplo de String com Três Aspas Simples ('''):")

texto_multilinha_simples: str = '''
Esta é uma string de múltiplas linhas
que abrange várias linhas do código.
Pode incluir quebras de linha e caracteres especiais,
e é útil para representar blocos de texto extensos.
'''

print(texto_multilinha_simples)


# - - - > Exemplo de Strings com Três Aspas Duplas ("""):
print('\nExemplo de Strings com Três Aspas Duplas ("""):')

texto_multilinha_duplas: str  = """
Esta é outra string de múltiplas linhas
que também abrange várias linhas do código.
Pode incluir quebras de linha e caracteres especiais,
e é útil para representar blocos de texto extensos.
"""

print(texto_multilinha_duplas)


# - - - > Exemplo de Strings com Caracteres de Escape:
print("\nExemplo de Strings Com Caracteres de Escape Para Quebra de Linha:")

texto_multilinha_escape: str  = "Esta é uma string de múltiplas linhas\nque usa caracteres de escape\npara quebras de linha.\n"

print(texto_multilinha_escape)


# - - - > Exemplo de Strings com Parênteses: 
print("\nExemplo de Strings com Parênteses:")

texto_multilinha_parenteses: str  = (
    "Esta é uma string de múltiplas linhas "
    "que pode ser dividida em várias linhas de código "
    "usando parênteses para continuar a expressão."
)

print(texto_multilinha_parenteses)
