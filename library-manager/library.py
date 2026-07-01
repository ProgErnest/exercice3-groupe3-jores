

#This file explain the definition of the Library class and its methods.
class Library:
    def __init__(self, title):
        self.books = []
        self.name = title

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def list_books(self):
        for book in self.books:
            print(book.informations())
    
    def list_availables_books(self):
        for book in self.books:
            if book.is_available():
                print(book.informations())
    def list_unavailable_books(self):
        for book in self.books:
            if not book.is_available():
                print(book.informations())