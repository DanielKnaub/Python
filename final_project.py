#Для завершения программы используйте "exit" или "выход"
from random import randint

while True:
    user_input = input('Выберите устройство: холодильник, чайник, отопление, освещение, робот-пылесос, стиральная машина\n')
    if user_input == 'exit' or user_input == 'выход':
         break
    elif user_input == 'холодильник':
         shopping_list = [] 
         products_list = ['сыр', 'молоко', 'яблоки', 'сливочное масло', 'яйца']
         print('В вашем холодильнике имеются:', ", ".join(products_list)) 
         if len(shopping_list) == 0:
             print('В вашем списке покупок ничего нет. Что-нибудь добавить?')
             shopping_list_input = input()
             shopping_list = shopping_list_input.split(',')
             difference = list(set(list(set(shopping_list) | set(products_list))) ^ set(products_list)) 
             print('Ваш список покупок:', ", ".join(difference))
         else:
             print('Ваш список покупок:', ", ".join(shopping_list))
    elif user_input == 'чайник':
        tea_set = {
              'Зелёный чай': 75,
              'Чёрный чай': 95,
              'Улун': 80,
              'Пуэр': 98
              }
        print('Выберите чай:')
        for key in tea_set.keys():
            print(key)
        tea_user_input = input()
        temp_tea = tea_set.get(tea_user_input)
        print(f"Ваш {tea_user_input} был приготвлен при температуре {temp_tea}°C!")
    elif user_input == 'отопление':
        heat_set = {
             'Кухня': randint(19, 27),
             'Прихожая': randint(19, 27),
             'Cпальня': randint(19, 27),
             'Ванная': randint(19, 27),
             'Гостиная': randint(19, 27)
             }
        print('Выберите комнату:')
        for key in heat_set.keys():
            print(key)
        heat_user_input = input()
        print(f"Какую температуру в комнате {heat_user_input} вы желаете?")
        heat_temp_user_input = int(input())
        heat_set[heat_user_input] = heat_temp_user_input
        print(f"В комнате {heat_user_input} температура стала {heat_temp_user_input}°C!")
    elif user_input == 'освещение':
        light_set = {
             'Кухня': False,
             'Прихожая': False,
             'Cпальня': False,
             'Ванная': False,
             'Гостиная': False
             }
        print('Выберите комнату:')
        for key in light_set.keys():
           print(key)
        light_user_input = input()
        light_set[light_user_input] = True
        print(f"В комнате {light_user_input} включен свет!")
    elif user_input == 'стиральная машина':
        print('В стиральной машине', randint(1,6), 'кг белья. Этого достаточно?')
        washing_machine_user_input = input()
        if washing_machine_user_input == 'да':
            print('Начало стирки... Она будет завершена через', randint(30, 80), 'минут.')
        else:
            print('На нет и суда нет.')
    elif user_input == 'робот-пылесос':
        light_set = {
             'Кухня': False,
             'Прихожая': False,
             'Cпальня': False,
             'Ванная': False,
             'Гостиная': False
             }
        print('Выберите комнату:')
        for key in light_set.keys():
           print(key)
        room_user_input = input()
        print(f"Происходит уборка в комнате {room_user_input}.")