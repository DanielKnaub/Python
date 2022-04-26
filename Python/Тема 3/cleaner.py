print('Выберите вид уборки.Введите 1 или 2: ')
print('1. сухая уборка')
print('2. влажная уборка')
cleaning_type_num = int(input())
print('Выберите время уборки. Введите 1 или 2: ')
print('1. по утрам')
print('2. по вечерам')
cleaning_time_num = int(input())
print('Выберите периодичность уборки. Введите 1, 2 или 3:')
print('1. ежедневно')
print('2. через день')
print('3. через каждые два дня')
cleaning_frequency_num = int(input())
if cleaning_type_num == 1:
    cleaning_type = 'сухая уборка'
elif cleaning_type_num == 2:
    cleaning_type = 'влажная уборка'
if cleaning_time_num == 1:
    cleaning_time = 'по утрам'
elif cleaning_time_num == 2:
    cleaning_time = 'по вечерам'
if cleaning_frequency_num == 1:
    cleaning_frequency = 'ежедневно'
elif cleaning_frequency_num == 2:
    cleaning_frequency = 'через день'
elif cleaning_frequency_num == 3:
    cleaning_frequency = 'через каждые два дня'
print('Моя программа уборки:', cleaning_type, cleaning_time, cleaning_frequency)
