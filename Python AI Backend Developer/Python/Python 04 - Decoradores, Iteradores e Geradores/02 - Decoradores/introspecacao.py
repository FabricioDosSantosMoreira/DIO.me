import logging
from functools import wraps

# Configuração básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Decorador introspectivo para logging
def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f'Iniciando execução da função: {func.__name__}')
        result = func(*args, **kwargs)
        logger.info(f'Concluída execução da função: {func.__name__}')
        return result
    return wrapper

# Função que será decorada
@log_function
def soma(a, b):
    return a + b

# Testando a função decorada
resultado = soma(3, 5)
print("Resultado da soma:", resultado)
