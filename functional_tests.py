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

        # She reads the static side of the page
        specialsection = self.browser.find_element_by_class_name('specialmsg')
        specialmsg = specialsection.find_element_by_tag_name('h1').text
        # She ensures there is a breakline as designed
        self.assertIn('Hey,\nI\'m Heather!', specialmsg)

        # She reads the contact information
        contactone = self.browser.find_element_by_class_name('contactone')
        contacts = contactone.find_elements_by_tag_name('p')
        self.assertIn('Email: someone@example.com', [contact.text for contact in contacts])
        self.assertIn('Number: 07123456789', [contact.text for contact in contacts])

        # She reads the current position information
        contacttwo = self.browser.find_element_by_class_name('contacttwo')
        position = contacttwo.find_elements_by_tag_name('p')
        self.assertIn('Current academia: University of Birmingham', [pos.text for pos in position])
        self.assertIn('Current year: Second Year', [pos.text for pos in position])
        self.assertIn('Current position: Degree Apprentice', [pos.text for pos in position])

    def test_can_use_cv_edit_page(self):
        # She goes to the edit page
        self.browser.get('http://127.0.0.1:8000/cv/edit/')

        # She is checks if she can edit her bio
        inputbox = self.browser.find_element_by_id('id_new_bio')

        ## she checks that the message already there is the current bio: making it easy to edit
        self.assertEqual(
	       inputbox.get_attribute('value'),
	        'this is a test bio'
	    )     

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

        ## she checks that the add placeholder has the correct message
        self.assertEqual(
	       inputbox.get_attribute('placeholder'),
	        'Enter a skill'
	    ) 

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

        ## she checks that the add placeholder has the correct message
        self.assertEqual(
	       inputbox.get_attribute('placeholder'),
	        'Enter a qualification'
	    ) 

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

        ## she checks that the add placeholder has the correct message
        self.assertEqual(
	       inputbox.get_attribute('placeholder'),
	        'Enter employment history'
	    ) 

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

        ## she checks that the add placeholder has the correct message
        self.assertEqual(
	       inputbox.get_attribute('placeholder'),
	        'Enter extracurricular item'
	    ) 

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