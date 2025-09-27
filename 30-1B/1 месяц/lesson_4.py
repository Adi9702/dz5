
# # Множество set, frozenset
# numbers = {1,2,5,4,7,3}
# print(numbers) # Выйдет все поп порядку (по возрастанию)
# print(numbers [0]) # не поддерживает индекс 

# names = {"Askhat", "Asyl", "Aslan", "Islam"}
# print(names) # выйдет хаотично

# names.add("Nurs") # добавление эоемента в set множества 
# names.remove("Askhat") # удаляет элемент из множества 
# names.pop() # удаляет случайный элемент 
# names.clear() # очищает множество

# list = [10, "10", True, 20.1, [20], {Islam}]
# print(list) # list можно писать все 

# st = {1, "3", True, 20.2}
# print(st) # set выдает ошибки если записать лист и сет а так без проблем 

# frznst = frozenset([1, 2, 3, 4, 5])
# print(frznst) # frozenset нельзя вносить измения (например через add, remove и тд)


# Tuple - кортеж  ( тоже самое чо и лист только он не изменяется, но индекс работает)


# cars = ("BMW", "Toyota", "Ferrari") # Tesla 
# list = list(cars) # здесб мы tuple преобразовали в list 
# list.append("Tesla") # и в лист добавили новый элемент
# cars = tuple(list) # здесь обратно list преобразовали в tuple
# print(cars)

### Можно преобразовывать не используя принт как на втором уроке, можно просто создать переменну и преобразовать 

# КЛЮЧИ 

# students = { "student": "Askhat", "age": 18}
# # print(students)

# # print(len(students)) # Выходит длина словаря (например выйдет 2 так как у нас "ключ: значение")
# # print(students["age"]) # Выходит значение по ключу (используем квадратную скопку как в индексе)
# # students.setdefault("Language", "python") # Добавление новаого элемента (тут пишем через , так как в начале он читает ключ потом значение)
# # students.pop("age") # Удаление по ключу
# # students["language"] = JS # Обновление значение через ключ 
# students["place"] = "Geeks" # Добавление элементов еще один вариант 
# # print(students.keys()) # выходит только ключи 
# print(students.values()) # выходит только знпчения 


