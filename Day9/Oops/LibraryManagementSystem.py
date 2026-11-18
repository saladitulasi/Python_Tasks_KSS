class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size

    def display_ebook(self):
        self.display()
        print("File Size:", self.file_size, "MB")


e = EBook("Python Programming", "John", 500, 10)

print("EBook Details:")
e.display_ebook()