# - - - - -> Funções em Python:

# Funções são blocos de código reutilizável que realizam uma tarefa específica quando chamados.
# Elas ajudam a organizar o código, tornando-o mais legível e fácil de manter.

# OBS: / * 










# - - -> Definindo uma função simples:
def saudacao():
    print("Olá, mundo!")

# Chamando a função:
saudacao()

# - - -> Função com parâmetros:
def saudar(nome):
    print("Olá,", nome)

# Chamando a função com argumentos:
saudar("João")
saudar("Maria")

# - - -> Função com valor de retorno:
def soma(a, b):
    return a + b

# Chamando a função e armazenando o resultado:
resultado = soma(3, 5)
print("Resultado da soma:", resultado)

# - - -> Função com argumentos padrão:
def saudacao_personalizada(nome, saudacao="Olá"):
    print(saudacao + ",", nome)

# Chamando a função com e sem especificar o argumento padrão:
saudacao_personalizada("João")
saudacao_personalizada("Maria", "Oi")

# - - -> Função com número variável de argumentos:
def soma_variavel(*args):
    total = 0
    for num in args:
        total += num
    return total

# Chamando a função com diferentes números de argumentos:
print("Soma dos números:", soma_variavel(1, 2, 3))
print("Soma dos números:", soma_variavel(1, 2, 3, 4, 5))

# - - -> Função com número variável de argumentos de palavras-chave:
def imprimir_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Chamando a função com diferentes argumentos de palavras-chave:
imprimir_info(nome="João", idade=30)
imprimir_info(nome="Maria", idade=25, cidade="São Paulo")

# - - -> Função lambda (funções anônimas):
dobro = lambda x: x * 2
print("O dobro de 5 é:", dobro(5))

# - - -> Função recursiva (função que chama a si mesma):
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print("Fatorial de 5:", fatorial(5))
