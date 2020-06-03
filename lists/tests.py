from django.http import HttpRequest
from django.urls import resolve  # takes URL returns view function
from django.test import TestCase
from .views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  # gets view function mapped to '/'
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        '''
        This tests constants <-- not good.
        :return:
        '''
        request = HttpRequest()  # django sees this when browsers request page
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

    def test_uses_home_template(self):
        '''
        Tests implementation <-- Good.
        :return:
        '''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post(
            '/',
            data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'lists/home.html')
