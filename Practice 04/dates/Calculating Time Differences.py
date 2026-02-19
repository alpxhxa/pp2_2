#ex 01
from datetime import datetime, timedelta
now = datetime.now()
tomorrow = now + timedelta(days=1)
print(tomorrow)

#ex 02
from datetime import date
d1 = date(2024, 1, 1)
d2 = date(2024, 1, 10)
diff = d2 - d1
print(diff.days)

#ex 03
from datetime import datetime, timedelta
dt3 = datetime(2024, 1, 1, 10, 0)
new_time = dt3 - timedelta(hours=5)
print(new_time)

#ex 04
from datetime import timedelta
t1 = timedelta(minutes=30)
t2 = timedelta(seconds=45)
print(t1 + t2)

#ex 05
from datetime import datetime, timedelta
dt5 = datetime.now()
past = dt5 - timedelta(weeks=2)
print(past)