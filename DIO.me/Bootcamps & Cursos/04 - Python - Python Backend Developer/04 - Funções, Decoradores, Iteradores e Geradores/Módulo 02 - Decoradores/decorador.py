# - - - - - > Decoradores:

#                 Decoradores são funções que envolvem outras funções ou métodos, 
#             permitindo executar código antes e depois da função decorada, sem 
#             modificar seu código. Isso é útil para adicionar funcionalidades 
#             extras a funções existentes sem alterá-las diretamente.


# - - - - -> Exemplo de Decoradores:
print("\nExemplo de Decoradores:")

from typing import Callable, TypeVar, Any

# NOTE: Tipo genérico para os decoradores
F = TypeVar('F', bound=Callable[..., Any])

# - - - - > Exemplo de Decorador Simples:
print("\nExemplo de Decorador Simples:")

# - - - > Criando um Decorador Simples:
def meu_decorador(funcao: F) -> F:

    def funcao_decorada(*args: Any, **kwargs: Any) -> Any:

        print("Executando o código antes da função!")
        resultado = funcao(*args, **kwargs)
        print("Executando o código depois da função!")

        return resultado
    
    return funcao_decorada


# - - - > Criando uma Função:
def minha_funcao() -> None:
    print("Executando a função!")


# - - - > Usando o Decorador:
minha_funcao_decorada: F = meu_decorador(minha_funcao)
minha_funcao_decorada()


# - - - - > Exemplo de Decorador com Açucar Sintático:
print("\nExemplo de Decorador com Açucar Sintático:")

# - - - > Criando um Decorador Simples:
def meu_decorador(funcao: F) -> F:

    def funcao_decorada(*args: Any, **kwargs: Any) -> Any:

        print("Executando o código antes da função!")
        resultado = funcao(*args, **kwargs)
        print("Executando o código depois da função!")

        return resultado
    
    return funcao_decorada


# - - - > Criando uma Função:
@meu_decorador  # NOTE: Usando o decorador com a sintaxe de "açúcar sintático"
def minha_funcao() -> None:
    print("Executando a função!")


# - - - > Usando o Decorador:
minha_funcao()
