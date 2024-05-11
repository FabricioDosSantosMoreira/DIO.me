# - - - - -> Conversão de Tipos de Dados:

    #   Conversão de tipos de dados é o processo de transformar um tipo de dado em outro.
    # Isso é útil para realizar operações que envolvem diferentes tipos de dados ou 
    # para garantir a compatibilidade entre eles.


    # - - - -> Conversão para Inteiro (int):
valor_str = "10"
valor_int_convertido = int(valor_str)
print("\nConversão para Inteiro (int):", valor_int_convertido)
print(type(valor_int_convertido))

    # - - - -> Conversão para Ponto Flutuante (float):
valor_str = "3.14"
valor_float_convertido = float(valor_str)
print("\nConversão para Ponto Flutuante (float):", valor_float_convertido)
print(type(valor_float_convertido))

    # - - - -> Conversão para Cadeia de Caracteres (string):
valor_int = 10
valor_str_convertido = str(valor_int)
print("\nConversão para Cadeia de Caracteres (string):", valor_str_convertido)
print(type(valor_str_convertido))

    # - - - -> Conversão para Booleano (bool):
valor_int = 0
valor_booleano_convertido = bool(valor_int)
print("\nConversão para Booleano (bool):", valor_booleano_convertido)
print(type(valor_booleano_convertido))

    # - - - -> Conversão para Lista (list):
valor_tupla = (1, 2, 3, 4, 5)
valor_lista_convertida = list(valor_tupla)
print("\nConversão para Lista (list):", valor_lista_convertida)
print(type(valor_lista_convertida))

    # - - - -> Conversão para Tupla (tuple):
valor_lista = [1, 2, 3, 4, 5]
valor_tupla_convertida = tuple(valor_lista)
print("\nConversão para Tupla (tuple):", valor_tupla_convertida)
print(type(valor_tupla_convertida))

    # - - - -> Conversão para Dicionário (dictionary):
valor_lista_de_listas = [['a', 1], ['b', 2], ['c', 3]]
valor_dicionario_convertido = dict(valor_lista_de_listas)
print("\nConversão para Dicionário (dictionary):", valor_dicionario_convertido)
print(type(valor_dicionario_convertido))

    # - - - -> Conversão para Conjunto (set):
valor_lista = [1, 2, 3, 4, 5, 5]
valor_conjunto_convertido = set(valor_lista)
print("\nConversão para Conjunto (set):", valor_conjunto_convertido)
print(type(valor_conjunto_convertido))

    # - - - -> Conversão para nulo (None):
valor_str = ""
valor_nulo_convertido = None if valor_str == "" else valor_str
print("\nConversão para Nulo (None):", valor_nulo_convertido)
print(type(valor_nulo_convertido))

    # - - - -> Conversão para Bytes (bytes):
valor_str = "Hello"
valor_bytes_convertido = bytes(valor_str, 'utf-8')
print("\nConversão para Bytes (bytes):", valor_bytes_convertido)
print(type(valor_bytes_convertido))

    # - - - -> Conversão para Bytearray (bytearray):
valor_bytes = b'Hello'
valor_bytearray_convertido = bytearray(valor_bytes)
print("\nConversão para Bytearray (bytearray):", valor_bytearray_convertido)
print(type(valor_bytearray_convertido))
