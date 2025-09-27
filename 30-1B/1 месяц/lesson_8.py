
## ИСКЛЮЧЕНИЕ - try (ксли в ex)

# def div(num1, num2):
#     try:
#         return num1 / num2 
#     except ZeroDivisionError:               # здесь пишем какая ошибка
#         return "На ноль делить нельзя!"
#     except TypeError:
#         return "Пиши только int"
    
# print(div(10, 0))
# print(div(10, "uhu"))


# def canculator():
#     while True:
#         try:
#             num1 = int(input("Введите первое число: "))
#             operator = input("+, -, /, *: ")
#             num2 = int(input("Введите второе число: "))

#             if operator == "+":
#                 print(num1 + num2)
#             elif operator == "-":
#                 print(num1 - num2)
#             elif operator == "*":
#                 print(num1 * num2)
#             elif operator == "/":
#                 try:
#                     print(num1 / num2)
#                 except ZeroDivisionError:
#                     print("На ноль делить нельзя!")
#             else:
#                 print("Введите корректное значение")
#         except ValueError:                              # если это записать то даже после ввеления одних данных канкулятор все еще будет активен
#             print("Пиши корректные данные")

# canculator()
            

# try: 
#     print(10/0)
# except:
#     print("ошибка")
# finally:
#     print("я буду работать")



## МОДУЛИ 

# from lesson_7 import mult_func
# num = [10, 230, 21, 203, 421, 42]
# mult_func(num)


# f = open("hello.txt", "w")
# f.write("Python")
# f.close()

# r = open("hello.txt", "r")
# print(r.read())
# r.close()

# def func(x, y=[]):
#     y.append(x) 
#     return y

# print(func(1))
# print(func(2))
# print(func(3))


# with open("geeks.txt", "a+") as g:
#     g.write("Aslan")

# with open("geeks.txt", "r") as r:
#     print(r.read())

