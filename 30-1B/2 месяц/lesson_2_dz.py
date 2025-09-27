##1

# class Shape:
#     def __init__(self, width=0, height=0, radius=0):
#         self.width = width
#         self.height = height 
#         self.radius = radius

#     def area(self):
#         rectangle_area = self.width * self.height
#         circle_area = 3.14159 * self.radius ** 2
#         print(f"Площадь прямоугольника: {rectangle_area}")
#         print(f"Площадь круга: {circle_area}")

# class Rectangle(Shape):
#     def area(self):
#          return self.width * self.height


# class Circle(Shape):
#      def area(self):
#          return 3.14159 * self.radius ** 2
     

# s = Rectangle(5, 8)
# print(f"Прямоугольник {s.area()}")

# p = Circle(radius=5)
# print(f"Круг {p.area()}")


##2 

class BankAccount:
    def __init__(self, balance, owner):
        self.__balance = balance
        self.__owner = owner 

    @property
    def balance(self):
        return self.__balance
    
    @ property
    def owner(self):
        return self.__owner

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Cумма для пополнения должна быть больше 0")

    def withdraw(self, amount):
        if amount <+ 0:
            self.balance < amount
        else:
            print("Недостаточно средств")

account = BankAccount("Bob", 1000)
account.deposit(500)
account.withdraw(300)

print(account.owner)
print(account.balance)
print(account.deposit)
print(account.withdraw)
