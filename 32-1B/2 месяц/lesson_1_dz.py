
class Animal:
    def __init__ (self, name, age):
        self.name = name 
        self.age = age 

    def make_sound(self):
        print(f"{self.name} издает звук")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        print(f"Собака {self.name} лает: Гав-гав")

p = Animal("Хаски", "5")
p.make_sound()

s = Dog("Бульдок", 5, "Французкий")
s.make_sound()




class Puppy(Dog):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
    
    def make_sound(self):
        print(f"Щенок {self.name} пищит: Пи-пи")

r = Puppy("Хаски", 3, "Сибирский")
r.make_sound()




class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} мяу")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} гав-гав")

class Elephant(Animal):
    def make_sound(self):
        print(f"{self.name} Тру-у-у")

dog = Dog("Bob", 2)
cat = Cat("Alice", 3)
elephant = Elephant("Dambo", 5)
dog.make_sound()
cat.make_sound()
elephant.make_sound()
