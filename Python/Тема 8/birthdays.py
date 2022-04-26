import datetime as dt

first_date = dt.datetime(2006, 11, 18)

second_date = dt.datetime(2006, 12, 27)

third_date = dt.datetime(2006, 9, 26)

fourth_date = dt.datetime(2006, 3, 8)

date_list = [first_date, second_date, fourth_date, third_date]

now = dt.datetime.now()

for i in range(4):
    if 