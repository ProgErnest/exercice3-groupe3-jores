

#This file explain the definition of the Library class and its methods.
class Library:
    def __init__(self, title):
        self.books = []
        self.name = title

    def add_book(self, book):
        self.books.append(book)
        print(f"The book {book.title}-{book.author}({book.year}) was added succesfally\n" 
              + "\nThank you for your fidelity\n\n\nCordially, Jores WABO\n\n")

    def remove_book(self, book):
        self.books.remove(book)

    def list_books(self):
        if self.books:
            print("The books in the library are : ")
            for book in self.books:
                print(f"{book.informations()}\n\n")
        else:
            print("No books in the library.")

    def list_availables_books(self):
        for book in self.books:
            if book.is_available():
                print(book.informations())
    def list_unavailable_books(self):
        for book in self.books:
            if not book.is_available():
                print(book.informations())

    def find_book_by_title(self, title):
        for book in self.books:
            if book.get_title() == title:
                return book
        return None
    