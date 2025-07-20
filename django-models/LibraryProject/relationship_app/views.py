from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# Create your views here.
def list_books(request):
    books = Book.objects.all() 
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        # Optimize DB access: prefetch related books and authors
        return Library.objects.prefetch_related('books__author')


        





"""1. Django Views and URL Configuration
mandatory
Objective: Develop proficiency in creating both function-based and class-based views in Django, and configuring URL patterns to handle web requests effectively. This task will help you understand different ways to define views and manage URL routing in Django.

Task Description:
In your existing Django project, enhance the relationship_app by adding new views that display information about books and libraries. Implement both function-based and class-based views to handle these displays and configure the URL patterns to route these views correctly.

Steps:
Implement Function-based View:

Create a function-based view in relationship_app/views.py that lists all books stored in the database.
This view should render a simple text list of book titles and their authors.
Implement Class-based View:

Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.
Utilize Django’s ListView or DetailView to structure this class-based view.
Configure URL Patterns:

Edit relationship_app/urls.py to include URL patterns that route to the newly created views. Make sure to link both the function-based and class-based views.
Create Templates (Optional for Display):

For a more structured output, using the code below as templates for each view to render the information in HTML format instead of plain text.
Template for Listing Books (list_books.html):
This template will be used by the function-based view to display a list of all books.

Template for Displaying Library Details (library_detail.html):
This template will be used by the class-based view to show details of a specific library, including all books available in that library.
"""
