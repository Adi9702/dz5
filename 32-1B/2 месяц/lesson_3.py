
# магический метод - это специальные методы которые начинаются и заканчиваются двумя подчёркиваниями:
# __init__ - конструктор, вызывается когда создается объект 
# __str__ - строковое представление. Определяет, что выводится при print().
# __add__ - оператор + Позволяет задать поведение сложения объектов

# class Point:
#     def __init__ (self, x, y):
#         self.x = x 
#         self.y = y 

#     def __str__ (self):
#         return f"Point({self.x} {self.y})"
    
#     def __add__ (self, other):
#         return Point(self.x + other.x, self.y + other.y)
    
# p1 = Point(2,3)
# p2 = Point(5,7)
# print(p1)
# p3 = p1 + p2 
# print(p3)


# Это магический метод __lt__ (больше или меньше)
# class Person:
#     def __init__(self, age):
#         self.age = age

#     def __lt__(self, other):
#         return self.age < other.age

# p1 = Person(25)
# p2 = Person(30)

# print(p1 < p2)  # True, Python вызывает p1.__lt__(p2)


# Статичные методы - это метод класса, который не зависит от конкретного объекта.Он не использует self и не использует данные экземпляра, но логически связан с классом. Его можно вызывать через класс или через объект, но обычно через класс.
# метод self - то ссылка на текущий объект. Используется, когда метод работает с данными конкретного объект 
# метод cls — это ссылка на сам класс, а не на объект. Используется, когда метод работает с атрибутами класса или создаёт новые объекты. Объявляется через декоратор @classmethod.

# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b

# print(Math.add(5, 10))


# Множественное наследование - это когда один класс наследует сразу от двух или более классов. То есть новый класс может получить свойства и методы нескольких родительских классов одновременно. 
# класс objekt - это птолок самый-самый родительский класс (все классы наследуются от него)
# алмазная проблема - то когда не ясно какой метод или свойства данный класс наследует от какого класса
# mro - для проверки последовательности классов, чтобф решить алмазную проблему  Class.__mro__ или Class.mro()
# kwargs = keyword arguments (именованные аргументы). Это способ передать любое количество аргументов в формате ключ=значение в функцию. Внутри функции **kwargs представляется как словарь (dict).
# Когда использовать ** kwargs Если неизвестно заранее, сколько именованных аргументов будет. Для гибкости функций и классов. Очень часто в декораторах и при работе с библиотеками (Flask, Django, Pandas, etc.).


# class Person:
#     species =  "Homo speiens"
# 
#     def __init__(self, name):
#         self.name = name
# 
#     @classmethod
#     def create_anonymous(cls):
#         return cls("Anonymous")
# 
# print(Person.species)
# 
# p = Person.create_anonymous()
# print(p.name)



# class A:
#     def method_a(self):
#         print("Method A")
# 
# class B:
#     def method_b(self):
#         print("Method B")
# 
# class C(A, B):
#     def mehtod_c(self):
#         print("Method C")
# 
# c = C()
# c.method_a()
# c.method_b()
# c.mehtod_c()
# 
# print(C.__mro__)

# class A:
#     def greet(self):
#         print("A")

# class B(A):
#     def greet(self):
#         print("B")
#         super().greet()

# class C(A):
#     def greet(self):
#         print("C")
#         super().greet()

# class D(B,C):
#     def greet(self):
#         print("D")
#         # super().greet()
        
# d = D()
# d.greet()

# print(D.__mro__)



class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.salary = salary

    def work(self):
        print(f"{self._name} выполняет свои обязанности")

    def __str__(self):
        return f"Сотрудник: {self._name}, salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        print(f"{self._name} управляет командой из {self.team_size} человек")


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def work(self):
        print(f"{self._name} пишет код на {self.language}")


class TechManage(Manager, Developer):
    def __init__(self, name, salary, team_size, language):
        Manager.__init__(self, name, salary, team_size)
        Developer.__init__(self, name, salary, language)

    def work(self):
        print(f"{self._name} управляет командой и пишет код")
        Manager.work(self)
        Developer.work(self)


class Utils:
    @staticmethod
    def bonus(salary, percent):
        return salary * percent / 100

    @classmethod
    def description(cls):
        print(f"{cls.__name__} — класс для расчета бонусов сотрудников")


mrg = Manager("Alice", 5000, 5)
dev = Developer("Bob", 5000, "Java")
# tech_mgr = TechManage("Mark", 6000, 6, "Python")

mrg.work()
dev.work()
# tech_mgr.work()

employees = [mrg, dev]
for e in employees:
    e.work()

print(mrg)
print(dev)
# print(tech_mgr)





