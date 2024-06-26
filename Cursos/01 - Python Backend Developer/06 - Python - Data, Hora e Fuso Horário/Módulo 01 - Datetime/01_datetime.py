# - - - - -> Datetime: datetime, date, time 

    #   O módulo 'datetime' em Python fornece classes para manipulação de datas e horas de 
    # forma eficiente. Isso é útil para lidar com datas, horas e operações relacionadas, 
    # como cálculos de diferença entre datas, formatação de datas e horas, e muito mais.


# - - - - -> Exemplo de uso do datetime, date e time:
from datetime import datetime, date, time


# - - - -> Obtendo a data e hora atual:
data_e_hora_atual = datetime.now()
print(f"\nData e hora atual: {data_e_hora_atual}")
print(f"Tipo de dado: {type(data_e_hora_atual)}")


# - - - -> Obtendo apenas a data atual:
data_atual = date.today()
print(f"\nData atual: {data_atual}")
print(f"Tipo de dado: {type(data_atual)}")


# - - - -> Obtendo apenas a hora atual:
hora_atual = time(datetime.now().hour, datetime.now().minute, datetime.now().second)
print(f"\nHora atual: {hora_atual}")
print(f"Tipo de dado: {type(hora_atual)}")


# - - - -> Criando uma data e hora específica:
data_hora_especifica = datetime(2024, 12, 31, 12, 30, 30)
print(f"\nData e hora específica: {data_hora_especifica}")
print(f"Tipo de dado: {type(data_hora_especifica)}")


# - - - -> Criando uma data específica:
data_especifica = date(2024, 12, 31)
print(f"\nData específica: {data_especifica}")
print(f"Tipo de dado: {type(data_especifica)}")


# - - - -> Criando uma hora específica:
hora_especifica = time(12, 50, 59)
print(f"\nHora específica: {hora_especifica}")
print(f"Tipo de dado: {type(hora_especifica)}")
