from django.test import SimpleTestCase,TestCase
from django.urls import reverse

# Create your tests here.

class Model_with_django(TestCase):
    """
    verify status code, With name of the route instead of the hard coded path 'home'
    """

    def test_home_route(self):
        expected = 200
        url = reverse('home')
        response= self.client.get(url)
        actual = response.status_code
        self.assertEquals(expected,actual)


class Mytest(TestCase):
    """
    I examine that if made more than one class
    """
    def test_template_home(self):
        """
        Check for the right path to the desired page
        """
        url = reverse('home')
        response = self.client.get(url)
        actual= 'home.html'
        self.assertTemplateUsed(response,actual)
        
