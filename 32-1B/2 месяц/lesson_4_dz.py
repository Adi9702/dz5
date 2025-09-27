
class Item:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"Название: {self.name}, год: {self.year}"
    
    @classmethod
    return cls

class Book(Item):
    def __init__(self, name, year, author,pages):
        super().__init__(name, year)
        self.author = author
        self.__pages = pages

    @getattr
    def get_pages(self):
        return self.get_pages
    
    def __str__(self):
        super(). greet()


class Magazine (Item):
    def __init__(self, name, year, issue_number):
        super().__init__(name, year)
        self.issue_number = issue_number

 