#ex 01
from datetime import date
d1 = date(2025, 1, 1)
print(d1)

#ex 02
from datetime import datetime
dt2 = datetime(2026, 5, 20, 15, 30)
print(dt2)

#ex 03
from datetime import date
d3 = date.fromisoformat('2024-12-31')
print(d3)

#ex 04
from datetime import datetime
dt4 = datetime.strptime("25/12/2024", "%d/%m/%Y")
print(dt4)

#ex 05
from datetime import date
d5 = date.fromtimestamp(1700000000)
print(d5)