from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import random
 #SO, we have a website and we want to test that we can do the following with it:
 #Update via a form that we have, which allows us to get this done.
 #Consider - static vs dynamic
 # Personal Statement -
 # Academic History - Add to it
 # Work History - Dynamic
 # Personal Achievements - Dynamic
 #We add to one, and then check on the page
 #THAT will work out. Work on it after tea
class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	def tearDown(self):
		self.browser.quit()
	def test_can_access_blog_page(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Blog', self.browser.title)
	def test_can_access_work_page(self):
		self.browser.get('http://localhost:8000/cv/work.html')
		self.assertIn('Work', self.browser.title)
	def test_can_access_work_form(self):
		self.browser.get('http://localhost:8000/cv/work_edit.html')
		self.assertIn('Form', self.browser.title)
	def test_can_put_stuff_in_work_form_and_submit(self):
		self.browser.get('http://localhost:8000/cv/work_edit.html')
		self.assertIn('Form', self.browser.title)
		randomint = random.randint(1000,9999)
		textinputbox = self.browser.find_element_by_id('id_text')
		textinputbox.send_keys("New Text Item "+str(randomint))
		paytypeinputbox = self.browser.find_element_by_id('id_payType')
		paytypeinputbox.send_keys("PAID")
		dateinputbox = self.browser.find_element_by_id('id_date')
		dateinputbox.send_keys("11/22/2020")
		submitbutton = self.browser.find_element_by_class_name("save")
		submitbutton.click()
		self.assertIn('Work',self.browser.title)
		source = self.browser.page_source
		self.assertIn("<li>New Text Item "+str(randomint)+"</li>", source)
	def test_can_put_content_in_personal_form_and_submit(self):
		self.browser.get('http://localhost:8000/cv/personal_edit.html')
		self.assertIn('Form', self.browser.title)
		randomint = random.randint(1000,9999)
		textinputbox = self.browser.find_element_by_id('id_text')
		textinputbox.send_keys("New Personal Item Test "+str(randomint))
		submitbutton = self.browser.find_element_by_class_name("save")
		submitbutton.click()
		source = self.browser.page_source
		self.assertIn("<li>New Personal Item Test "+str(randomint)+"</li>", source)
	def test_can_put_content_in_academic_form_and_submit(self):
		self.browser.get('http://localhost:8000/cv/education_edit.html')
		self.assertIn('Form', self.browser.title)
		randomint = random.randint(1000,9999)
		textinputbox = self.browser.find_element_by_id('id_text')
		textinputbox.send_keys("New Academic Item Test "+str(randomint))
		levelinputbox = self.browser.find_element_by_id('id_level')
		levelinputbox.send_keys("New Academic Level Test")
		submitbutton = self.browser.find_element_by_class_name("save")
		submitbutton.click()
		source = self.browser.page_source
		self.assertIn("<li>New Academic Item Test "+str(randomint)+"</li>", source)
	def test_can_fail_when_missing_content(self): #On Fail, return to page
		self.browser.get('http://localhost:8000/cv/education_edit.html')
		self.assertIn('Form', self.browser.title)
		submitbutton = self.browser.find_element_by_class_name("save")
		submitbutton.click()
		self.assertIn('Form', self.browser.title)
if __name__=='__main__':
	unittest.main(warnings='ignore')