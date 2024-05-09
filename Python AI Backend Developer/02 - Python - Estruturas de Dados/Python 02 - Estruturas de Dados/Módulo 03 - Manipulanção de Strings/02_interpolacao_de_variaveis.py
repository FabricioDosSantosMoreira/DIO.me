# - - - - -> Interpolação de Variáveis:

    # A interpolação de variáveis é uma técnica para construir strings que contêm valores de variáveis.
    # Isso é útil para criar mensagens dinâmicas ou formatar saídas de texto de maneira mais legível.


# - - - -> Interpolação de Variáveis com 'f-strings':

# - - -> Exemplo de Interpolação de Variáveis com 'f-strings':
nome = "João"
idade = 30
altura = 1.75

mensagem = f"Olá, meu nome é {nome}, tenho {idade} anos e minha altura é {altura} metros."

print("\nExemplo de interpolação de variáveis com 'f-strings':")
print(mensagem)


# - - - -> Interpolação de Variáveis com o método 'format()':

# - - -> Exemplo de Interpolação de Variáveis com 'format(*args)':
nome = "Maria"
idade = 25
altura = 1.60

mensagem = "Olá, meu nome é {}, tenho {} anos e minha altura é {} metros.".format(nome, idade, altura)

print("\nExemplo de interpolação de variáveis com 'format(*args)':")
print(mensagem)


# - - -> Exemplo de Interpolação de Variáveis com 'format(*kargs)':
nome = "Roberta"
idade = 19
altura = 1.80

mensagem = """Olá, meu nome é {nome}, tenho {idade} anos e 
            minha altura é {altura} metros.""".format(nome=nome, idade=idade, altura=altura)

print("\nExemplo de interpolação de variáveis com 'format(*kargs)':")
print(mensagem)


# - - - -> Interpolação de Variáveis com % (old style):

# - - -> Exemplo de Interpolação de Variáveis com '%':
nome = "Carlos"
idade = 35
altura = 1.75

mensagem = "Olá, meu nome é %s, tenho %d anos e minha altura é %.2f metros." % (nome, idade, altura)

print("\nExemplo de interpolação de variáveis com '%'")
print(mensagem)
