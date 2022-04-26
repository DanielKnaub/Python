import datetime as dt 

first_time = dt.datetime(2022, 2, 19, 9)

second_time = dt.datetime(2022, 2, 19, 11)

third_time = dt.datetime(2022, 2, 19, 11, 30)

fourth_time = dt.datetime(2022, 2, 19, 13)

total = (second_time-first_time)+(fourth_time-third_time)

print('Время, проведённое за компьютером:', total)