import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):

    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
       
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}")

# 2. List all books in a library
def get_books_by_library(library_name):

    try:
        library = Library.objects.get(name=library_name)
       
        print(f"Books in {library_name}:")
        for book in library.books.all():
            print(f"- {book.title}")

    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):

    try:
        library = Library.objects.get(name=library_name)
        librarian = Library.objects.get(library=")
    
        print(f"Librarian for '{library_name}': {librarian.name}")

    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found")

    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")


