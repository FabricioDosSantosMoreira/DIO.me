# Operadores de atribuição são utilizados para atribuir valores a variáveis em Python. 
# Eles permitem que você associe um valor a uma variável de forma simples e direta. 


# ---> Operador de Atribuição Simples (=)

# Atribui um valor à variável
x = 10 
print("Valor de x após atribuição simples:", x) # Saída: 10


# ---> Operadores de Atribuição Combinada. Estes operadores combinam atribuição com uma operação aritmética

# Operador de Atribuição e Adição (+=)
# Adiciona o valor à variável e atribui o resultado à mesma variável
x = 10 
x += 5  # Equivalente a x = x + 5
print("Valor de x após atribuição e adição:", x) # Saída: 15

# Operador de Atribuição e Subtração (-=)
# Subtrai o valor da variável e atribui o resultado à mesma variável
x = 10 
x -= 3  # Equivalente a x = x - 3
print("Valor de x após atribuição e subtração:", x) # Saída: 7

# Operador de Atribuição e Multiplicação (*=)
# Multiplica o valor à variável e atribui o resultado à mesma variável
x = 10 
x *= 2  # Equivalente a x = x * 2
print("Valor de x após atribuição e multiplicação:", x) # Saída: 20

# Operador de Atribuição e Divisão (/=)
# Divide o valor da variável e atribui o resultado à mesma variável
x = 10 
x /= 4  # Equivalente a x = x / 4
print("Valor de x após atribuição e divisão:", x) # Saída: 2.5

# Operador de Atribuição e Resto da Divisão (%) (também conhecido como módulo)
# Calcula o resto da divisão e atribui o resultado à mesma variável
x = 10 
x %= 2  # Equivalente a x = x % 2
print("Valor de x após atribuição e resto da divisão:", x) # Saída: 0

# Operador de Atribuição e Potenciação (**)
# Eleva a variável à potência do valor e atribui o resultado à mesma variável
x = 10 
x **= 3  # Equivalente a x = x ** 3
print("Valor de x após atribuição e potenciação:", x) # Saída: 1000

# Operador de Atribuição e Divisão Inteira (//)
# Realiza a divisão inteira e atribui o resultado à mesma variável
x = 10 
x //= 2  # Equivalente a x = x // 2
print("Valor de x após atribuição e divisão inteira:", x) # Saída: 5


# Operador de Atribuição de Concatenação (+= com strings)

# Concatena uma string à variável e atribui o resultado à mesma variável
texto = "Olá"
texto += " mundo!"  # Equivalente a texto = texto + " mundo!"
print("Valor de texto após atribuição e concatenação:", texto) # Saída: Olá mundo!