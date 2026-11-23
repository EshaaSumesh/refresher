class Book :
    def __init__(self,title,author,status):
        self.title=title
        self.author=author
        self.status=True
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)

    def borrow(self,title):
        for book in self.books:
            if book.title==title and book.status==True:
                book.status=False
                print(f"you have borrowed {book.title} by {book.author}")
            elif book.title==title and book.status==False:
                print(f"Sorry , {book.title} is already borrowed")
            else:
                 print(f"no book titled {title}")

    def return_book(self,title):
        for book in self.books:
            if book.title==title and book.status==False:
                book.status=True
                print(f"you have returned {book.title} by {book.author}")
            elif book.title==title and book.status==True:
                print(f"{book.title} is not borrowed")
            else:
                 print(f"no book titled {title}")

    def show_books(self):

        for book in self.books:
            if book.status==True:
                print(f"{book.title} by {book.author} is available")
            else:
                print(f"{book.title} by {book.author} is borrowed")


lib=Library()
lib.add_book(Book("Python 101","Rao",True))
lib.add_book(Book("To Kill a Mockingbird","Harper Lee",True))
lib.add_book(Book("1984","George Orwell",True))
lib.show_books()
lib.borrow("Python 101")
lib.show_books()
lib.return_book("Python 101")
lib.show_books()

