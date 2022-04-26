print('Введите высоту комнаты')
room_height = float(input())
print('Введите длину комнаты')
room_length = float(input())
print('Введите высоту оконного проёма')
window_height = float(input())
print('Введите длину оконного проёма')
window_length = float(input())


def calculations(room_height, room_length, window_height, window_length):
    print('Площадь стены без учёта площадь оконного проёма:', room_height * room_length - window_length * window_height, 'кв. м')
calculations(room_height, room_length, window_height, window_length)