#ex 01
import datetime
print(datetime.datetime.now())

#ex 02
import datetime
print(datetime.date.today())

#ex 03
from datetime import time
t = time(14, 30, 15)
print(t)

#ex 04
import datetime
print(datetime.MAXYEAR)

#ex 05
import datetime
dt = datetime.datetime(2023, 10, 5, 12, 0)
print(dt.timestamp())