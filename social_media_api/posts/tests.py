from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class PostCommentAPITestCase(APITestCase):

    def setUp(self):
        # Create users
        self.user1 = User.objects.create_user(username='user1', password='pass123')
        self.user2 = User.objects.create_user(username='user2', password='pass123')

        # Authenticate user1
        self.client = APIClient()
        self.client.force_authenticate(user=self.user1)

        # Create initial post
        self.post = Post.objects.create(author=self.user1, title='Hello', content='World')

        # Create initial comment
        self.comment = Comment.objects.create(post=self.post, author=self.user1, content='Nice post!')

    def test_post_creation(self):
        url = reverse('posts-list')
        data = {'title': 'New Post', 'content': 'Content here'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['author'], self.user1.username)

    def test_post_update_by_author(self):
        url = reverse('posts-detail', args=[self.post.id])
        data = {'title': 'Updated Title'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Title')

    def test_post_update_by_non_author(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse('posts-detail', args=[self.post.id])
        data = {'title': 'Hacked'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_comment_creation(self):
        url = reverse('comments-list')
        data = {'post': self.post.id, 'content': 'Another comment'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['author'], self.user1.username)

    def test_post_pagination(self):
        # Create additional posts
        for i in range(15):
            Post.objects.create(author=self.user1, title=f'Post {i}', content='Test')
        url = reverse('posts-list') + '?page=2'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)
