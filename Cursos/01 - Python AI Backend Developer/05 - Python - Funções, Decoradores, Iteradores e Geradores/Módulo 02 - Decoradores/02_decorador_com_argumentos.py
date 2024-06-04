# - - - - -> Decoradores com Argumentos:

    #   Decoradores com argumentos são funções que envolvem outras funções para 
    # modificar ou estender seu comportamento. Eles aceitam argumentos adicionais 
    # que permitem personalizar o comportamento do decorador.


# - - - - -> Exemplo de Decoradores com Argumentos:

# - - - -> Decorador com Argumentos para Verbose:
def verbose(prefix):

    def decorator(func):

        def wrapper(*args, **kwargs):

            print(f'\n{prefix}: Função {func.__name__} sendo chamada.')
            result = func(*args, **kwargs)
            print(f'\n{prefix}: Função {func.__name__} concluída.')

            return result
        
        return wrapper
    
    return decorator


# - - - -> Uso do Decorador com Argumentos:
@verbose("DEBUG")
def soma(a, b):
    return a + b

resultado = soma(3, 5)
print("\nResultado da soma:", resultado)
