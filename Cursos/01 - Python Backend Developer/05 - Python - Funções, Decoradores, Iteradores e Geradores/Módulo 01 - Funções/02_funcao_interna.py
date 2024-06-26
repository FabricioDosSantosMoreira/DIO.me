# - - - - -> Funções Internas:

    #   Funções internas são funções definidas dentro de outras funções. Elas têm 
    # acesso ao escopo da função externa, o que significa que podem usar variáveis 
    # e argumentos dessa função externa.


# - - - - -> Exemplo de Funções Internas:

def externa():
    print("\nExecutando a função externa!")
    
    def interna():  # Função interna
        print("\nExecutando a função interna!")

        return "\nEste é o retorno da função interna!"

    return interna()

print(externa())
