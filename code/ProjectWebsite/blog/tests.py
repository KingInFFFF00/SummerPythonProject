from django.test import TestCase
from django.urls import resolve
from blog.views import post_list
class SmokeTest(TestCase):
	def test_url_resolve_to_home(self):
		found = resolve('/')
		self.assertEqual(found.func, post_list)
# Create your tests here.
