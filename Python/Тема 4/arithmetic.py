print('Введите количество пингвинов')
pinguins_parent = int(input())
for i in range(pinguins_parent):
    print('   _~_')
    print('  (o o)  ')
    print(' /  V  \ ')
    print('/(  _  )\ ')
    print(' ^^^^^^^ ')
print('Сколько пингвинов изображено на экране?')
pinguins_children = int(input())
if pinguins_children == pinguins_parent:
    print('Правильно, молодец!')
while pinguins_children != pinguins_parent:
    print('Неправильно, попробуй ещё раз!')
    for i in range(pinguins_parent):
        print('   _~_')
        print('  (o o)  ')
        print(' /  V  \ ')
        print('/(  _  )\ ')
        print(' ^^^^^^^ ')
    print('Сколько пингвинов изображено на экране?')
    pinguins_children = int(input())
    if pinguins_children == pinguins_parent:
        print('Правильно, молодец!')
        break
    elif pinguins_parent != pinguins_children:
        print('Неправильно, попробуй ещё раз')
        continue



