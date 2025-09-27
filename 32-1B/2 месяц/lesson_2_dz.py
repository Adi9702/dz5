

class Animal:
    def __init__(self,name,age,weight):
        self.name = name
        self._age = age
        self.__weight = weight
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
            self._age = new_age

    @property
    def weight(self):
         return self.__weight
    
    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight
    
    def info(self):
        return f"Имя животного : {self.name}, Возраст {self._age}, Вес {self.__weight}"
    
    def sound(self):
        print("Звук животного")

class Lion(Animal):
    def sound(self):
        print("Арр!")


class Elephant(Animal):
    def sound(self):
        print("Тру-уу-у!")


class Parrot(Animal):
    def sound(self):
        print("Чирик-чирик!")

zoo = [
    Lion("Симба", 6, 200),
    Elephant("Дамбо", 5, 6000),
    Parrot("Гриша", 3, 2)
]

for v in zoo:
    print(v.info())  
    v.sound()
    
lion = Lion("Симба", 5, 230)
lion.weight = 400
print("Обновление веса Симбы:", lion.weight)

lion_zoo = zoo[0] 
print("Исходный вес Симбы:", lion_zoo.weight)



class Food(Animal):
    def __init__(self,name,age,weight):
        super().__init__(name,age,weight)

    def sound(self):
        print(f"Попугай {self.name} издает звук Чирик-чирик")

    def feed(self):
        print(f"Попугай {self.name} ест семечки")

    def move(self):
        print(f"Попугай {self.name} сидит в клетке")


w = Food("Гриша", 3, 2)
w.feed()
w.move()
w.sound()