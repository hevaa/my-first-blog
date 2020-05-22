from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text, table):
        table = self.browser.find_element_by_id(table)
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

    def test_can_use_cv_edit_page(self):
        # She goes to the edit page
        self.browser.get('http://127.0.0.1:8000/cv/edit/')

        # She is checks if she can edit her bio
        inputbox = self.browser.find_element_by_id('id_new_bio')     

        # She types into a text box (Edith's hobby
        # is web-dev)
        inputbox.send_keys('I am a web developer')

        # Edith wonders whether the site will remember this. Then she sees
        # that there is a back button

        # She clicks it - her bio is still there on the main CV page.

    def test_cv_add_skill_page(self):
        # She goes to the edit page
        self.browser.get('http://127.0.0.1:8000/cv/edit/add')

        # She is checks if she can add a skill
        inputbox = self.browser.find_element_by_id('id_new_skill')     

        # She types into a text box (Edith's hobby
        # is web-dev)
        inputbox.send_keys('HTML')

        # When she hits enter, the page updates, and now the page lists
        # "•: HTML" as an item in a table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('• HTML', 'id_skills_table')

        # There is still a text box inviting her to add another item. She
        # enters "DJANGO" (Edith is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_skill')
        inputbox.send_keys('DJANGO')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('• HTML', 'id_skills_table')
        self.check_for_row_in_list_table('• DJANGO', 'id_skills_table')

    def test_cv_add_qual_page(self):
        # She goes to the edit page
        self.browser.get('http://127.0.0.1:8000/cv/edit/add')

        # She is checks if she can add her qualifications
        inputbox = self.browser.find_element_by_id('id_new_qual')     

        # She types into a text box
        inputbox.send_keys('GCSE')

        # When she hits enter, the page updates
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('• GCSE', 'id_qual_table')

        # There is still a text box inviting her to add another item.
        inputbox = self.browser.find_element_by_id('id_new_qual')
        inputbox.send_keys('A LEVEL')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('• GCSE', 'id_qual_table')
        self.check_for_row_in_list_table('• A LEVEL', 'id_qual_table')

    def test_cv_add_employ_page(self):
        # She goes to the edit page
        self.browser.get('http://127.0.0.1:8000/cv/edit/add')

        # She is checks if she can add her employment history
        inputbox = self.browser.find_element_by_id('id_new_employ')     

        # She types into a text box
        inputbox.send_keys('VODAFONE')

        # When she hits enter, the page updates
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('• VODAFONE', 'id_employ_table')

        # There is still a text box inviting her to add another item.
        inputbox = self.browser.find_element_by_id('id_new_employ')
        inputbox.send_keys('BBC')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('• VODAFONE', 'id_employ_table')
        self.check_for_row_in_list_table('• BBC', 'id_employ_table')

    def test_cv_add_extra_page(self):
        # She goes to the edit page
        self.browser.get('http://127.0.0.1:8000/cv/edit/add')

        # She is checks if she can add extracurricular
        inputbox = self.browser.find_element_by_id('id_new_extra')     

        # She types into a text box
        inputbox.send_keys('FISHING')

        # When she hits enter, the page updates
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('• FISHING', 'id_extra_table')

        # There is still a text box inviting her to add another item.
        inputbox = self.browser.find_element_by_id('id_new_extra')
        inputbox.send_keys('GAMING')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('• FISHING', 'id_extra_table')
        self.check_for_row_in_list_table('• GAMING', 'id_extra_table')


        # Edith wonders whether the site will remember her lists. Then she sees
        # that there is a back button

        # She clicks it - her list is still there on the main CV page.

        # Satisfied, she goes back to sleep
        self.fail('Finish the test!')

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  