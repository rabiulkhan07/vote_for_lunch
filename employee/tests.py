from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Employee

class EmployeeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a test user
        self.user = Employee.objects.create(
            fullname='Rabiul Khan T',
            email='rk@test.com',
            employeeId='E001',
            presentAddress='Dhaka',
            contactNo='09876543',
            jwt_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZXhwIjoxNjk3OTg0NjY4LCJpYXQiOjE2OTc5ODEwNjh9.4_EacF-lORDaPpG4pItQXjPUz6f1Ex3b28xEHpG49y0'  # Provide a sample token for testing
        )
        self.user.set_password('rabit')
        self.user.save()

    def test_registration(self):
        url = reverse('register')
        data = {
            'employeeId': 'E001',
            'fullname': 'Rabiul Khan T',
            'email': 'rk@test.com',
            'presentAddress': 'Dhaka',
            'contactNo': '09876543',
            'password': 'rabit'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        url = reverse('login')
        data = {'employeeId': 'E001', 'password': 'rabit'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('jwt' in response.data)

    def test_get_all_employees(self):
        url = reverse('employee')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_single_employee(self):
        url = reverse('employee', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_employee(self):
        url = reverse('employee', args=[self.user.id])
        data = {'fullname': 'Updated Name'}  # Provide updated data
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['fullname'], 'Updated Name')

    def test_delete_employee(self):
        url = reverse('employee', args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_employee_profile(self):
        url = reverse('activeuser')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        url = reverse('logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_profile(self):
        url = reverse('activeuser')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

    def test_unauthenticated_logout(self):
        url = reverse('logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 401)