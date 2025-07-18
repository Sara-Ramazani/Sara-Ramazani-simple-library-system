class Library:

    def __init__(self, book_list):
        self.available_books = book_list
        self.borrowed_books = []

    def show_available_books(self):
        print("Here is a list of all the available books:")
        for book in self.available_books:
            print(book)


    def borrow_book(self, title):
        for book in self.available_books:
            if book.title == title:
                self.available_books.remove(book)
                self.borrowed_books.append(book)
                print(f'You borrowed the book "{title}"')
                return

        for book in self.borrowed_books:
            if book.title == title:
                print(f'Sorry, the book "{title}" is already borrowed.')
                return

        print(f'Sorry, the book "{title}" is not available in this library.')



    def return_book(self, title):
        for book in self.borrowed_books:
            if book.title ==  title:
                self.borrowed_books.remove(book)
                self.available_books.append(book)
                print(f'You\'ve returned the book "{title}". Thank you!')
                return

        for book in self.available_books:
            if book.title == title:
                print(f'The book "{title}" was not borrowed.')
                return

        print(f'The book "{title}" was not borrowed from this library.')



