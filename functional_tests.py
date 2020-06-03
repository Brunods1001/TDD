from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a To-Do item right away.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Buy feathers" into a text box.
        inputbox.send_keys('Buy peacock feathers')

        # When he hits enter, the page updates, and now the page lists
        # "1: Buy feathers" as an item in a to-do list.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # There is still a text box inviting him to add another item. He enters "Use
        # feathers to make a fly"
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on his list.

        # He wonders whether the site will remember his list. Then he sees that the
        # site has generated a unique URL - his to-do list is still there.

        # Satisfied, he goes to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
