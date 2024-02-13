from django.test import TestCase
from django.urls import reverse


# Here we create our tests, to see if the content from 'home_page.html' is displayed correctly

class HomePageTest(TestCase):
    def test_home_page_content(self):
        response = self.client.get(reverse('home_page:home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_page/home_page.html')

        # Check for specific pieces of content
        self.assertContains(response, 'Navbar')  # checks if 'Navbar' is in the response
        self.assertContains(response, 'Home')  # checks if 'Home' is in the response
        self.assertContains(response, 'Account')  # checks if 'Account' is in the response
        self.assertContains(response, 'Transactions')  # checks if 'Transactions' is in the response
        self.assertContains(response, 'Create Transaction')  # checks if 'Create Transaction' is in the response
        self.assertContains(response, 'View Transactions')  # checks if 'View Transactions' is in the response
        self.assertContains(response, 'Search')  # checks if 'Search' is in the response
        self.assertContains(response, 'Personal Budget Tool')  # checks if 'Personal Budget Tool' is in the response

        # TODO Some test methods that we'll use for later tests

        # def test_home_page_redirects(self):
        #     # Test that the user is redirected to the login page if they're not authenticated
        #     response = self.client.get(reverse('home_page'), follow=True)
        #     self.assertRedirects(response, '/login/')  # replace '/login/' with the actual login page URL
        #
        # def test_home_page_form(self):
        #     # Test that the search form is included in the context data and works as expected
        #     response = self.client.get(reverse('home_page'))
        #     self.assertIn('form', response.context)  # checks if 'form' is in the context data
        #     form = response.context['form']
        #     self.assertTrue(form.is_valid())  # checks if the form validates user input correctly
