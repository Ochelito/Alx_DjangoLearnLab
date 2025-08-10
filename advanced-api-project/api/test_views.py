from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status
from api.views import (
    BookListView, BookDetailView,
    BookCreateView, BookUpdateView, BookDeleteView
)
from api.models import Book
from django.contrib.auth import get_user_model

User = get_user_model()

class BookAPITests(TestCase):
    """Test suite for Book API endpoints using APIRequestFactory."""

    def setUp(self):
        """Set up test user, request factory, and a sample book."""
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create a book authored by the test user
        self.book = Book.objects.create(
            title='Test Book',
            author=self.user,
            publication_year=2021
        )

    def test_list_books(self):
        """Test retrieving list of books (GET /books/)."""
        request = self.factory.get('/books/')
        response = BookListView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_book(self):
        """Test retrieving a single book detail (GET /books/<pk>/)."""
        request = self.factory.get(f'/books/{self.book.pk}/')
        response = BookDetailView.as_view()(request, pk=self.book.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        """Test creating a new book (POST /books/create/)."""
        data = {
            'title': 'New Book',
            'author': self.user.pk,  # Primary key reference
            'publication_year': 2022
        }
        request = self.factory.post('/books/create/', data)
        force_authenticate(request, user=self.user)
        response = BookCreateView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        """Test updating an existing book (PUT /books/update/<pk>/)."""
        updated_data = {
            'title': 'Updated Book',
            'author': self.user.pk,
            'publication_year': 2021
        }
        request = self.factory.put(f'/books/update/{self.book.pk}/', updated_data)
        force_authenticate(request, user=self.user)
        response = BookUpdateView.as_view()(request, pk=self.book.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        """Test deleting a book (DELETE /books/delete/<pk>/)."""
        request = self.factory.delete(f'/books/delete/{self.book.pk}/')
        force_authenticate(request, user=self.user)
        response = BookDeleteView.as_view()(request, pk=self.book.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
