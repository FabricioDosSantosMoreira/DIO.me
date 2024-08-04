# - - - - - > Módulo Datetime: Timezone

#                 O módulo datetime em Python fornece classes para manipular 
#             datas e horas. A classe timezone é uma parte deste módulo e 
#             é usada para representar fusos horários fixos.


# - - - - > Exemplos de Utilização do 'timezone':
print("\nExemplos de Utilização do 'timezone':")

from datetime import datetime, timedelta, timezone


# - - - > Exemplo de Obtenção da Data e Hora Atual em UTC:
print("\nExemplo de Obtenção da Data e Hora Atual em UTC:")

data_hora_utc = datetime.now(timezone.utc)
print(f"Data e hora atual em UTC: {data_hora_utc}")


# - - - > Exemplo de Conversão para Outro Fuso Horário:
print("\nExemplo de Conversão para Outro Fuso Horário:")

data_hora_utc = datetime.now(timezone.utc)

fuso_horario_brasilia = timezone(timedelta(hours=-3))
fuso_horario_oslo = timezone(timedelta(hours=2))

data_hora_brasilia = data_hora_utc.astimezone(fuso_horario_brasilia)
print(f"Data e hora em Brasília: {data_hora_brasilia}")

data_hora_oslo = data_hora_utc.astimezone(fuso_horario_oslo)
print(f"Data e hora em Oslo: {data_hora_oslo}")
