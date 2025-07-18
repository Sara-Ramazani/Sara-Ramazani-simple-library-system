from book import Book
from book_list import book_list
from library import Library

available_books = []

for book in book_list:
    title = book["title"]
    author = book["author"]
    new_book = Book(title, author)
    available_books.append(new_book)


my_library = Library(available_books)
my_library.show_available_books()
print("\n")


should_continue = True

while should_continue:
    user_input = input("What do you want to do? Type 'borrow' or return': ")
    if user_input == "borrow":
        borrow = input("What book do you want to borrow. Type the title: ")
        my_library.borrow_book(borrow)

    elif user_input == "return":
        return_book = input("What book do you want to return? Type the title:  ")
        my_library.return_book(return_book)