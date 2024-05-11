# - - - - -> Precedência de Operadores:

    # Em Python, a precedência de operadores determina a ordem na qual as operações 
    # são realizadas em uma expressão. Isso significa que certos operadores 
    # são avaliados antes de outros, seguindo uma hierarquia predefinida.

    # Aqui está a hierarquia de precedência dos operadores em Python, 
    # do mais alto para o mais baixo:

    # -> Parênteses: ()
    # -> Exponenciação: **
    # -> Operadores unários: +x, -x, not
    # -> Multiplicação, divisão, e módulo: *, /, %
    # -> Adição e subtração: +, -
    # -> Operadores de comparação: ==, !=, >, <, >=, <=, is, is not, in, not in
    # -> Operadores lógicos: and, or

    # OBS: É importante notar que, dentro da mesma precedência, os operadores 
        # são avaliados da esquerda para a direita.


# Parênteses têm a mais alta precedência, então esta expressão será avaliada primeiro
resultado = (2 + 3) * 4
print("\nResultado (2 + 3) * 4:", resultado)  

# Exponenciação tem precedência após parênteses
resultado = 2 + 3 ** 2
print("\nResultado 2 + 3 ** 2:", resultado) 

# Operadores unários têm a próxima precedência
resultado = -3 * 2 + 5
print("\nResultado -3 * 2 + 5:", resultado) 

# Multiplicação e divisão têm precedência sobre a adição e subtração
resultado = 6 + 8 / 2
print("\nResultado 6 + 8 / 2:", resultado) 

# Operadores de comparação têm precedência após operadores aritméticos
resultado = 10 > 5 + 3
print("\nResultado 10 > 5 + 3:", resultado) 

# Operadores lógicos têm a menor precedência
resultado = True or False and not True
print("\nResultado True or False and not True:", resultado) 
