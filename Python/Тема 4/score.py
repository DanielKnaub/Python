print('Введите количество пингвинов')
pengiuns_parent = int(input())
for i in range(pengiuns_parent):
        print('    _~_')
        print('   (o o)  ')
        print('  /  V  \ ')
        print(' /(  _  )\ ')
        print('   ^^^^^  ')
        print('Сколько пингвинов изображено на экране?')
        pengiuns_children = int(input())
if pengiuns_parent == pengiuns_children:
    print('Правильно, молодец!')
while pengiuns_parent != pengiuns_children:
    print('Не правильно, попробуй ещё раз!')
    for pengiuns_parent in range(pengiuns_parent):
        print('    _~_')
        print('   (o o)  ')
        print('  /  V  \ ')
        print(' /(  _  )\ ')
        print('   ^^^^^  ')
        print('Сколько пингвинов изображено на экране?')
    pengiuns_children = int(input())
    if pengiuns_parent == pengiuns_children:
        break
        print('Правильно, молодец!')

