from datetime import datetime


data_hora_atual = datetime.now()

mascara = "%d/%m/%Y %H:%M %a"

print(data_hora_atual)
print(data_hora_atual.strftime(mascara))


data_hora_string = "2023-10-20 10:20"
mascara_EN = "%Y-%m-%d %H:%M"


data_str_to_datetime = datetime.strptime(data_hora_string, mascara_EN)

print(data_str_to_datetime)
print(type(data_str_to_datetime))