# - - - - - > Conversão de Tipos de Dados:

#                 Conversão de tipos de dados é o processo de transformar um tipo de dado em outro.
#             Isso é útil para realizar operações que envolvem diferentes tipos de dados ou para 
#             garantir a compatibilidade entre eles.


# - - - - > Exemplos de Conversão de Tipos de Dados:
print("\nExemplos de Conversão de Tipos de Dados:")

# - - - > Conversão para inteiro (int):
valor_str: str = "10"
valor_int_convertido = int(valor_str)

print("\nConversão para inteiro (int):", valor_int_convertido)
print(type(valor_int_convertido))


# - - - > Conversão para ponto flutuante (float):
valor_str: str = "3.14"
valor_float_convertido = float(valor_str)

print("\nConversão para ponto flutuante (float):", valor_float_convertido)
print(type(valor_float_convertido))


# - - - > Conversão para cadeia de caracteres (string):
valor_int: int = 10
valor_str_convertido = str(valor_int)

print("\nConversão para cadeia de caracteres (string):", valor_str_convertido)
print(type(valor_str_convertido))


# - - - > Conversão para booleano (bool):
valor_int: int = 0
valor_booleano_convertido = bool(valor_int)

print("\nConversão para booleano (bool):", valor_booleano_convertido)
print(type(valor_booleano_convertido))


# - - - > Conversão para lista (list):
valor_tupla: tuple = (1, 2, 3, 4, 5)
valor_lista_convertida = list(valor_tupla)

print("\nConversão para lista (list):", valor_lista_convertida)
print(type(valor_lista_convertida))


# - - - > Conversão para tupla (tuple):
valor_lista: list = [1, 2, 3, 4, 5]
valor_tupla_convertida = tuple(valor_lista)

print("\nConversão para tupla (tuple):", valor_tupla_convertida)
print(type(valor_tupla_convertida))


# - - - > Conversão para dicionário (dict):
valor_lista_de_listas: list = [['a', 1], ['b', 2], ['c', 3]]
valor_dicionario_convertido = dict(valor_lista_de_listas)

print("\nConversão para dicionário (dict):", valor_dicionario_convertido)
print(type(valor_dicionario_convertido))


# - - - > Conversão para conjunto (set):
valor_lista: list = [1, 2, 3, 4, 5, 5]
valor_conjunto_convertido = set(valor_lista)

print("\nConversão para conjunto (set):", valor_conjunto_convertido)
print(type(valor_conjunto_convertido))


# - - - > Conversão para nulo (None):
valor_str: str = ""
valor_nulo_convertido = None if valor_str == "" else valor_str

print("\nConversão para nulo (None):", valor_nulo_convertido)
print(type(valor_nulo_convertido))


# - - - > Conversão para bytes (bytes):
valor_str: str = "Hello"
valor_bytes_convertido = bytes(valor_str, 'UTF-8')

print("\nConversão para bytes (bytes):", valor_bytes_convertido)
print(type(valor_bytes_convertido))


# - - - > Conversão para bytearray (bytearray):
valor_bytes: bytes = b'Hello'
valor_bytearray_convertido = bytearray(valor_bytes)

print("\nConversão para bytearray (bytearray):", valor_bytearray_convertido)
print(type(valor_bytearray_convertido))
