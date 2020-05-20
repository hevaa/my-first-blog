from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_use_home_page(self):
        # Edith is an admin on a cool new online blog. She goes
        # to check out its homepage
        self.browser.get('http://127.0.0.1:8000/')

        # She notices the page title and header mention Heather
        self.assertIn('Heather\'s Blog', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Heather\'s Blog', header_text)

    def test_can_use_blog_page(self):
        # She is invited to view the page of blogs
        self.browser.get('http://127.0.0.1:8000/blog/')
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Heather\'s Blog', header_text)

    def test_can_use_cv_page(self):
        # She is invited to view the cv page
        self.browser.get('http://127.0.0.1:8000/cv/')
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Heather\'s Blog', header_text)

        # She goes to the edit page
        self.browser.get('http://127.0.0.1:8000/cv/edit/')

        # She is checks if the edit is there for skills
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "HTML" into a text box (Edith's hobby
        # is web-dev)
        inputbox.send_keys('HTML')

        # When she hits enter, the page updates, and now the page lists
        # "1: HTML" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: HTML')

        # There is still a text box inviting her to add another item. She
        # enters "DJANGO" (Edith is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('DJANGO')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: HTML')
        self.check_for_row_in_list_table('2: DJANGO')

        # Edith wonders whether the site will remember her list. Then she sees
        # that there is a back button

        # She clicks it - her list is still there on the main CV page.

        # Satisfied, she goes back to sleep
        self.fail('Finish the test!')

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  