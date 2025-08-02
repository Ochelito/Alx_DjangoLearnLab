from rest_framework import generics
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser #Imports the built-in permission classes
from .permissions import IsAuthorOrReadOnly # Import the custom permission class

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, IsAuthorOrReadOnly]

# BookViewSet using DRF's ModelViewSet
# This viewset automatically provides CRUD operations for the Book model
# and enforces access control using both built-in and custom permissions
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, IsAuthorOrReadOnly]
