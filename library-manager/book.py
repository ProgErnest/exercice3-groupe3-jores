
#This file explain the definition of the Book class and its methods.

class Book:

    def __init__(self, title, author, genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.available = True

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_genre(self):
        return self.genre

    def is_available(self):
        return self.available

    def get_year(self):
        return self.year
    
    def set_title(self, title):
        self.title = title
        
    def set_author(self, author):
        self.author = author
        
    def set_genre(self, genre):
        self.genre = genre
        
    def set_year(self, year):
        self.year = year
        
    def borrow(self):
        self.available = False
        print(f"The book {self.title}-{self.author}({self.year}) was borrowed succesfally\n --\n Thank you for your fidelity\n Cordially, Jores WABO")
        
    def render(self):
        self.available =True
        print(f"The book {self.title}-{self.author}({self.year}) was returned succesfally\n --\n Thank you for your fidelity\n Cordially, Jores WABO")
    def informations(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nYear: {self.year}\nAvailable: {'Yes' if self.available else 'No'}"