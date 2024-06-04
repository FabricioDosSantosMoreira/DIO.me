# - - - - -> Decoradores:

    #   Decoradores são funções que envolvem outras funções ou métodos, 
    # permitindo executar código antes e depois da função decorada, sem 
    # modificar seu código. Isso é útil para adicionar funcionalidades 
    # extras a funções existentes sem alterá-las diretamente.


# - - - - -> Exemplo de Uso de Decoradores:

# - - - -> Definição de um decorador:
def meu_decorador(funcao):

    def funcao_decorada(*args, **kwargs):

        print("\nExecutando código antes da função!")
        resultado = funcao(*args, **kwargs)
        print("\nExecutando código depois da função!")

        return resultado
    
    return funcao_decorada


# - - - -> Definição de uma função:
def minha_funcao():
    print("\nExecutando minha função!")


# - - - -> Uso do decorador:
minha_funcao_decorada = meu_decorador(minha_funcao)
minha_funcao_decorada()


# - - - - -> Exemplo de Uso de Decoradores Açucar Sintático:

# - - - -> Uso do decorador com açucar sintático:
@meu_decorador
def minha_outra_funcao():
    print("\nExecutando minha outra função!")


# - - - -> Chamada da função decorada:
minha_outra_funcao()
