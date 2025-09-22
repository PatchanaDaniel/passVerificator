
from django.urls import reverse
from rest_framework.test import APITestCase

class PasswordCheckAPITest(APITestCase):
    def test_compromised_password(self):
        url = reverse('check-password') 
        data = {"password": "airriannaconner"}  
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["compromised"])

    def test_safe_password(self):
        url = reverse('check-password')
        data = {"password": "Ocerttfdgfe12@"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.data["compromised"])