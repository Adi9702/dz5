
names = ["Aslan", "Islam", "Bael", "Askhat", "Aruzhan"]
operator = input("Введите имя: ")
if operator in names:
    print("Имя найдено:", operator )
else:
    names.append(operator)
    print("Имя добавлено:", operator)
    print("Обновленный список имен:", names)
