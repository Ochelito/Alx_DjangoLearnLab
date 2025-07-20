import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):

    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)

        return books
    
    except Author.DoesNotExist:
        return []

# 2. List all books in a library
def get_books_by_library(library_name):

    try:
        library = Library.objects.get(name=library_name)
       
        return library.books.all()
    
    except Library.DoesNotExist:
        return []

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):

    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)

        return librarian

    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None
