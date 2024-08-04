# - - - - - > Módulo Datetime: datetime, date, time 
#                 O módulo 'datetime' em Python fornece classes para manipulação de datas e horas de 
#             forma eficiente. Isso é útil para lidar com datas, horas e operações relacionadas, 
#             como cálculos de diferença entre datas, formatação de datas e horas, e muito mais.


# - - - - > Exemplos de Utilização do 'datetime', 'date' e 'time':
print("\nExemplos de Utilização do 'datetime', 'date' e 'time':")

from datetime import datetime, date, time

# - - - > Exemplo de Obtenção da Data e Hora Atual:
print("\nExemplo de Obtenção da Data e Hora Atual:")

data_e_hora_atual = datetime.now()

print(f"Data e hora atual: {data_e_hora_atual}")
print(f"Tipo de dado: {type(data_e_hora_atual)}")


# - - - > Exemplo de Obtenção Apenas a Data Atual:
print("\nExemplo de Obtenção Apenas a Data Atual:")

data_atual = date.today()

print(f"Data atual: {data_atual}")
print(f"Tipo de dado: {type(data_atual)}")


# - - - > Exemplo de Obtenção Apenas da Hora Atual:
print("\nExemplo de Obtenção Apenas da Hora Atual:")

hora_atual = time(datetime.now().hour, datetime.now().minute, datetime.now().second)

print(f"Hora atual: {hora_atual}")
print(f"Tipo de dado: {type(hora_atual)}")


# - - - > Exemplo de Criação de uma Data e Hora Específica:
print("\nExemplo de Criação de uma Data e Hora Específica:")

data_hora_especifica = datetime(2024, 12, 31, 12, 30, 30)

print(f"Data e hora específica: {data_hora_especifica}")
print(f"Tipo de dado: {type(data_hora_especifica)}")


# - - - > Exemplo de Criação de uma Data Específica:
print("\nExemplo de Criação de uma Data Específica:")

data_especifica = date(2024, 12, 31)

print(f"Data específica: {data_especifica}")
print(f"Tipo de dado: {type(data_especifica)}")


# - - - > Exemplo de Criação de uma Hora Específica:
print("\nExemplo de Criação de uma Hora Específica:")

hora_especifica = time(12, 50, 59)

print(f"Hora específica: {hora_especifica}")
print(f"Tipo de dado: {type(hora_especifica)}")
