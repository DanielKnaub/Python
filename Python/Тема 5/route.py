import random
route = [11, 16, 417, 428, 480]
time = [random.randint(5, 15), random.randint(5, 15), random.randint(5, 15), random.randint(5, 15), random.randint(5, 15)]


def search(user_route):
    if user_route == route[0] or user_route == route[1] or user_route == route[2] or user_route == route[3] or user_route == route[4]:
        if user_route == route[0]:
            print('Время, оставшееся до прибытия маршрута под номером', route[0], ':', time[0], 'минут')
        elif user_route == route[1]:
            print('Время, оставшееся до прибытия маршрута под номером', route[1], ':', time[1], 'минут')
        elif user_route == route[2]:
            print('Время, оставшееся до прибытия маршрута под номером', route[2], ':', time[2], 'минут')
        elif user_route == route[3]:
            print('Время, оставшееся до прибытия маршрута под номером', route[3], ':', time[3], 'минут')
        elif user_route == route[4]:
            print('Время, оставшееся до прибытия маршрута под номером', route[4], ':', time[4], 'минут')
    else:
        print('Такого маршрута не существует')


print('Введите номер маршрута')
user_route = int(input())

search(user_route)
