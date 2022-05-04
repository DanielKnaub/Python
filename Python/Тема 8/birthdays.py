import datetime as dt

first_date = dt.datetime(2006, 5, 4)

second_date = dt.datetime(2006, 12, 27)

third_date = dt.datetime(2006, 9, 26)

fourth_date = dt.datetime(2006, 3, 8)

date_list = [first_date, second_date, fourth_date, third_date]

now = dt.datetime.now()

counter = 0
for i in range(4):
    if date_list[i].strftime('%d.%m.') == now.strftime('%d.%m.'):
        print('У одного из ваших друзей сегодня День рождения!')
        counter += 1
        

if counter == 0:
    print('Никто из ваших друзей не отмечает сегодня День рождения')
