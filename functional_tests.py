from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Safari()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # James heard about a new online to-do app. He goes to checkout its
        # homepage.
        self.browser.get('http://127.0.0.1:8000')

        # He notices the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # He is invited to enter a To-Do item right away.

        # He types "Buy feathers" into a text box.

        # When he hits enter, the page updates, and now the page lists
        # "1: Buy feathers" as an item in a to-do list.

        # There is still a text box inviting him to add another item. He enters "Use
        # feathers to make a fly"

        # The page updates again, and now shows both items on his list.

        # He wonders whether the site will remember his list. Then he sees that the
        # site has generated a unique URL - his to-do list is still there.

        # Satisfied, he goes to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
