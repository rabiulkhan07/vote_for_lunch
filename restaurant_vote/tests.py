from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Restaurant

User = get_user_model()

class RestaurantCreateViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            employeeId='1001',  # Replace with your user data
            password='rabiul',   # Replace with the password
        )

        # Generate a valid JWT token
        refresh = RefreshToken.for_user(self.user)
        self.jwt_token = str(refresh.access_token)

    def test_create_restaurant_authenticated(self):
        url = reverse('restaurant-create')  # Replace with the actual URL name
        data = {
            "name": "New Restaurant",  # Replace with your restaurant data
        }

        # Set the JWT token as a cookie in the client
        self.client.cookies['jwt'] = self.jwt_token

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify that the restaurant is created in the database
        self.assertEqual(Restaurant.objects.count(), 1)
        restaurant = Restaurant.objects.first()
        self.assertEqual(restaurant.name, "New Restaurant")

    def test_create_restaurant_unauthenticated(self):
        url = reverse('restaurant-create')  # Replace with the actual URL name
        data = {
            "name": "New Restaurant",  # Replace with your restaurant data
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Verify that the restaurant is not created in the database
        self.assertEqual(Restaurant.objects.count(), 0)

