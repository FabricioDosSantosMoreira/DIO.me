# - - - - -> Decorador de Introspecção:

    #   Decoradores de introspecção são funções especiais que podem modificar o comportamento 
    # de outras funções ou métodos. Eles fornecem uma maneira elegante de alterar ou estender 
    # o comportamento de funções sem a necessidade de modificar seu código subjacente.


# - - - - -> Exemplo de Decorador de Introspecção:

# - - - -> Definição do Decorador:
import logging

from functools import wraps

# Configuração básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_function(func):  # Decorador introspectivo para logging

    @wraps(func)
    def wrapper(*args, **kwargs):

        logger.info(f'Iniciando execução da função: {func.__name__}')
        result = func(*args, **kwargs)
        logger.info(f'Concluída execução da função: {func.__name__}')

        return result
    
    return wrapper


# - - - -> Uso do Decorador:
@log_function
def soma(a, b):
    return a + b

# - - - -> Chamada da Função Decorada:
resultado = soma(3, 5)
print(f"\nResultado da soma: {resultado}")
