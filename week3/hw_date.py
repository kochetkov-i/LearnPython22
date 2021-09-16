from datetime import date, datetime, timedelta


today = datetime.now()
one_day_delta = timedelta(days = 1)
thirty_days_delta = timedelta(days = 30)
yesterday = today - one_day_delta
month_ago = today - thirty_days_delta

print(yesterday)
print(today)
print(month_ago)

str_date = "01/01/25 12:10:03.234567"
date_from_str = datetime.strptime(str_date, '%d/%m/%y %H:%M:%S.%f')
print(date_from_str)
