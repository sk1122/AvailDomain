from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User

class AuthTest(TestCase):
	def test_get_register(self):
		response = self.client.get(reverse('register'))
		self.assertEqual(response.status_code, HTTPStatus.OK)
		self.assertContains(response, "<h1>Register</h1>", html=True)

	def test_post_register(self):
		response = self.client.post(reverse('register'), data={
			"username": "sk1122",
			"password1": "password@789",
			"password2": "password@789"
		})
		self.assertEqual(response.status_code, HTTPStatus.FOUND)
		self.assertEqual(response["Location"], reverse("login"))

	def test_get_login(self):
		response = self.client.get(reverse('login'))
		self.assertEqual(response.status_code, HTTPStatus.OK)
		self.assertContains(response, "<h1>Login</h1>", html=True)

	
	def test_post_login(self):
		response = self.client.post(reverse('register'), data={
			"username": "sk1122",
			"password1": "password@789",
			"password2": "password@789"
		})
		self.assertEqual(response.status_code, HTTPStatus.FOUND)

		res = self.client.post(reverse('login'), data={
			"username": "sk1122",
			"password": "password@789"
		})

		self.assertEqual(res.status_code, HTTPStatus.FOUND)
		self.assertEqual(res["Location"], reverse("domain_availablity"))

	def test_post_logout(self):
		response = self.client.post(reverse('register'), data={
			"username": "sk1122",
			"password1": "password@789",
			"password2": "password@789"
		})
		self.assertEqual(response.status_code, HTTPStatus.FOUND)

		res = self.client.post(reverse('login'), data={
			"username": "sk1122",
			"password": "password@789"
		})

		self.assertEqual(res.status_code, HTTPStatus.FOUND)
		self.assertEqual(res["Location"], reverse("domain_availablity"))

		res_logout = self.client.get(reverse('logout'))
		self.assertEqual(res_logout.status_code, HTTPStatus.FOUND)
		self.assertEqual(res_logout["Location"], reverse("login"))