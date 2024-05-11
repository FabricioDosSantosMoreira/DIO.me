# - - - - -> Fatiamento de Strings:

    # Fatiamento ou Slicing de strings é o processo de extrair partes específicas 
    # de uma string. É feito especificando um intervalo de índices, permitindo 
    # acessar substrings da string original.

    # OBS: Quando for fazer um fatiamento informe: [start: stop: step]
    #       - Início (start);
    #       - Fim (stop);
    #       - Passo (step).


# - - - -> Fatiamento de Strings:
texto = "Python é uma linguagem de programação"

# - - -> Exemplo de Fatiamento de Strings simples:
substring = texto[7:18]  # Fatiando do índice 7 até o índice 17(18 - 1)
print("\nExemplo de fatiamento de strings simples:", substring)


# - - -> Exemplo de Fatiamento de Strings com índices negativos:
substring = texto[-8:-1]  # Fatiando do 8º caractere do final até o 2º caractere do final
print("\nExemplo de fatiamento com índices negativos:", substring)

# - - -> Exemplo de Fatiamento com passo:
substring = texto[::2]  # Fatiando com um passo de 2
print("\nExemplo de fatiamento com passo:", substring)

# - - -> Exemplo de Fatiamento invertido:
substring = texto[::-1]  # Fatiando de trás para frente
print("\nExemplo de fatiamento invertido:", substring)
