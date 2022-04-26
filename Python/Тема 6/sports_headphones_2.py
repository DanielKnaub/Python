question = input()
training_dict = {
    'Разминка': 'наклоны головы, наклоны корпуса, вращение руками, бег',
    'Силовая часть': 'отжимания, подтягивания, приседания',
    'Растяжка': 'низкие выпады, наклоны вперёд'
}


def exercises(training_dict):
    print(', '.join(training_dict.values()))


def parts(training_dict):
    print(', '.join(training_dict.keys()))


def training_program(question):
    if question == 'Какие сегодня будут упражнения?':
        exercises(training_dict)
    elif question == 'Из каких основных частей будет состоять тренировка?':
        parts(training_dict)
    else:
        print('Об этом мне неизвестно')


training_program(question)