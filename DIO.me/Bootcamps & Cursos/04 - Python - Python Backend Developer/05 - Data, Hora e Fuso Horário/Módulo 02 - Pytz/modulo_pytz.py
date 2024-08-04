# - - - - - > Módulo Pytz:

#                 O módulo 'pytz' é uma biblioteca Python que permite trabalhar com fusos horários de 
#             forma eficiente. Ele fornece suporte para conversão entre diferentes fusos horários, 
#             bem como para obtenção de informações sobre fusos horários em todo o mundo.


# - - - - > Exemplos de Utilização do 'pytz':
print("\nExemplos de Utilização do 'pytz':")

import pytz

from datetime import datetime


# - - - > Exemplo de Obtenção da Lista de Fusos Horários Disponíveis:
print("\nExemplo de Obtenção da Lista de Fusos Horários Disponíveis:")

fusos_horarios = pytz.all_timezones

print("Lista de fusos horários disponíveis:")
for fuso in fusos_horarios:
    print(f"\t{fuso}")


# - - - > Exemplo de Obtenção da Hora Atual em um Fuso Horário Específico:
print("\nExemplo de Obtenção da Hora Atual em um Fuso Horário Específico:")

fuso_horario = pytz.timezone('America/Sao_Paulo')

hora_atual = datetime.now(fuso_horario).time()
print("Hora Atual em São Paulo:", hora_atual)


# - - - > Exemplo de Conversão da Hora Atual para Outro Fuso Horário:
print("\nExemplo de Conversão da Hora Atual para Outro Fuso Horário:")

fuso_destino = pytz.timezone('America/New_York')

hora_atual = datetime.now(pytz.timezone('UTC'))
hora_atual_destino = hora_atual.astimezone(fuso_destino)

print("Hora Atual em Nova Iorque:", hora_atual_destino)
