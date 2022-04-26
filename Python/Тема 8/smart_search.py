import re

pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|ru|net|edu|org)"
user_input = input('Введите текст: ')
email = re.search(pattern, user_input)
if email:
	print(email[0])
else:
	print("Электронная почта не обнаружена")
