import json
from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [b for b in self.books if b.title != title]

    def display_books(self):
        for book in self.books:
            print(book)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([b.__dict__ for b in self.books], f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.books = [Book(**item) for item in data]