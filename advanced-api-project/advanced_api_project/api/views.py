from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import BasePermission 
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Custom permission to allow only the author to edit/delete the book
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed to any request
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # If the request method is not read-only, check if the user is the author of
            # Allow write access only to the author of the book
        return obj.author == request.user

#list all books - accessible to everyone(read only)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthorOrReadOnly]  # Allow unauthenticated users to view the list of books

     # Enable filtering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']  # Enable search by title and author's name
    ordering_fields = ['title', 'publication_year']  # Allow ordering by publication year and title
    ordering = ['title']  # Default ordering by title

# Get details of a specific book - accessible to everyone(read only)
class BookDetailView(generics.DetailAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthorOrReadOnly]  # Allow unauthenticated users to view book details

# Create a new book - accessible to authenticated users only
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]   # Allow only logged in users to create a book; author set automatically

    def perform_create(self, serializer): # Saves the book with the current user as the author
        serializer.save(author=self.request.user) # 

# Updates the book with the current user as the author
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]  # Allow only logged in users and authors to update a book

    def perform_update(self, serializer): # Saves the book with the current user as the author
        serializer.save() # Updates the book with the current user as the author

    def get_queryset(self):
        # Filters books to only include those published in the last 5 years
        five_years_ago = datetime.now().year - 5
        return self.queryset.filter(publication_year__gte=five_years_ago)

# Deletes a book - accessible to authenticated users only
class BookDeleteView(generics.DeleteAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]  # Allow only logged in users and authors to delete a book