from rest_framework import generics
from rest_framework.viewsets import ModelViewSets
from .models import Book
from .serializers import BookSerializer


# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

