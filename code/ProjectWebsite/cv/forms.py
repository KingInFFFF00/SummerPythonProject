from django import forms
from .models import EducationHistory,WorkHistory,PersonalAchievement

class EducationForm(forms.ModelForm):
	class Meta:
		model = EducationHistory
		fields = ('level','text')
class WorkForm(forms.ModelForm):
	class Meta:
		model = WorkHistory
		fields = ('payType','text','date')
class AchievementForm(forms.ModelForm):
	class Meta:
		model = PersonalAchievement
		fields = ('text',)