from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
import jwt
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model

User = get_user_model()

class TestRestaurantAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.restaurant_create_url = reverse('restaurant-create')
        self.restaurant_list_url = reverse('restaurant-list')
        self.menu_create_url = reverse('menu-create')
        self.vote_create_url = reverse('vote-create')

        self.user_data = {
            "fullname": "John Doe",
            "email": "johndoe@example.com",
            "employeeId": "1001",
            "password": "password",
            "presentAddress": "123 Main St",
            "contactNo": "123-456-7890",
        }
        
        self.restaurant_data = {
            "name": "Best Restaurant",
        }

        self.menu_data = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "restaurant": 1,
            "created_by": 1,
            "image": "http://localhost:8000/media/menus/350128793_949169933085762_3422294038878444981_n_W3qoOTm.jpeg",
        }

    def create_and_login_user(self):
        # Register and login a user
        self.client.post(reverse('register'), self.user_data)
        login_data = {
            "employeeId": "1001",
            "password": "password",
        }
        login_response = self.client.post(reverse('login'), login_data)
        token = login_response.data['jwt']
        return token

    def test_create_restaurant(self):
        # Create and authenticate a user
        token = self.create_and_login_user()

        # Create a restaurant
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.post(self.restaurant_create_url, self.restaurant_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_restaurants(self):
        # Create and authenticate a user
        token = self.create_and_login_user()

        # List restaurants
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(self.restaurant_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_vote(self):
        token = self.create_and_login_user()

        # List restaurants
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        # Create a restaurant for testing
        response = self.client.post(self.restaurant_create_url, self.restaurant_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Create a menu for the restaurant
        response = self.client.post(self.menu_create_url, self.menu_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Create a vote for the menu
        vote_data = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "restaurant": 1,  # Ensure this matches the restaurant created above
            "employee": 1,  # Provide a valid user ID
            "choice": 1  # 1 for "Yes"
        }
        response = self.client.post(self.vote_create_url, vote_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

