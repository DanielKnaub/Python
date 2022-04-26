import random

temp = random.randint(15, 35)
if 15 <= temp <= 20 or 25 <= temp <=30 or temp == 35:
	print('Температура воздуха', temp, 'градусов')
elif temp % 10 == 1:
	print('Температура воздуха', temp, 'градус')
elif temp % 10 == 4 or temp % 10 == 3 or temp % 10 == 2:
	print('Температура воздуха', temp, 'градусa')
if temp > 25:
	print('Слишком жарко, уменьшаю обогрев помещения')
	difference = 25 - temp
	temp = temp + difference
elif temp < 23:
	print('Слишком прохладно, усиливаю обогрев помещения')
	difference = 25 - temp
	temp = temp + difference
if (temp > 22) and (temp < 26):
	print('Температура воздуха в норме')
print('Продолжить отслеживать температуру воздуха? (y/n)')
agreement = input()
while agreement == 'y':
	temp = random.randint(15, 35)
	if 15 <= temp <= 20 or 25 <= temp <= 30 or temp == 35:
		print('Температура воздуха', temp, 'градусов')
	elif temp % 10 == 1:
		print('Температура воздуха', temp, 'градус')
	elif temp % 10 == 4 or temp % 10 == 3 or temp % 10 == 2:
		print('Температура воздуха', temp, 'градусa')
	if temp > 25:
		print('Слишком жарко, уменьшаю обогрев помещения')
		temp = 25
	elif temp < 23:
		print('Слишком прохладно, усиливаю обогрев помещения')
		temp = 25
	if (temp > 22) and (temp < 26):
		print('Температура воздуха в норме')
	print('Продолжить отслеживать температуру воздуха? (y/n)')
	agreement = input()
	if agreement == 'n':
		break