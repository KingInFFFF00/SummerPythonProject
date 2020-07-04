from django.db import models
from django.conf import settings
# Create your models here.
class EducationHistory(models.Model):
	level = models.CharField(max_length=30)
	text = models.TextField()
class WorkHistory(models.Model):
	text = models.TextField()
	payType = models.TextField() #Will be either PAID or UNPAID
	date = models.DateTimeField(blank=True, null=True)
class PersonalAchievement(models.Model):
	text = models.TextField()