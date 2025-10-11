

from dotenv import load_dotenv
# это чтобы импортировать функцию load_dotenv из библиотеки python-dotenv (это находится в папке "env" по ссылке ищет)

import os
# это чтобы прочитать модули в 'env'

import requests
# Делает HTTP-запросы к API (requests - это внешняя библиотека)

from lesson_5_dz.math_utils import add, multiply


load_dotenv()
# это чотбы загрузить функции из env

API_URL = os.getenv("API_URL")
# это чтобы взять или призвать код из env

print("Сумма:", add(5, 3))
print("Произведение:", multiply(5, 3))


response = requests.get(API_URL)
# эта строка отправляет запрос на сайт и чтобы птом показать это нам

print("Ответ от API:")
print(response.json())