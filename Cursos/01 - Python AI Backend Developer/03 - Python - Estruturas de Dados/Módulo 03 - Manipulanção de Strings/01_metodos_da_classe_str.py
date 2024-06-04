# - - - - -> Métodos Úteis da Classe str:

    # Os métodos úteis da classe str são funções incorporadas que podem ser chamadas em 
    # objetos do tipo str para realizar várias operações de manipulação de strings.


# - - - -> Método upper():
mensagem = "Olá, mundo!"
mensagem_upper = mensagem.upper()
print("\nMétodo upper():", mensagem_upper)


# - - - -> Método lower():
mensagem_lower = mensagem.lower()
print("\nMétodo lower():", mensagem_lower)


# - - - -> Método capitalize():
mensagem_capitalize = mensagem.capitalize()
print("\nMétodo capitalize():", mensagem_capitalize)


# - - - -> Método title():
mensagem_title = mensagem.title()
print("\nMétodo title():", mensagem_title)


# - - - -> Método split():
mensagem_split = mensagem.split(',')
print("\nMétodo split():", mensagem_split)


# - - - -> Método strip():
mensagem = "Olá, mundo!"
mensagem_strip = mensagem.strip('mundo!')
print("\nMétodo strip():", mensagem_strip)


# - - - -> Método replace():
mensagem_replace = mensagem.replace('mundo', 'Python')
print("\nMétodo replace():", mensagem_replace)


# - - - -> Método find():
indice_mundo = mensagem.find('mundo')
print("\nMétodo find():", indice_mundo)


# - - - -> Método count():
quantidade_a = mensagem.count('o')
print("\nMétodo count():", quantidade_a)


# - - - -> Método startswith():
comeca_com_ola = mensagem.startswith('Olá')
print("\nMétodo startswith():", comeca_com_ola)


# - - - -> Método endswith():
termina_com_exclamacao = mensagem.endswith('!')
print("\nMétodo endswith():", termina_com_exclamacao)


# - - - -> Método isalnum():
is_alnum = mensagem.isalnum()
print("\nMétodo isalnum():", is_alnum)


# - - - -> Método isalpha():
is_alpha = mensagem.isalpha()
print("\nMétodo isalpha():", is_alpha)


# - - - -> Método isnumeric():
is_numeric = mensagem.isnumeric()
print("\nMétodo isnumeric():", is_numeric)


# - - - -> Método join():
lista_palavras = ['Olá', 'mundo', 'Python']
mensagem_juntada = '-'.join(lista_palavras)
print("\nMétodo join():", mensagem_juntada)
