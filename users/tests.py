from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


# Create your tests here.
class UserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test_user@test.ru")
        self.client.force_authenticate(user=self.user)

    def test_user_register(self):
        url = reverse("users:register")
        data = {"email": "admin@admin.ru", "password": "test_passw"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
