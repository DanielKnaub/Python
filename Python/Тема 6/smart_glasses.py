words_dict = {
    'ticket': 'билет',
    'arrive': 'прибывать',
    'time': 'время',
    'date': 'дата',
    'flight': 'рейс',
    'landing': 'посадка',
    'passport': 'паспорт',
    'aisle': 'проход',
    'delay': 'задержка',
    'boarding': 'посадка',
    'customs': 'таможня'
}
print('Выберите слово, которое необходимо перевести')
print(', '.join(words_dict.keys()))
word = input()
print('Перевод слова ', word, ' - ', words_dict[word], sep='')

