from books import BOOK
from users import USER
from library import LIBRARY

library=LIBRARY()

#Adding a new book
id_book= input("Enter the book's ID: ")
name= input("Enter the book's name: ")
author= input("Enter the book's author: ")
editorial= input("Enter the book's editorial: ")

add_book= BOOK(id_book, name, author, editorial)

#Adding a new user
id_user= input("Enter the user's ID: ")    
username= input("Enter the user's name: ")

add_user= USER(id_user, username)


#Instances
book1 = BOOK("001", "Python for Dummies", "Juan Perez", "Santillan")
book2 = BOOK("002", "OOP fundamentals", "Diego Guzman", "E.A.")
user1= USER("001", "Maximiliano Gonzalez")

library.add_book(add_book)
library.add_users(add_user)


library.show_books()
library.show_users()
library.borrow_book(id_book, id_user)
library.return_book(id_book)
library.borrow_book(id_book, id_user)
library.borrow_book(id_book, id_user)
#The system must allow to register new books
#The system must allow to register new users
#The system must allow a boook to be borrowed by an user
#A book that has already been borrowed cannot be borrowed again until it is returned
#The system must allow a book to be returned and made available for borrowing again

from books import BOOK
from users import USER
from library import LIBRARY

library = LIBRARY()

#Catalog of books and users
library.add_book(BOOK("001", "Python for Dummies", "Juan Perez", "Santillan"))
library.add_book(BOOK("002", "OOP Fundamentals", "Miguel Ortega", "E.A."))
library.add_users(USER("001", "Fernanda Obregon"))

while True:
    print("\n--- LIBRARY MENU ---")
    print("1. Show books")
    print("2. Register a book")
    print("3. Register a user")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Exit")

    option = input("Choose an option: ")

    if option == "1":
        library.show_books()

    elif option == "2":
        id_book = input("Enter the book's ID: ")
        name = input("Enter the book's name: ")
        author = input("Enter the book's author: ")
        editorial = input("Enter the book's editorial: ")

        new_book = BOOK(id_book, name, author, editorial)
        library.add_book(new_book)
        print("Book registered.")

    elif option == "3":
        id_user = input("Enter the user's ID: ")
        username = input("Enter the user's name: ")

        new_user = USER(id_user, username)
        library.add_users(new_user)
        print("User registered.")

    elif option == "4":
        library.show_books()
        id_book = input("Enter the ID of the book to borrow: ")
        id_user = input("Enter your user ID: ")

        library.borrow_book(id_book, id_user)

    elif option == "5":
        id_book = input("Enter the ID of the book to return: ")
        library.return_book(id_book)

    elif option == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
