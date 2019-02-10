""""""
from datetime import datetime


str_time = "2018-12-7"
print()
print(datetime.date(datetime.strptime(str_time, "%Y-%m-%d")))