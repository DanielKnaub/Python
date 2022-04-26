question = input()
answer_list = ['бег', 'приседания', 'наклоны', 'отжимания', 'подтягивания']


def training_program(answer_list):
    print(answer_list[0], answer_list[1], answer_list[2], answer_list[3], answer_list[4], sep='\n')


def answer(question):
    if question == 'Какие упражнения включены в тренировку?':
        training_program(answer_list)
    else:
        print('Я не знаю ответ. Я всего лишь твой персональный тренер')


answer(question)
