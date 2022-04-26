students_list = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Соколов', 'Михайлов']
print("Пожалуйста, введите фамилии присутствующих учеников")
surnames = input()
lesson_list = surnames.split(',')
result = list(set(students_list) ^ set(lesson_list))
count = len(result)
if count != 0:
    for i in range(count):
        print(f'Cегодня в классе отсутствует {result[i]}')
else:
    print('В классе присутствуют все')