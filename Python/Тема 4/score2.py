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
else: 
    print('Неправильно попробуй ещё раз!')
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
    else: 
        print('НеправильноБ попробуй ещё раз!')
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
