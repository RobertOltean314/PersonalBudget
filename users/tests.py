from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from users.models import Profile


class TestViews(TestCase):

    def setUp(self):
        # Setting up the test client, URLs, user model and a test user
        self.client = Client()
        self.register_url = reverse('users:register')
        self.logout_url = reverse('users:logout')
        self.profile_url = reverse('users:profile')
        self.update_profile_url = reverse('users:update_profile')
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(username='testuser', password='12345')

    def test_register_view_POST_creates_new_user(self):
        # Test to check if a new user is correctly created when valid data is posted to the register URL
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'password1': '12345',
            'password2': '12345'
        })
        # Asserting that the response status code is 200 (OK) and the user was created successfully
        self.assertEquals(response.status_code, 200)
        self.assertTrue(self.user_model.objects.filter(username='testuser').exists())

    def test_register_view_POST_invalid_form(self):
        # Test to check the behavior when invalid data is posted to the register URL
        response = self.client.post(self.register_url, {
            'username': '',
            'password1': '12345',
            'password2': '12345'
        })
        # Asserting that the response status code is 200 (OK) and the user was not created due to invalid data
        self.assertEquals(response.status_code, 200)
        self.assertFalse(self.user_model.objects.filter(username='').exists())

    def test_logout_view_POST_logs_out_user(self):
        # Test to check if the user is logged out successfully when the logout URL is posted to
        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.logout_url)
        # Asserting that the response status code is 302 (Redirect) and the user is no longer authenticated
        self.assertEquals(response.status_code, 302)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_profile_created_on_user_creation(self):
        # Test to check if a profile is created for each new user
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

    def test_profile_update_view_POST(self):
        # Test to check if the profile is updated successfully when valid data is posted
        updated_username = 'updated_testuser'
        response = self.client.post(self.update_profile_url, {
            'username': updated_username,
            'email': self.user.email
        })
        # Asserting that the response status code is 302 (Redirect) and the user's profile is updated
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user_model.objects.get(id=self.user.id).username, updated_username)

    def test_profile_update_view_POST_invalid_form(self):
        # Test to check the behavior when invalid data is posted to the profile update URL
        response = self.client.post(self.update_profile_url, {
            'username': '',  # invalid username
            'email': self.user.email
        })
        # Asserting that the response status code is 200 (OK) and the user's profile is not updated
        self.assertEquals(response.status_code, 200)
        self.assertNotEquals(self.user_model.objects.get(id=self.user.id).username, '')

    def test_profile_view_GET(self):
        # Test to check if the profile view displays user details correctly
        response = self.client.get(self.profile_url)
        # Asserting that the response status code is 200 (OK) and the correct user details are displayed
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.user.username.encode(), response.content)
