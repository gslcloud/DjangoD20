from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class AuthenticationTest(TestCase):
    fixtures = ['test_data.json']

    def test_login_url_resolves_correctly(self):
        url = reverse("login")
        self.assertEqual(url, "/login/")

    def test_user_authentication_success(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        response = self.client.post(reverse("login"), {"username": "testuser", "password": "testpassword"})
        self.assertEqual(response.status_code, 200)

    def test_user_authentication_failure_invalid_credentials(self):
        response = self.client.post(reverse("login"), {"username": "testuser", "password": "wrongpassword"})
        self.assertNotEqual(response.status_code, 200)

    def test_user_authentication_failure_user_not_found(self):
        response = self.client.post(reverse("login"), {"username": "nonexistentuser", "password": "testpassword"})
        self.assertNotEqual(response.status_code, 200)

    def test_user_authentication_failure_account_inactive(self):
        inactive_user = User.objects.create_user(username="inactiveuser", password="testpassword")
        inactive_user.is_active = False
        inactive_user.save()
        response = self.client.post(reverse("login"), {"username": "inactiveuser", "password": "testpassword"})
        self.assertNotEqual(response.status_code, 200)

    def test_user_authentication_failure_account_locked(self):
        locked_user = User.objects.create_user(username="lockeduser", password="testpassword")
        locked_user.is_active = False
        locked_user.save()
        response = self.client.post(reverse("login"), {"username": "lockeduser", "password": "testpassword"})
        self.assertNotEqual(response.status_code, 200)
