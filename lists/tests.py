from django.urls import resolve  # takes URL returns view function
from django.test import TestCase
from .views import home_page

class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 2, 3)

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('')  # gets view function mapped to '/'
        self.assertEqual(found.func, home_page)
