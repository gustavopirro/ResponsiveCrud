from django.urls import reverse
from django.contrib.auth.models import User
from api.models import Post
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status


class APITestCase(APITestCase):
    def setUp(self):
        self.unauthenticated_client = APIClient()

    def test_get_posts_unauthenticated(self):
        response = self.unauthenticated_client.get(reverse('api:api_post_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_post_unauthenticated(self):
        user = User.objects.create(username='test_user', password='test_password')
        Post.objects.create(title='test', content='test_content', author=user)
        response = self.unauthenticated_client.get(reverse('api:api_post_detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_post_unauthenticated(self):
        response = self.unauthenticated_client.post(reverse('api:api_post_list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)