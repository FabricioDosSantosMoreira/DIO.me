# A indentação é usada para definir blocos de código, como em funções, loops e condicionais.  
# Cada nível de indentação indica um novo bloco.
# Os blocos de código são delimitados por dois pontos (:) 
# e o código dentro de um bloco é indentado com espaços ou tabulações.

#A indentação correta é crucial em Python, pois determina a estrutura e a execução do código.


def par_ou_impar(numero: int): # início do bloco do método

    # Verificando se o número é divisível por 2
    if numero % 2 == 0: # início do bloco do if

        print(f"{numero} é par.")  # Esta linha está dentro do bloco "if" porque está identada dentro dele
    else:

        print(f"{numero} é ímpar.")  # Esta linha está dentro do bloco "else" porque está identada dentro dele

    # fim do bloco do if

# fim do bloco do método

par_ou_impar(7) # Chamando a função par_ou_impar para verificar se um número é par ou ímpar