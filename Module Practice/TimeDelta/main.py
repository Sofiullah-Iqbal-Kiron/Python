from datetime import time, date, datetime, timedelta

tisha_bday = date(2023, 8, 14)
tisha_bday_r = timedelta(days=53)
today = datetime.now()
print(today + tisha_bday_r)
