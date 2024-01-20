from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class UserCreationTestCase(TestCase):
    def test_create_user_success(self):
        # Test user creation
        username = "test_user"
        password = "test_password"
        email = "test@example.com"

        user = User.objects.create_user(username=username, password=password, email=email)
        self.assertEqual(user.username, username, "Username doesn't match")
        self.assertEqual(user.email, email, "Email doesn't match")
        self.assertFalse(user.is_staff, "User should not have staff status")
        self.assertFalse(user.is_superuser, "User should not have superuser status")

        # Test user login
        user = authenticate(username=username, password=password)
        self.assertIsNotNone(user, "User should be authenticated")
        login_success = login(self.client.request(), user)
        self.assertTrue(login_success, "User login failed")

        # Test user logout
        logout_success = logout(self.client.request())
        self.assertTrue(logout_success, "User logout failed")

    def test_create_user_empty_username(self):
        # Test user creation with empty username
        password = "test_password"
        email = "test@example.com"

        with self.assertRaises(ValueError):
            User.objects.create_user(username="", password=password, email=email)

    def test_create_user_empty_password(self):
        # Test user creation with empty password
        username = "test_user"
        email = "test@example.com"

        with self.assertRaises(ValueError):
            User.objects.create_user(username=username, password="", email=email)

    def test_create_user_invalid_email(self):
        # Test user creation with invalid email
        username = "test_user"
        password = "test_password"
        email = "invalid_email"

        with self.assertRaises(ValueError):
            User.objects.create_user(username=username, password=password, email=email)
