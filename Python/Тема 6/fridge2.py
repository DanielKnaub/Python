shopping_set ={'оливковое масло', 'дрожжи', 'пеперони', 'сыр', 'спагетти', 'чеснок', 'лук', 'морковь', 'сельдерей', 'фарш', 'сахар', 'помидоры', 'петрушка', 'пармезан', 'моцарелла', 'орегано', 'базилик', 'мука'}
home_food = {'оливковое масло', 'дрожжи', 'пеперони',  'помидоры', 'чеснок', 'лук', 'морковь'}
actial_set = shopping_set.difference(home_food)
print('Вам небходимо докупить:')
print(', '.join(actial_set))
fridge_set = {'сыр', 'моцарелла', 'пармезан'}
print('В этом ходильнике имеются:')
product_set = actial_set.intersection(fridge_set)
print(', '.join(product_set))