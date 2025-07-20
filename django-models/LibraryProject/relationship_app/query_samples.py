import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):

    try:
        author = Author.objects.filter(author=author_name)
        books = author.books.all()

        print(f"\nBooks by {author.name}:")
        for book in books:
            print(f"- {book.title}")

    except Author.DoesNotExist:
        print(f"No author found with the name '{author_name}'.")

# 2. List all books in a library
def get_books_by_library(library_name):

    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()

        print(f"\nBooks in the {library.name} library:")
        for book in books:
            print(f"- {book.title}")

    except Library.DoesNotExist:
        print(f"No Library found with the name '{library_name}'.")

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):

    try:
        library = Library.objects.get(name=library_name)
        if hasattr(library, 'librarians'):
            print(f"\nLibrarian of {library.name} is {library.librarians.name}")

        else:
            print(f"\nNo Librarian assigned to '{library.name}' library")

    except Librarian.DoesNotExist:
        print(f"No Library found with the name '{library_name}'.")

