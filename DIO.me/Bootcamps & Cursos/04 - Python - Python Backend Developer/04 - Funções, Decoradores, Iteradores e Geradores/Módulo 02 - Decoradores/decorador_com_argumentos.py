# - - - - - > Decoradores com Argumentos:

#                 Decoradores com argumentos são funções que envolvem outras funções para 
#             modificar ou estender seu comportamento. Eles aceitam argumentos adicionais 
#             que permitem personalizar o comportamento do decorador.


# - - - - > Exemplo de Decoradores com Argumentos:
print("\nExemplo de Decoradores com Argumentos:")

from typing import Callable, TypeVar, Any

# NOTE: Tipo genérico para os decoradores
F = TypeVar('F', bound=Callable[..., Any])


# - - - > Criando um Decorador com Argumentos para Verbose:
def verbose(prefix: str) -> Callable[[F], F]:

    def decorator(funcao: F) -> F:

        def wrapper(*args: Any, **kwargs: Any) -> Any:

            print(f'{prefix}: Função {funcao.__name__} sendo chamada.')
            resultado = funcao(*args, **kwargs)
            print(f'{prefix}: Função {funcao.__name__} concluída.')

            return resultado
        
        return wrapper
    
    return decorator


# - - - > Criando uma Função:
@verbose("DEBUG") # NOTE: Usando o decorador com a sintaxe de "açúcar sintático"
def soma(a: float, b: float) -> float:
    return a + b


# - - - > Usando o Decorador com Argumentos:
print("\nUsando o Decorador com Argumentos:")

print(f"Resultado: {soma(3.5, 5.6)}")
