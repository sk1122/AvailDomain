from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class APITest(APITestCase):
	def setUp(self):
		response = self.client.post(reverse('register'), data={
			"username": "sk1122",
			"password1": "password@789",
			"password2": "password@789"
		})

		res = self.client.post(reverse('login'), data={
			"username": "sk1122",
			"password": "password@789"
		})

	def test_api_check_domain_available(self):
		response = self.client.post(reverse('check_availablity'), data={
			"domain": "google.com"
		})

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_api_get_available_tlds(self):
		response = self.client.get(reverse('get_available_tlds'))

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertTrue(".com" in response.data["data"])

	def test_api_get_history(self):
		response = self.client.get(reverse('get_history'))

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertTrue("data" in response.data)