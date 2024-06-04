# - - - - -> Datetime: Timezone

    #   A timezone (fuso horário) é uma região da Terra onde a mesma hora padrão é usada.
    # Em Python, o módulo datetime é utilizado para lidar com datas e horas. A classe 
    # datetime.datetime inclui um método para definir o fuso horário de um objeto de 
    # datetime. O módulo 'pytz' fornece suporte para fuso horário mais completo.


# - - - - -> Exemplo de uso do timezone:
from datetime import datetime, timedelta, timezone


# - - - -> Criando uma data e hora UTC
data_hora_utc = datetime.now(timezone.utc)
print("\nData e hora UTC:", data_hora_utc)


# - - - -> Convertendo para outro fuso horário:
fuso_horario_brasilia = timezone(timedelta(hours=-3))
fuso_horario_oslo = timezone(timedelta(hours=2))

data_hora_brasilia = data_hora_utc.astimezone(fuso_horario_brasilia)
print("\nData e hora em Brasília:", data_hora_brasilia)

data_hora_oslo = data_hora_utc.astimezone(fuso_horario_oslo)
print("\nData e hora em Oslo:", data_hora_oslo)
