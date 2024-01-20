from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AuthenticationTests(TestCase):
    def test_user_registration(self):
        """
        Test user registration functionality.
        """
        response = self.client.post(reverse('register'), data={
            'username': 'testuser',
            'password1': 'p@ssw0rd123',
            'password2': 'p@ssw0rd123'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

        user = User.objects.get(username='testuser')
        self.assertIsNotNone(user)
    
    def test_user_login(self):
        """
        Test user login functionality.
        """
        # Create a test user
        User.objects.create_user(username='testuser_login', password='p@ssw0rd123')

        # Log in the user
        response = self.client.post(reverse('login'), data={
            'username': 'testuser_login',
            'password': 'p@ssw0rd123'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        # Check that the user is logged in
        user = self.client.user
        self.assertTrue(user.is_authenticated)

    def test_user_logout(self):
        """
        Test user logout functionality.
        """
        # Create a test user
        user = User.objects.create_user(username='testuser_logout', password='p@ssw0rd123')

        # Log in the user
        self.client.force_login(user)

        # Log out the user
        response = self.client.post(reverse('logout'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

        # Check that the user is logged out
        user = self.client.user
        self.assertFalse(user.is_authenticated)
    
    def test_password_reset(self):
        """
        Test password reset functionality.
        """
        # Create a test user
        User.objects.create_user(username='testuser_pw_reset', password='p@ssw0rd123')

        # Request password reset
        response = self.client.post(reverse('password_reset'), data={
            'email': 'testuser_pw_reset@example.com',
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('password_reset_done'))
    
    def test_authentication_middleware(self):
        """
        Test authentication middleware settings.
        """
        # Create a test user
        user = User.objects.create_user(username='testuser_middleware', password='p@ssw0rd123')

        # Log in the user
        self.client.force_login(user)

        # Access a protected page
        response = self.client.get(reverse('profile'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profile Page')

        # Log out the user
        self.client.logout()

        # Access the protected page again
        response = self.client.get(reverse('profile'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))