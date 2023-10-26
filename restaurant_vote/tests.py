from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
import jwt
from datetime import datetime, timedelta
from io import BytesIO
from PIL import Image
from .models import Vote
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
            "fullname": "Riaz ",
            "email": "riaz@test.com",
            "employeeId": "1001",
            "password": "password",
            "presentAddress": "Magura",
            "contactNo": "435713467788",
        }
        
        self.restaurant_data = {
            "name": "Best Restaurant",
        }

        self.menu_data = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "restaurant": "be360080-0c09-4ab2-adcc-7751b208a68a",
            "created_by": "62a77302-363f-4965-b20d-3b9c9173ce5b",
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

    #menu create
    def test_create_menu_with_image(self):
        # Create and authenticate a user
        token = self.create_and_login_user()

        # Create a restaurant
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.post(self.restaurant_create_url, self.restaurant_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Create a menu for the restaurant with an image
        restaurant_id = response.data.get('id')
        image = Image.new('RGB', (100, 100))
        image_io = BytesIO()
        image.save(image_io, format='JPEG')
        menu_image = SimpleUploadedFile("restaurant_vote/test_media/test.jpeg", image_io.getvalue())
        #menu_image = SimpleUploadedFile("restaurant_vote/test_media/test.jpeg", b"file_content")
        print(menu_image)
        menu_data = {
            "id":"550b2e42-dcd8-48a9-be65-d48c3f3f26e2",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "restaurant": "be360080-0c09-4ab2-adcc-7751b208a68a",
            "created_by": "62a77302-363f-4965-b20d-3b9c9173ce5b",
            "image": menu_image,
        }

        response = self.client.post(self.menu_create_url, menu_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_vote(self):
        # Create and authenticate a user
        token = self.create_and_login_user()

        # Create a restaurant
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.post(self.restaurant_create_url, self.restaurant_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Create a menu for the restaurant
        restaurant_id = response.data.get('id')
        menu_data = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "restaurant": "be360080-0c09-4ab2-adcc-7751b208a68a",
            "created_by": "62a77302-363f-4965-b20d-3b9c9173ce5b",
            "image": "http://localhost:8000/media/menus/350128793_949169933085762_3422294038878444981_n_W3qoOTm.jpeg",
        }

        response = self.client.post(self.menu_create_url, menu_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Create a vote for the menu
        menu_id = response.data.get('id')
        vote_data = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "restaurant": "be360080-0c09-4ab2-adcc-7751b208a68a",
            "employee": "62a77302-363f-4965-b20d-3b9c9173ce5b",
            "choice": 1,
        }

        response = self.client.post(self.vote_create_url, vote_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_menus(self):
        # Create and authenticate a user
        token = self.create_and_login_user()

        # List menus
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(self.menu_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vote_for_menu(self):
        # Create and authenticate a user
        token = self.create_and_login_user()

        # Create a menu
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.post(self.restaurant_create_url, self.restaurant_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        restaurant_id = response.data.get('id')

        menu_image = SimpleUploadedFile("test_image.jpg", b"file_content")
        menu_data = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "restaurant": restaurant_id,
            "created_by": self.user_data['employeeId'],
            "image": menu_image,
        }
        response = self.client.post(self.menu_create_url, menu_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        menu_id = response.data.get('id')

        # Vote for the menu
        vote_data = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "restaurant": restaurant_id,
            "employee": self.user_data['employeeId'],
            "choice": 1,  # Assuming 1 represents 'Yes'
        }
        response = self.client.post(self.vote_create_url, vote_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the vote was recorded
        vote = Vote.objects.get(menu=menu_id, employee=self.user_data['employeeId'])
        self.assertIsNotNone(vote)

    def test_calculate_result(self):
        # Create and authenticate a user
        token = self.create_and_login_user()

        # Create a restaurant
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.post(self.restaurant_create_url, self.restaurant_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Create a menu for the restaurant
        restaurant_id = response.data.get('id')
        menu_image = SimpleUploadedFile("test_image.jpg", b"file_content")

        menu_data = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "restaurant": restaurant_id,
            "created_by": self.user_data['employeeId'],
            "image": menu_image,
        }

        response = self.client.post(self.menu_create_url, menu_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        menu_id = response.data.get('id')

        # Vote for the menu
        vote_data = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "restaurant": restaurant_id,
            "employee": self.user_data['employeeId'],
            "choice": 1,  # Assuming 1 represents 'Yes'
        }
        response = self.client.post(self.vote_create_url, vote_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Calculate the result
        response = self.client.get(self.calculate_result_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the result matches the expected format
        self.assertTrue('result' in response.data)

    