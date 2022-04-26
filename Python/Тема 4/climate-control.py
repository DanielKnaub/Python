import random
temp = random.randint(15, 35)
print('Температура воздуха', temp, '°C')
if temp > 25:
	print('Слишком жарко, уменьшаю обогрев помещения')
	temp = 25
elif temp < 23:
	print('Слишком прохладно, усиливаю обогрев помещения')
	temp = 25
if  (temp > 22) and (temp < 26):
	print('Температура воздуха в норме')
print('Продолжить отслеживать температуру воздуха? (y/n)')
agreement = input()
while agreement == 'y':
	temp = random.randint(15, 35)
	print('Температура воздуха', temp, '°C')
	if temp > 25:
		print('Слишком жарко, уменьшаю обогрев помещения')
		temp = 25
	elif temp < 23:
		print('Слишком прохладно, усиливаю обогрев помещения')
		temp = 25
	if  (temp > 22) and (temp < 26):
		print('Температура воздуха в норме')
	print('Продолжить отслеживать температуру воздуха? (y/n)')
	agreement = input()
	if agreement == 'n':
		break