import datetime as dt
import time

def work():
    data = {}
    now = dt.datetime.now()
    data[now.microsecond] = now.day
    return data

print(work())
time.sleep(0.1)
print(work())