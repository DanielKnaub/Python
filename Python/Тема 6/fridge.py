print('Введите номер холодильника (от 1 до 5)')
num = input()
numbers = ['1', '2', '3', '4', '5']
if num not in numbers:
    print('Такого холодильника нет')
juices = ['яблочный сок', 'апельсиновый сок', 'томатный сок']
fruits = ['яблоки', 'бананы', 'апельсины']
sweets = ['шоколад', 'карамель', 'пряники']
vegetables = ['капуста', 'морковь', 'картофель']
dairy_products = ['молоко', 'кефир', 'бифидок']
num1 = int(num) - 1
print('Введите название продукта')
product = input()
if num == numbers[0]:
    if product in juices:
        print('В холодильнике под номером', num, 'есть продукт', product)
    else:
        print('В холодильнике под номером', num, 'нет продукта', product)
elif num == numbers[1]:
    if product in fruits:
        print('В холодильнике под номером', num, 'есть продукт', product)
    else:
        print('В холодильнике под номером', num, 'нет продукта', product)
elif num == numbers[2]:
    if product in sweets:
        print('В холодильнике под номером', num, 'есть продукт', product)
    else:
        print('В холодильнике под номером', num, 'нет продукта', product)
elif num == numbers[3]:
    if product in vegetables:
        print('В холодильнике под номером', num, 'есть продукт', product)
    else:
        print('В холодильнике под номером', num, 'нет продукта', product)
elif num == numbers[4]:
    if product in dairy_products:
        print('В холодильнике под номером', num, 'есть продукт', product)
    else:
        print('В холодильнике под номером', num, 'нет продукта', product)


