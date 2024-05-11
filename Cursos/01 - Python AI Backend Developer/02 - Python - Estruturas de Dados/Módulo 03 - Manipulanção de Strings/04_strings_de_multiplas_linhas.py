# - - - - -> Strings de Múltiplas Linhas:

    # Strings de múltiplas linhas são úteis para representar blocos de texto 
    # que se estendem por várias linhas. Elas podem ser definidas usando 
    # três aspas simples (''') ou três aspas duplas (""").


# - - - -> Strings de Múltiplas Linhas:

# - - -> Exemplo de Strings de Múltiplas Linhas com três aspas simples ('''):
texto_multilinha_simples = '''
Esta é uma string de múltiplas linhas
que abrange várias linhas do código.
Pode incluir quebras de linha e caracteres especiais,
e é útil para representar blocos de texto extensos.
'''

print("\nExemplo de strings de múltiplas linhas com três aspas simples ('''):")
print(texto_multilinha_simples)


# - - -> Exemplo de Strings de Múltiplas Linhas com três aspas duplas ("""):
texto_multilinha_duplas = """
Esta é outra string de múltiplas linhas
que também abrange várias linhas do código.
Pode incluir quebras de linha e caracteres especiais,
e é útil para representar blocos de texto extensos.
"""

print('\nExemplo de strings de múltiplas linhas com três aspas duplas ("""):')
print(texto_multilinha_duplas)


# - - -> Exemplo de Strings de Múltiplas Linhas com caracteres de escape para quebra de linha:
texto_multilinha_escape = "Esta é uma string de múltiplas linhas\nque usa caracteres de escape\npara quebras de linha.\n"

print("\nExemplo de strings de múltiplas linhas com caracteres de escape para quebra de linha:")
print(texto_multilinha_escape)


# - - -> Exemplo de Strings de Múltiplas Linhas com parênteses para continuar em várias linhas de código:
texto_multilinha_parenteses = (
    "Esta é uma string de múltiplas linhas "
    "que pode ser dividida em várias linhas de código "
    "usando parênteses para continuar a expressão."
)

print("\nExemplo de strings de múltiplas linhas com parênteses para continuar em várias linhas de código:")
print(texto_multilinha_parenteses)
