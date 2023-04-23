#!/usr/bin/env python3
import datetime

# first sunday of 1901
p = datetime.date(year=1901, month=1, day=6)
delta = datetime.timedelta(days=7)
end = datetime.date(year=2000, month=12, day=31)

count = 0
while p < end:
    if p.day == 1 and p.weekday() == 6:
        count += 1
    p += delta
print(count)
