# - - - - - > Módulo Datetime: timedelta

#                 A classe 'timedelta' do módulo 'datetime' é utilizada para representar
#             uma duração ou diferença entre duas datas ou tempos. É comumente usada em 
#             operações que envolvem manipulação de datas e tempos.


# - - - - > Exemplos de Utilização do 'timedelta': 
print("\nExemplos de Utilização do 'timedelta':")

from datetime import datetime, timedelta


# - - - > Exemplo de Criação de um Timedelta:
print("\nExemplo de Criação de um Timedelta:")

time_delta = timedelta(weeks=10, days=1)

print(f"Timedelta: {time_delta}")
print(f"Tipo de dado: {type(time_delta)}")


# - - - > Exemplo de Soma de um Timedelta a uma Data:
print("\nExemplo de Soma de um Timedelta a uma Data:")

data_atual = datetime.now()
data_futura = data_atual + timedelta(weeks=7)

print(f"Data atual: {data_atual.date()}")
print(f"Data futura: {data_futura.date()}")


# - - - > Exemplo de Subtração de um Timedelta de uma Data:
print("\nExemplo de Subtração de um Timedelta de uma Data:")

data_atual = datetime.now()
data_passada = (data_atual - timedelta(weeks=1))

print(f"Data atual: {data_atual.date()}")
print(f"Data passada: {data_passada.date()}")


# - - - > Exemplo de Acesso aos Componentes da Diferença:
print("\nExemplo de Acesso aos Componentes da Diferença:")

diferenca = (datetime.now() + timedelta(days=10, seconds=30)) - datetime.now()

print(f"Dias de diferença: {diferenca.days}") 
print(f"Segundos de diferença: {diferenca.seconds}")

horas = diferenca.total_seconds() / 3600
print(f"Horas de diferença: {horas}")
