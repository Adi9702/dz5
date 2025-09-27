
# Функции - ее используют если логика должна будет повторяется 

# def calc():
#     num1 = int(input("ВВедите первое число: "))
#     num2 = int(input("введите второе число: "))
#     print(num1 + num2)

# calc() 


# def calc(num1, num2):  #num1 num2 - параметры 
#     print(num1 + num2)

# calc(55, 44) # к параметрам передаются аргументы 

# Функция принимает все типы данных 


#Логикку одной функции можно передовать или использовать в другой функции

# def func_while():
#     n = 0 
#     while True:
#         n += 1
#         print(n)
#         if n == 20:
#             print("Stop")
#             break

# def main():
#     return func_while()

# main()

# def helllo_user(name: str) -> str:  # -> этот знак значит что при принте все будет выходить как стр 
#     print("Здравтсвуйте", name)
# helllo_user("Islam")
# helllo_user("Asyl")
# helllo_user(3)


# def num0():
#     a = 20
#     num1 = int(input("Введите число: "))
#     if num1 == a:
#         print("число найдено")
#     else:
#         print("не найдено")

# def num():
#     return num0()

# num()


# def add(num1: int, num2: int):
#     print(num1 + num2)
# def sud(num1: int, num2: int):
#     print(num1 - num2)
# def mult(num1: int, num2: int):
#     print(num1 * num2)
# def div(num1: int, num2: int):
#     print(num1 / num2)

# def calculator(num1: int, operator: str, num2: int):
#     if operator == "+":
#         add(num1, num2) 
#     elif operator == "-":
#         sud(num1, num2)
#     elif operator == "*":
#         mult(num1, num2)
#     elif operator == "/":
#         div(num1, num2)
#     else:
#         print("Error")

# calculator( 20, "+", 30)  


# name = "Привет, как дела?"

# name1 = "а, е, ё, и, о, у, ы, э, ю, я"

# def count_vowels(text: str) -> int:
#     name1 = "а, е, ё, и, о, у, ы, э, ю, я"
#     count = 0 
#     for char in text:
#         if char in name1:
#             count += 1 
#     print(count)

              
# count_vowels("Привет, как дела?")

# def hello_world(x):
#     return x * x

# print(hello_world(10))

# hello = lambda x: x * x 
# print(hello(10))

# print((lambda x: x * x)(10)) # вот так оно и сократилось до одной строки 



