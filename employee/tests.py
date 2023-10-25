from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
import jwt
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model

User = get_user_model()

class TestEmployeeAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.employee_url = reverse('activeuser')


        self.user_data = {
            "fullname": "Rabiul Khan",
            "email": "rabiul@test.com",
            "employeeId": "1001",
            "password": "password",
            "presentAddress": "Magura",
            "contactNo": "01737954190",
        }

    def test_register_user(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_user(self):
        # Register a user
        self.client.post(self.register_url, self.user_data)
        login_data = {
            "employeeId": "1001",
            "password": "password",
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('jwt' in response.data)

    def test_authenticated_user_profile(self):
        # Register and login a user
        self.client.post(self.register_url, self.user_data)
        login_data = {
            "employeeId": "1001",
            "password": "password",
        }
        login_response = self.client.post(self.login_url, login_data)
        token = login_response.data['jwt']

        # Use the JWT token to access the authenticated user profile
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(self.employee_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['fullname'], self.user_data['fullname'])

    

