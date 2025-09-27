
# Лямбда функции 

# def mult (num1: int = 2, num2: int = 2) -> int:
#     return num1 * num2 

# print(mult(10,5))

# lambda_mult = lambda num1, num2: num1 * num2 
# print(lambda_mult(10,5))

# print((lambda num1, num2: num1 * num2)(10,5))


# numders = [10, 230, 21, 203, 42]
# chet = []

# def chet_func(num:list) -> list:
#     for n in num:
#         if n % 2 == 0:
#             chet.append(n)
#     return chet
# print(chet_func(numders))


# numbers = [10, 230, 21, 203, 42]
# chet = list(filter(lambda num: num % 2 == 0, numbers))
# print(chet)


# numbers = [10, 230, 21, 203, 42]
# print(list(filter(lambda num: num % 2 == 0, numbers)))

# print(list(filter(lambda num: num % 2 == 0,[10, 230, 21, 203, 42])))


# num = [10, 230, 21, 203, 42]
# lst = []

# def mult_func(num_list: list) -> list:
#     for n in num:
#         lst.append(n * 2)
#     return lst 
# print(mult_func(num))


# print(list(map(lambda num: num * 2,[10, 230, 21, 203, 42] )))


# def square(n: int) -> int:
#    print(n * n)
# square(0)
# square(5)
# square(-3)

import time

def safe_login_password(login: str, password: str) -> str:
    password_file = open("login_password.txt", "a+", encoding="utf-8")
    if login and len(password) >= 8 and " " not in password:
        password_file.write(f"Логин: {login}, Пароль: {password}, {time.ctime()} \n")
    else:
        return "Неправильный логин или пароль"
    password_file.close()
    return "Логин и пароль сохранен"

print(safe_login_password("Islam", "12378980"))