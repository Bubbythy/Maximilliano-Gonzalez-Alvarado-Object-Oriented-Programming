class LIBRARY:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):

        self.books.append(book)

    def add_users(self, user):
        self.users.append(user)

    def show_books(self):
        for book in self.books:
            print(book.show_book_info())

    def show_users(self):
            for user in self.users:
                print(user.show_user_info())

    def borrow_book(self, id_book, id_user):
         for book in self.books:
             if book.id == id_book:
                  for user in self.users:
                    if user.id == id_user:
                        if book.available == True:
                            book.available = False
                            print(f"Book {book.name} has been borrowed by user {user.name}.")
                        else:
                            print(f"Book {book.name} is not available for borrowing.")
    
    def return_book(self,id_book):
        for book in self.books:
                     if book.id == id_book:
                                if book.available == False:
                                    book.available = True
                                    print(f"Book {book.name} has been returned")
