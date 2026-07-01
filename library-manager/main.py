#In this files the main functionnalities are made and we execute the program here

import library
import book

my_library = library.Library("-----------Jores Book Library--------")

print(f"Welcome to my new Library :\n {my_library.name}\n")

while True:
    print("Here are the available menu commands:\n")
    print("1. Add a book\n2. Remove a book\n3. List all books\n4. List available books\n" +
        "5. List unavailable books\n6. Find a book by title\n7. Borrow a book\n8. Return a book\n9. Exit")
    
    command = int(input("Please enter the number of the command you want to execute:  "))
    if command == 1:
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        genre = input("Enter the genre of the book: ")
        year = input("Enter the year of the book: ")
        new_book = book.Book(title, author, genre, year)
        my_library.add_book(new_book)
        input("Press Enter to continue...")
              
    elif command == 2:
        title = input("Enter the title of the book you want to remove: ")
        book = my_library.find_book_by_title(title)
        if book:
            my_library.remove_book(book)
            print(f"The book {book.title}-{book.author}({book.year}) was removed succesfally\n --\n Thank you for your fidelity\n Cordially, Jores WABO")
        else:
            print("Book not found.")
        input("Press Enter to continue...")
        
    elif command == 3:
        my_library.list_books()
        input("Press Enter to continue...")
        
    elif command == 4:
        my_library.list_availables_books()
        input("Press Enter to continue...")
        
    elif command == 5:
        my_library.list_unavailable_books()
        input("Press Enter to continue...")
        
    elif command == 6:
        book_title = input("Enter the title of the book you want to find: ")
        book = my_library.find_book_by_title(book_title)
        if book:
            print(book.informations())
        else:
            print("Book not found.")
        input("Press Enter to continue...")
        
    elif command == 7:
        book_title = input("Enter the title of the book you want to borrow: ")
        book = my_library.find_book_by_title(book_title)
        if book:
            book.borrow()
        else:
            print("Book not found.")
        input("Press Enter to continue...")
            
    elif command == 8:
        book_title = input("Enter the title of the book you want to return: ")
        book = my_library.find_book_by_title(book_title)
        if book:
            book.return_book()
        else:
            print("Book not found.")
        input("Press Enter to continue...")
        
    elif command == 9:
        print("\n\nExiting the program...")
        break
    else:
        print("Invalid command. Please try again.")
        input("Press Enter to continue...")
        

print(f"\n\n\nThank you for using {my_library.name}. Goodbye!")