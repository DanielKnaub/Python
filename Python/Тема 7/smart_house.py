def request_list(request):
    i = (request.split())
    if i[0] == 'Олег,':
        return print('Запрос к Олегу')
    else:
        return print('Посторонний разговор')
print('Сколько строк необходимо анализировать?')
n = int(input())
for i in range(n):
    print('Введите строку под номером', i + 1)
    request = input()
    request_list(request)