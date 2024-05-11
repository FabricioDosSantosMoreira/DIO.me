# - - - - -> Datetime: strftime, strptime

    #   A biblioteca datetime em Python fornece classes para manipulação de datas e horas.
    # Duas funções importantes são strftime() e strptime(), usadas para formatar objetos 
    # datetime em strings e para converter strings em objetos datetime, respectivamente.


# - - - - -> Exemplo de uso do strftime e strptime:
from datetime import datetime


# - - - -> Formatação de objeto datetime para string (strftime):
data_atual = datetime.now()
data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")
print(f"\nFormatação de objeto datetime para string (strftime): {data_formatada}")
print(type(data_formatada))


# - - - -> Conversão de string para objeto datetime (strptime):
data_string = "10/05/2024 15:30:00"
data_convertida = datetime.strptime(data_string, "%d/%m/%Y %H:%M:%S")
print(f"\nConversão de string para objeto datetime (strptime): {data_convertida}")
print(type(data_convertida))
