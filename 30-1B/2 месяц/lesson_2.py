## Инкопцуляция / гетеро , сетеро? / декоратор / пайнофизм


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#         else:
#             print("Недостаточно средств")

#     def get_balance(self):
#         return self.__balance

# account = BankAccount("Bob", 1000)
# account.deposit(500)
# account.withdraw(300)

# print(account.get_balance())
# print(account.owner)
# print(account.__balance)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p = Person("Bob", 20)
# p.age = -50



# def add(x = 10, y = 5):
#     return x + y

# print(add())

# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.__age = age

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, value):
#         if value >= 0:
#             self.__age = value
#         else:
#             print("Возраст не может быть отрицательным!")

# p = Person("bob", 23)
# print(p.age)
# 
# p.age = 24
# print(p.age)  
# 
# print(p._Person__age)
#



# class Rectangle:
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height

#     @property
#     def width(self):
#         return self.__width
    
#     @width.setter
#     def width(self, area):
#         if area >= 0:
#             self.__width = area
#         else:
#             print(width * height)
        
#     @property
#     def height(self):
#         return self.__height
    
#     @height.setter
#     def height(self, area):
#         if area >= 0:
#             self.__height = area
#         else:
#             print(width * height)

# s = Rectangle(5, 8)
# print(s.width)
# print(s.height)



# Создай базовый класс Shape с методом area()

# Создай 2 подкласса:

# Circle(radius)

# Rectangle(width, height)

# Каждый подкласс должен переопределить метод area()

# Создай список из фигур разных типов

# Пройдись по списку и выведи площадь каждой фигуры через shape.area()'



class Shape:
    def __init__(self, width, height, radius):
        self.width = width
        self.height = height 
        ra