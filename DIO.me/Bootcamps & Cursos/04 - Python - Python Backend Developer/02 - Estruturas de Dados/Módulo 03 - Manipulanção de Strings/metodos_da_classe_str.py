# - - - - - > Métodos Úteis da Classe 'str':

#                 Os métodos úteis da classe 'str' são funções incorporadas que podem ser chamadas em 
#             objetos do tipo str para realizar várias operações de manipulação de strings.


# - - - - > Exemplos dos Métodos Úteis da Classe 'str':
print("\nExemplos dos Métodos Úteis da Classe 'str':")

# - - - > Exemplo do Método 'upper()':
string: str = "olá, mundo!"

string_upper = string.upper()
print(f"\nExemplo do Método 'upper()': {string_upper}")


# - - - > Exemplo do Método 'lower()':
string: str = "olá, mundo!"

string_lower = string.lower()
print(f"\nExemplo do Método 'lower()': {string_lower}")


# - - - -> Exemplo do Método 'capitalize()':
string: str = "olá, mundo!"

string_capitalize = string.capitalize()
print(f"\nExemplo do Método 'capitalize()': {string_capitalize}")


# - - - > Exemplo do Método 'title()':
string: str = "olá, mundo!"

string_title = string.title()
print(f"\nExemplo do Método 'title()': {string_title}")


# - - - > Exemplo do Método 'split()':
string: str = "olá, mundo!"

string_split = string.split(',')
print(f"\nExemplo do Método 'split()': {string_split}")


# - - - > Exemplo do Método 'strip()':
string: str = "olá, mundo!"

string_strip = string.strip('o')
print(f"\nExemplo do Método 'strip()': {string_strip}")


# - - - > Exemplo do Método 'replace()':
string: str = "olá, mundo!"

string_replace = string.replace('mundo', 'Python')
print(f"\nExemplo do Método 'replace()': {string_replace}")


# - - - > Exemplo do Método 'find()':
string: str = "olá, mundo!"

indice = string.find('á')
print(f"\nExemplo do Método 'find()': {indice}")


# - - - > Exemplo do Método 'count()':
string: str = "olá, mundo!"

ocorrencias = string.count('o')
print(f"\nExemplo do Método 'count()': {ocorrencias}")


# - - - > Exemplo do Método 'startswith()':
string: str = "olá, mundo!"

comeca_com = string.startswith('olá')
print(f"\nExemplo do Método 'startswith()': {comeca_com}")


# - - - > Exemplo do Método 'endswith()':
string: str = "olá, mundo!"

termina_com = string.endswith('!')
print(f"\nExemplo do Método 'endswith()': {termina_com}")


# - - - > Exemplo do Método 'isalnum()':
string: str = "olá, mundo!"

is_alnum = string.isalnum()
print(f"\nExemplo do Método 'isalnum()': {is_alnum}")


# - - - > Exemplo do Método 'isalpha()':
string: str = "olá, mundo!"

is_alpha = string.isalpha()
print(f"\nExemplo do Método 'isalpha()': {is_alpha}")


# - - - > Exemplo do Método 'isnumeric()':
string: str = "olá, mundo!"

is_numeric = string.isnumeric()
print(f"\nExemplo do Método 'isnumeric()': {is_numeric}")


# - - - > Exemplo do Método 'join()':
lista_palavras: list = ['Olá', 'mundo', 'Python']

lista_join = '-'.join(lista_palavras)
print(f"\nExemplo do Método 'join()': {lista_join}")
