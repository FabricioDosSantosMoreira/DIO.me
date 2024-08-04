# - - - - - > Decorador de Introspecção:
#                 Decoradores de introspecção são funções especiais que podem modificar o comportamento 
#             de outras funções ou métodos. Eles fornecem uma maneira elegante de alterar ou estender 
#             o comportamento de funções sem a necessidade de modificar seu código subjacente.

# - - - - > Exemplo de Decorador de Introspecção:
print("\nExemplo de Decorador de Introspecção:")

import logging

from functools import wraps
from typing import Callable, TypeVar, Any

# NOTE: Tipo genérico para os decoradores
F = TypeVar('F', bound=Callable[..., Any])

# NOTE: Configuração básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# - - - > Criando um Decorador de Introspecção:
def realizar_log(funcao: F) -> F:

    @wraps(funcao)
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        logger.info(f' Iniciando execução da função: {funcao.__name__}')
        resultado = funcao(*args, **kwargs)
        logger.info(f' Concluída execução da função: {funcao.__name__}')

        return resultado
    
    return wrapper


# - - - > Criando uma Função:
@realizar_log # NOTE: Usando o decorador com a sintaxe de "açúcar sintático"
def soma(a: float, b: float) -> float:
    return a + b


# - - - > Usando o Decorador de Introspecção:
print("\nUsando o Decorador de Introspecção:")

print(f"Resultado: {soma(3.5, 5.6)}")
