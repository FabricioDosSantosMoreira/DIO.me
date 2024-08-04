# - - - - - > Interpolação de Variáveis:

#                A interpolação de variáveis é uma técnica para construir strings que 
#             contêm valores de variáveis. Isso é útil para criar mensagens dinâmicas 
#             ou formatar saídas de texto de maneira mais legível.


# - - - - > Exemplos de Interpolação de Variáveis:
print("\nExemplos de Interpolação de Variáveis:")

# - - -> Exemplo de Interpolação de Variáveis com 'f-strings':
nome: str = "João"
idade: int = 30
altura: float = 1.75

mensagem = f"\nOlá, meu nome é {nome}, tenho {idade} anos e minha altura é {altura}m."

print(f"\nExemplo de Interpolação de Variáveis com 'f-strings': {mensagem}")


# - - -> Exemplo de Interpolação de Variáveis com 'format(*args)':
nome: str = "Maria"
idade: int = 25
altura: float = 1.60

mensagem = "\nOlá, meu nome é {}, tenho {} anos e minha altura é {}m.".format(nome, idade, altura)

print(f"\nExemplo de Interpolação de Variáveis com 'format(*args)': {mensagem}")


# - - -> Exemplo de Interpolação de Variáveis com 'format(*kargs)':
nome: str = "Roberta"
idade: int = 19
altura: float = 1.80

mensagem = """\nOlá, meu nome é {nome}, tenho {idade} anos e minha altura é {altura}m.""".format(nome=nome, idade=idade, altura=altura)

print(f"\nExemplo de interpolação de variáveis com 'format(*kargs)': {mensagem}")


# - - - > Exemplo de Interpolação de Variáveis com '%' (old style):
nome: str = "Carlos"
idade: int = 35
altura: float = 1.75

mensagem = "\nOlá, meu nome é %s, tenho %d anos e minha altura é %.2f m." % (nome, idade, altura)

print(f"\nExemplo de Interpolação de Variáveis com '%' (old style): {mensagem}")
