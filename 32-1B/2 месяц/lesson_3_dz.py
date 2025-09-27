
class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def __str__(self):
        return f"Книга: {self.title} ({self.year}), автор: {self.author}"

    def __lt__(self, other):
        return self.year < other.year


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def read(self, book):
        print(f"{self.name} читает {book.title}")

    @staticmethod
    def library_rules():
        print("Библиотеке нельзя шуметь")


class PremiumUser(User):
    def __init__(self, name, age, membership_level="Gold", **kwargs):
        super().__init__(name, age, **kwargs)
        self.membership_level = membership_level

    @classmethod
    def create_premium(cls, name, age):
        return cls(name, age, membership_level="Gold")


class Librarian(User):
    def __init__(self,name, age, position="Библиотекарь", **kwargs):
        super().__init__(name, age, **kwargs)
        self.position = position
    
    def manage_book(self, book, action):
        print(f"{self.name} {action} книгу {book.title}")


class SuperUser(PremiumUser, Librarian):
    def __init__(self, name, age, membership_level="Gold", position="Главный"):
        super().__init__(name,age,membership_level=membership_level, position=position)
        PremiumUser.__init__(self, name, age, membership_level)
        Librarian.__init__(self, name, age, position)

    def work(self):
        print(f"{self._name} главный Библиотекарь")
        PremiumUser.work(self)
        Librarian.work(self)


book1 = Book("Маленький принц", 1943, "Антуан де Сент-Экзюпери")
book2 = Book("Гордость и предубеждение", 1813, "Джейн Остин")
u = User("Алиса", 25)
p = PremiumUser.create_premium("Боб", 25)
l = Librarian("Макс", 30, "Главный")
s = SuperUser("Алеша", 40, "Gold", "Главный")


u.read(book1)
p.read(book2)
s.read(book1)
print(book1 < book2)

