"""
URL configuration for advanced_api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface URL
    path('books/', BookListView.as_view(), name='book-list'),  # List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Get details of a specific book
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create a new book
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),  # Update an existing book
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),  # Delete a book
]
# This code sets up the URL routing for the advanced_api_project, linking URLs to their respective
# views for handling book-related operations such as listing, creating, updating, and deleting books.
# The admin URL is also included for managing the models through the Django admin interface.
