from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class HomePageTest(TestCase):
    def setUp(self):
        # Create a user for testing authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_authenticated_user_navigation(self):
        # Test if the navigation bar displays correctly for an authenticated user
        self.client.force_login(self.user)
        response = self.client.get(reverse('home_page:home_page'))

        self.assertContains(response, 'Logout')
        self.assertNotContains(response, 'Login')
        self.assertNotContains(response, 'Register')

    def test_unauthenticated_user_navigation(self):
        # Test if the navigation bar displays correctly for an unauthenticated user
        response = self.client.get(reverse('home_page:home_page'))

        self.assertNotContains(response, 'Logout')
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Register')

    def test_redirect_to_login_for_unauthenticated_user(self):
        # Test if unauthenticated user accessing the home page renders successfully
        response = self.client.get(reverse('home_page:home_page'))
        self.assertEqual(response.status_code, 200)
