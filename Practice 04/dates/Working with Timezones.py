#ex 01
from datetime import datetime, timezone
utc_dt = datetime.now(timezone.utc)
print(utc_dt)

#ex 02
from datetime import datetime, timezone, timedelta
offset = timezone(timedelta(hours=3))
dt2 = datetime.now(offset)
print(dt2)

#ex 03
from datetime import datetime
from zoneinfo import ZoneInfo
dt3 = datetime.now(ZoneInfo("America/New_York"))
print(dt3)

#ex 04
from datetime import datetime
from zoneinfo import ZoneInfo
tokyo = datetime.now(ZoneInfo("Asia/Tokyo"))
print(tokyo)

#ex 05
from datetime import datetime, timezone
dt5 = datetime(2024, 1, 1, tzinfo=timezone.utc)
print(dt5.isoformat())