# - - - - - > Módulo Datetime: strftime, strptime
#                 A biblioteca datetime em Python fornece classes para manipulação de datas e horas.
#             Duas funções importantes são strftime() e strptime(), usadas para formatar objetos 
#             datetime em strings e para converter strings em objetos datetime, respectivamente.


# - - - - > Exemplo de Utilização do 'strftime' e 'strptime':
print("\nExemplo de Utilização do 'strftime' e 'strptime':")

from datetime import datetime

# - - - > Exemplo de Formatação de Datetime para String (strftime):
print("\nExemplo de Formatação de Datetime para String (strftime):")

data_atual = datetime.now()
data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")

print(f"Datetime para string: {data_formatada}")
print(f"Tipo de dado: {type(data_formatada)}")


# - - - > Exemplo de Conversão de String para Datetime (strptime):
print("\nExemplo de Conversão de Dtring para Datetime (strptime):")

data_string = "10/05/2024 15:30:00"
data_convertida = datetime.strptime(data_string, "%d/%m/%Y %H:%M:%S")

print(f"String para datetime: {data_convertida}")
print(f"Tipo de dado: {type(data_convertida)}")
