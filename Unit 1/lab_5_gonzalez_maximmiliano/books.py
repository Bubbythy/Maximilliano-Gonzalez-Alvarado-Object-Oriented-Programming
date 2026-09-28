class BOOK:
    def __init__(self, id_book, name, author, editorial):
        self.id= id_book
        self.name = name
        self. author = author
        self.editorial = editorial
        self.available = True
    def show_book_info(self):
        return f"{self.id} - {self.name} - {self.author}"

        