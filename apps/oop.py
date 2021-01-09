class Book():
    def __init__(self, name):
        self._name = name

    # getter
    @property
    def name(self):
        return self._name.title()

    # setter
    @name.setter
    def name(self, name):
        self._name = name.lower()

    

book = Book("MATH")

print(book.name)