# - - - - -> Funções: Retornando Funções e Passando Funções como Parâmetros:

    #   Em Python, é possível retornar funções de outras funções e também passar funções
    # como argumentos para outras funções. Isso oferece uma grande flexibilidade e 
    # poder de expressão na construção de programas.


# - - - - -> Exemplo de funções retornando funções:
def calculadora(operacao):

    def soma(a, b):
        return a + b
    
    def subtracao(a, b):
        return a - b
    
    def multiplicacao(a, b):
        return a * b
    
    def divisao(a, b):
        return a / b
    
    match operacao:
        case "+":
            return soma
        case "-":
            return subtracao
        case "*":
            return multiplicacao
        case "/":
            return divisao
    
a, b = 10, 8

print(calculadora('+'))
print(calculadora('-'))
print(calculadora('*'))
print(calculadora('/'))
print(calculadora('+')(a, b)) 
print(calculadora('-')(a, b))
print(calculadora('*')(a, b))
print(calculadora('/')(a, b))


# - - - - -> Exemplo de passagem de funções como parâmetro:
def aplicar_funcao(funcao, valor):
    return funcao(valor)

def dobro(x):
    return x * 2

def triplo(x):
    return x * 3

print("\nAplicar função dobro:", aplicar_funcao(dobro, 5))  # Saída: 10
print("Aplicar função triplo:", aplicar_funcao(triplo, 5))  # Saída: 15
