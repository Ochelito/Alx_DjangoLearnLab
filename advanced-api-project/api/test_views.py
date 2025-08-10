from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import YourModel  # Replace with your actual model
from django.contrib.auth.models import User


class YourModelAPITests(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create test data
        self.item1 = YourModel.objects.create(name='Test Item 1', description='First item')
        self.item2 = YourModel.objects.create(name='Test Item 2', description='Second item')

        # Common URLs
        self.list_url = reverse('yourmodel-list')  # DRF router name or manual path
        self.detail_url = lambda pk: reverse('yourmodel-detail', args=[pk])

    def test_create_item(self):
        data = {'name': 'New Item', 'description': 'New description'}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(YourModel.objects.count(), 3)

    def test_read_item_list(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_read_item_detail(self):
        response = self.client.get(self.detail_url(self.item1.pk), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Item 1')

    def test_update_item(self):
        data = {'name': 'Updated Item', 'description': 'Updated description'}
        response = self.client.put(self.detail_url(self.item1.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item1.refresh_from_db()
        self.assertEqual(self.item1.name, 'Updated Item')

    def test_delete_item(self):
        response = self.client.delete(self.detail_url(self.item1.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(YourModel.objects.count(), 1)

    def test_filter_items(self):
        response = self.client.get(self.list_url, {'name': 'Test Item 1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Item 1')

    def test_search_items(self):
        response = self.client.get(self.list_url, {'search': 'First'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('First item' in item['description'] for item in response.data))

    def test_order_items(self):
        response = self.client.get(self.list_url, {'ordering': '-name'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        names = [item['name'] for item in response.data]
        self.assertEqual(names, sorted(names, reverse=True))

    def test_permission_enforcement(self):
        self.client.logout()
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
