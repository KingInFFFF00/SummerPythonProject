from django.test import TestCase
from django.urls import resolve
from blog.views import post_list
from django.http import HttpRequest
class SmokeTest(TestCase):
	def test_url_resolve_to_home(self):
		found = resolve('/')
		self.assertEqual(found.func, post_list)
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = post_list(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn("<title>David's Summer Project Blog</title>", html)
		self.assertTrue(html.endswith('</html>')) 
# Create your tests here.
