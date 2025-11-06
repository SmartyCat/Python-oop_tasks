from datetime import date, timedelta

year, month = int(input()), int(input())
my_date = date(year, month, 1)
while my_date.weekday() != 3:
    my_date += timedelta(days=1)
else:
    my_date += timedelta(days=21)
    print(my_date.strftime("%d.%m.%Y"))
