
from datetime import datetime 

date_string = "2023-05-01" 
date_obj = datetime.strptime(date_string, "%Y-%d-%m") 

print(date_obj)
datetime()