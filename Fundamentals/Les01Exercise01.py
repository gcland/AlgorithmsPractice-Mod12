# Problem statement: Build a simple library data structure that allows visitors to easily find books by book category.
# -------------------------------------------------------------------------------------------------
# 
# List is ordered, algorithm will have to run through entire list of books to check for category
# Dictionary is not necessarily ordered and allows user to directly pull up a list of books that apply to the given critera:

class Library:
    def __init__(self):
        self.shelves = {}

    def add_book(self, category, book):
        if category not in self.shelves:
            self.shelves[category] = [book]
        else:
            self.shelves[category].append(book)
    
    def get_books(self, category):
        return self.shelves.get(category, f"No books found within '{category}' category")
    
library = Library()

library.add_book("Fiction", "Book1")
library.add_book("Fiction", "Book2")
library.add_book("Non-Fiction", "Book3")


print(library.get_books("Fiction")) #Output: [Book1, Book2]
print(library.get_books("Non-Fiction")) #Output: [Book3]
print(library.get_books("Romance")) #Output: 'No books found within 'Romance' category

