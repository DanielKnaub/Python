import random
amount_of_feed = random.randint(0, 3)
if amount_of_feed == 0:
    print('Миска опустела!')
elif amount_of_feed == 1:
    print('Миска почти пуста!')
elif amount_of_feed == 2:
    print('Корм ещё есть!')
elif amount_of_feed == 3:
    print('Миска полная!')