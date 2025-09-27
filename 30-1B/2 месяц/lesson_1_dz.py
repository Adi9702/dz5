##1

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade 

#     def introduce(self):
#         print(f"Меня зовут {self.name}, мне {self.age}, моя оценка: {self.grade}")

# student1 = Student("Алия", 17, 95)
# student1.introduce()


##2 

# class Transport:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
#     def info(self):
#         print(f"Марка: {self.brand}, Cкорость: {self.speed} км/ч")

# class Car(Transport):
#     def drive(self):
#         print(f"{self.brand} едет по дороге со скоростью {self.speed} км/ч")

# class Airplane(Transport):
#     def fly(self):
#         print(f"{self.brand} летит со скоростью {self.speed} км/ч")

# car = Car("Toyota", 140)
# car.info()
# car.drive()


##3

# class User:
#     def __init__(self, username, age):
#         self.username = username
#         self.age = age

#     def is_adult(self, age):
#         if age <= 18:
#             self.is_adult = age
#         else:
#             print("False")

# class Admin(User):
#     def ban_user(self, other_user):
#         print(f"Админ {self.username} забанил пользователя {other_user.username}")

# admin = Admin("root", 25)
# user = User("guest", 16)
# admin.ban_user(user)

