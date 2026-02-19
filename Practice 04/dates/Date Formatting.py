#ex 01
from datetime import datetime
now = datetime(2024, 5, 15)
print(now.strftime("%Y/%m/%d"))

#ex 02
from datetime import datetime
dt2 = datetime(2024, 1, 1)
print(dt2.strftime("%A, %B %d"))

#ex 03
from datetime import datetime
dt3 = datetime.now()
print(dt3.strftime("%H:%M:%S"))

#ex 04
from datetime import datetime
dt4 = datetime(2024, 10, 10)
print(dt4.strftime("%d-%m-%y"))

#ex 05
from datetime import datetime
dt5 = datetime(2024, 3, 8)
print(dt5.strftime("Week: %U"))