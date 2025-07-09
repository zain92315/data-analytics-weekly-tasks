from book import Book
from library import Library

lib = Library()
lib.load_from_file("data.json")
lib.add_book(Book("1984", "George Orwell", "1234567890"))
lib.display_books()
lib.save_to_file("data.json")