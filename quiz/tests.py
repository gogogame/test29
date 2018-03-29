from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from quiz.views import home_page

class HomePageTest(TestCase):

    def test_url_resolves_to_home_page_view(self):
        found = resolve('/quiz')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Quiz</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')
