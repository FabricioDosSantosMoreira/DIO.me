# - - - - -> Pytz:

    #   O módulo 'pytz' é uma biblioteca Python que permite trabalhar com fusos horários de 
    # forma eficiente. Ele fornece suporte para conversão entre diferentes fusos horários, 
    # bem como para obtenção de informações sobre fusos horários em todo o mundo.


# - - - - -> Exemplo de utilização do Pytz:
import pytz # NOTE: pip install pytz

from datetime import datetime


# - - - -> Obtendo a lista de fusos horários disponíveis:
fusos_horarios = pytz.all_timezones
print("\nLista de fusos horários disponíveis:")
for fuso in fusos_horarios:
    print(f"\t{fuso}")


# - - - -> Obtendo a hora atual em um fuso horário específico:
fuso_horario = pytz.timezone('America/Sao_Paulo')
hora_atual = datetime.now(fuso_horario)
print("\nHora Atual em São Paulo:", hora_atual)


# - - - -> Convertendo a hora atual para outro fuso horário:
fuso_destino = pytz.timezone('America/New_York')
hora_atual = datetime.now(pytz.timezone('UTC'))
hora_atual_destino = hora_atual.astimezone(fuso_destino)
print("\nHora Atual em Nova Iorque:", hora_atual_destino)


# - - - -> Tips:

    # pip install pytz
    
    # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    # https://pypi.org/project/pytz/

    # É preferível usar o UTC e quando for mostrar ao usuario final formatar para o timezone dele
