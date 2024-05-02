# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# pip install pytz


from datetime import datetime
import pytz

# É preferível usar UTC e quando 
# for mostrar ao usuario formatar para o timezone dele
data = datetime.now(pytz.timezone('UTC')) 
print(data)

data = data.astimezone(pytz.timezone('America/Sao_Paulo'))
print(data)