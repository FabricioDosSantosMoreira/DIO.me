# - - - - -> Datetime: timedelta

    #   A classe timedelta do módulo datetime é utilizada para representar uma duração
    # ou diferença entre duas datas ou tempos. É comumente usada em operações 
    # que envolvem manipulação de datas e tempos.


# - - - - -> Exemplo de uso do timedelta: 
from datetime import datetime, timedelta


# - - - -> Criando um timedelta:
time_delta = timedelta(weeks=10, days=1)
print(f"\nTimedelta: {time_delta}")
print(f"Tipo de dado {type(time_delta)}")


# - - - -> Somando um timedelta a uma data:
data_atual = datetime.now()
data_futura = data_atual + timedelta(weeks=7)
print(f"\nData atual: {data_atual}")
print(f"Data futura: {data_futura}")


# - - - -> Subtraindo um timedelta de uma data
data_passada = data_atual - timedelta(weeks=1)
print("\nData atual:", data_atual)
print("Data passada:", data_passada)


# - - -> Acessando os componentes da diferença
diferenca = (datetime.now() + timedelta(days=10, seconds=30)) - datetime.now()

print("\nDias de diferença:", diferenca.days)
print("Segundos de diferença:", diferenca.seconds)

horas = diferenca.total_seconds() / 3600
print("Horas de diferença:", horas)