from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from api.models import Book
from django.urls import reverse

User = get_user_model()

class BookAPITests(APITestCase):
    """Test suite for Book API endpoints using APITestCase."""

    def setUp(self):
        """Set up test user and a sample book."""
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create a book authored by the test user
        self.book = Book.objects.create(
            title='Test Book',
            author=self.user,
            publication_year=2021
        )

        # Authenticated client
        self.client.login(username='testuser', password='testpass')

    def test_list_books(self):
        """Test retrieving list of books (GET /books/)."""
        url = reverse('book-list')  # Name from your urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_book(self):
        """Test retrieving a single book detail (GET /books/<pk>/)."""
        url = reverse('book-detail', args=[self.book.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        """Test creating a new book (POST /books/create/)."""
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2022
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        """Test updating an existing book (PUT /books/update/<pk>/)."""
        url = reverse('book-update', args=[self.book.pk])
        updated_data = {
            'title': 'Updated Book',
            'publication_year': 2021
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        """Test deleting a book (DELETE /books/delete/<pk>/)."""
        url = reverse('book-delete', args=[self.book.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)