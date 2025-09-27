# print(20 ** 20) # степень 
# print(9 // 2) # Деление без остатка 
# print(30 % 4) # показывает остаток 


# нельзя сложить int и str - выйдет ошибка, точно также и наоборот 
# Если перед целым числом или перед строкой поставить int и str то оно переобразуется 
# 

# name = "python " + "developer" # - это чложение строк "Конкатинация"

# print(20 + int("30")) # - это пример где мы переобразовали строку на целое число 
# print("python" + str(3)) # - это где мы преобразовали целое число на строку 

# True = 1 
# False = 0 

# print( 20 + True) # - в данном случаи мы получим ответ 21, так как True=1 поэтому посчитало 20+1=21 
# print(20 + False) # - в данном случаи ответ мы получим 20, так как False=0 поэтому посчитало 20+0=20


# Тема на 12/06/25 - if , else , elif - продолжение условии


# num1 = 20
# num2 = 50 

# if num1 > num2 :
#     print(num1)
# else:
#     print(num2)


# number = 453223429

# if number % 2 == 0:
#     print(number, "четное")
# else:
#     print(number, "нечетное")


# Imput - по умолчанию использует str, исходя из этого если нужно то его нужно будет преобраховать в int (по мере неоюходимости)

# num1 = int(input("Введите первое число: "))
# operator = input("+, -, *, /: ")
# num2 = int(input("Введите второе число: "))

# if operator == "+":
#     print("Ответ", num1 + num2)
# elif operator == "-":
#     print("Ответ", num1 - num2)
# elif operator == "*":
#     print("Ответ", num1 * num2)
# elif operator == "/":
#     print("Ответ", num1 / num2)
# else: 
#     print("Введите корректное значение")


# # or , and 

# login = "geeks"
# password = "geeks2025"

# user_login = input("login: ")
# user_Password = input("Password: ")

# if login == user_login and user_Password == Password:
#     print("Welcome")
# else: 
#     print("error")

# print(int("578"))
# print(int(float(str(192))))
# print("Calling " + str(911) "abc" + "xyz")

# print(float(173) + 5) 
# print(str(193.000000000001))

# print(589+932.901)

# num1a = 589
# num2b = 932.901
# num3c = "Hello world"
# num4d = "892.01"

# print(num3c + str(num1a), num4d , str(num2b) + str(num1a) , str(num1a + float(num4d)))


# def func(a, b=2, c=3):
#     return a + b + c 
# print(func(1))
