# - - - - - > Identação e Blocos:

#                 A indentação é usada para definir blocos de código, como em funções, loops e condicionais.  
#             Cada nível de indentação indica um novo bloco. Os blocos de código são delimitados por  
#             dois pontos (:) e o código dentro de um bloco é indentado com espaços ou tabulações.
#             A indentação correta é crucial em Python, pois determina a estrutura e a execução do código.


# - - - - > Exemplo de Identação e Blocos:

def par_ou_impar(numero: int) -> None: # NOTE: Início do bloco do método

    # NOTE: Início do bloco condicional
    if numero % 2 == 0: 
        # NOTE: Esta linha está dentro do bloco 'if' porque está identada dentro dele
        print(f"{numero} é par!") 

    else:
        # NOTE: Esta linha está dentro do bloco 'else' porque está identada dentro dele
        print(f"{numero} é ímpar!") 

    # NOTE: Fim do bloco condicional

# NOTE: Fim do bloco do método


# Chamando a função 'par_ou_impar()' para verificar se o número é par ou ímpar
par_ou_impar(7) 
