from django.test import TestCase
from django.urls import resolve
from blog.views import post_list
from django.http import HttpRequest
class SmokeTest(TestCase):
	def test_new_work_item_works(self):
		self.browser
# Create your tests here.
