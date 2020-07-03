from selenium import webdriver
import unittest
 #SO, we have a website and we want to test that we can do the following with it:
 #Update via a form that we have, which allows us to get this done.
 #Consider - static vs dynamic
 # Personal Statement -
 # Academic History - Add to it
 # Work History - Dynamic
 # Personal Achievements - Dynamic
 #We add to one, and then check on the page
class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	def tearDown(self):
		self.browser.quit()
	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Blog', self.browser.title)
		self.fail('FinishTest')
if __name__=='__main__':
	unittest.main(warnings='ignore')