## 1 

# num1 = input("Введите первое число: ")
# operator = input("+, -, /, *")
# num2 = input("Введите второе число: ")
# if operator("+"):
#     print(num1 + num2)
# elif operator("-"):
#     print(num1 - num2)
# elif operator("/"):
#     print(num1 / num2)
# elif operator("*"):
#     print(num1 * num2)
# else:
#     print("Введите корректное значение!")


## 2 

# minuta = int(input("Введите минуту: "))
# num = minuta // 60                                     # // это для того чтобы получить целое число при делении
# chas_minuta = minuta % 60                              # тут мы снова поделили минуту на 60 и в итоге получили 15 чтобы получить остаток 
# print(num, str("часа "), chas_minuta, str("минут"))


##3 

# operator1 = int(input("Введите цену товара: "))
# operator2 = int(input("Ввкдите скидку: "))
# print("К оплате: ", operator1 - operator2)


##4 

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# print(int(num1 + num2 + num3 / 3))


##5 

# def sum_two_numbers(num1, num2):
#     print(num1 + num2)

# sum_two_numbers(3, 7)
# sum_two_numbers(5, -2)


##6

# def is_even():
#     num1 = int(input("Введите число: "))
#     if num1 % 2 == 0:
#         print(True)
#     else:
#         print(False)

# is_even()


##7 

# def longest_string():
#     stroka1 = str(input("Введите первое слово: "))
#     stroka2 = str(input("Введите второе слово: "))
#     stroka3 = str(input("Введите третье слово: "))

#     if stroka1 >= stroka2 and stroka1 >= stroka3:
#         print(stroka1)
#     elif stroka2 >= stroka1 and stroka2 >= stroka3:
#         print(stroka2)
#     else:
#         print(stroka3)

# longest_string()


##8


try:
    with open("numbers.txt", "r", encoding="utf-8") as r:
        numbers = []
        for i, line in enumerate(r, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                num = float(line)
                numbers.append(num)
            except ValueError:
                print(f"Строка {i} пропущена: не число")

        if numbers:
            total = sum(numbers)
            average = total / len(numbers)
            print(f"Сумма: {total} Среднее: {average}")
        else:
            print("Нет корректных чисел для подсчета")

except FileNotFoundError:
    print("Файл не найден.")