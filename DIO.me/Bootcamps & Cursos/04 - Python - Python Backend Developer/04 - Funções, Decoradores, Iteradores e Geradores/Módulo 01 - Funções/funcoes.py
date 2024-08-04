# - - - - - > Funções:

#                 Funções são blocos de código reutilizável que realizam uma tarefa específica quando chamados.
#             Elas ajudam a organizar o código, tornando-o mais legível e fácil de manter.


# - - - - > Exemplos de Funções:
print("\nExemplos de Funções:")

# - - - > Exemplo de Função Simples:
print("\nExemplo de Função Simples:")

def saudacao() -> None:
    print("Olá, mundo!")

# NOTE: Chamando a função
saudacao()


# - - - > Exemplo de Função com Parâmetros:
print("\nExemplo de Função com Parâmetros:")

def saudar(nome: str) -> None:
    print(f"Olá, {nome}")

# NOTE: Chamando a função com argumentos
saudar("João")
saudar("Maria")


# - - - > Exemplo de Função com Parâmetros por Referência:
print("\nExemplo de Função com Parâmetros por Referência:")

def modificar_lista(lista) -> None:
    lista.append(4)

lista: list = [1, 2, 3]
modificar_lista(lista)
print(f"Lista modificada: {lista}")


# - - - > Exemplo de Função com Valor de Retorno:
print("\nExemplo de Função com Valor de Retorno:")

def soma(a: float, b: float) -> float:
    return a + b

# NOTE: Chamando a função e armazenando o resultado
resultado: float = soma(3.5, 5.9)
print(f"Resultado: {resultado}")


# - - - > Exemplo de Função com Argumentos Padrão:
print("\nExemplo de Função com Argumentos Padrão:")

def saudacao_personalizada(nome: str, saudacao: str="Olá") -> None:
    print(f"{saudacao}, {nome}")

# NOTE: Chamando a função sem especificar o argumento padrão
saudacao_personalizada("João")

# NOTE: Chamando a função especificando o argumento padrão
saudacao_personalizada("Maria", saudacao="Oi")


# - - - > Exemplo de Função com um Número Variável de Argumentos:
print("\nExemplo de Função com um Número Variável de Argumentos:")

def soma_variavel(*args) -> int:
    total: int = 0

    for num in args:
        total += num

    return total

# NOTE: Chamando a função com diferentes números de argumentos
print(f"Resultado: {soma_variavel(1, 2, 3)}")
print(f"Resultado: {soma_variavel(1, 2, 3, 4, 5)}")


# - - - > Exemplo de Função com Número Variável de Argumentos de Palavras-Chave:
print("\nExemplo de Função com um Número Variável de Argumentos:")

def imprimir_info(**kwargs) -> None:
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# NOTE: Chamando a função com diferentes argumentos de palavras-chave
imprimir_info(nome="João", idade=30)
imprimir_info(nome="Maria", idade=25, cidade="São Paulo")


# - - - > Exemplo de Função Lambda (funções anônimas):
print("\nExemplo de Função Lambda (funções anônimas):")

dobro: float = lambda x: x * 2

print(f"Resultado: {dobro(5)}")


# - - - > Exemplo de Função Recursiva (chama a si mesma):
print("\nExemplo de Função Recursiva (chama a si mesma):")

def fatorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print(f"Resultado: {fatorial(5)}")


# - - - > Exemplo de Função Interna (funções dentro de funções):
print("\nExemplo de Função Interna (funções dentro de funções):")

def externa() -> None:
    print("Executando a função externa!")
    
    def interna() -> None:
        print("Executando a função interna!")

        return "Este é o retorno da função interna!"

    return interna()

print(f"Resultado: {externa()}")


# - - - > Exemplo de Funções Retornando Funções:
print("\nExemplo de Funções Retornando Funções:")

from typing import Callable

def calculadora(operacao: str) -> Callable[[float, float], float]:

    def soma(a: float, b: float) -> float:
        return a + b
    

    def subtracao(a: float, b: float) -> float:
        return a - b
    

    match operacao:
        case "+":
            return soma
        case "-":
            return subtracao

print(f"Resultado: {calculadora('+')}")
print(f"Resultado: {calculadora('-')}")
print(f"Resultado: {calculadora('+')(10, 8)}") 
print(f"Resultado: {calculadora('-')(10, 8)}")


# - - - - -> Exemplo de Função com Funções como Parâmetro:
print("\nExemplo de Função com Funções como Parâmetro:")

def aplicar_funcao(funcao: Callable[[int], int], valor: int) -> int:
    return funcao(valor)


def triplo(x: int) -> int:
    return x * 3

print(f"Resultado: {aplicar_funcao(triplo, 5)}")
