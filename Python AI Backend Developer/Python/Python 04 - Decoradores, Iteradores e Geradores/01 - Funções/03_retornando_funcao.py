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
c = calculadora("+")
print(c(a, b))


print(calculadora("+")(a, b)) # calculadora("+") retorna um objeto contendo uma funcao
print(calculadora("-")(a, b))
print(calculadora("*")(a, b))
print(calculadora("/")(a, b))