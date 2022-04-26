from random import randint

students_input = input('Введите фамилии присутствующих учеников: ')
students_list = students_input.split(', ')
topics_list = ['циклы', 'функции', 'списки', 'словари','множества']
for i in range(len(students_list)):
    name = students_list[i]
    topic = topics_list[randint(0, len(topics_list)-1)]
    print(f"У ученика {name} проект под названием {topic}")
