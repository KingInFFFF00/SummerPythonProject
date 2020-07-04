from django.shortcuts import render
from .models import EducationHistory, WorkHistory,PersonalAchievement
from .forms import *
def index(request):
	return render(request, 'cv/index.html', {})
def academic(request):
	educations = EducationHistory.objects.all()
	return render(request, 'cv/academic.html',{'educations':educations})
def achievement(request):
	personals = PersonalAchievement.objects.all()
	return render(request, 'cv/achievement.html',{'personals':personals})
def work(request):
	paidWorks = WorkHistory.objects.filter(payType="PAID")
	unpaidWorks = WorkHistory.objects.filter(payType="UNPAID")
	return render(request, 'cv/work.html',{'paidWorks':paidWorks, 'unpaidWorks':unpaidWorks})
def personal(request):
	return render(request, 'cv/personal.html',{})
def education_edit(request):
	form = EducationForm()
	return render(request, 'cv/education_edit.html',{'form':form})
def work_edit(request):
	form = WorkForm()
	return render(request, 'cv/work_edit.html',{'form':form})
def personal_edit(request):
	form = AchievementForm()
	return render(request, 'cv/personal_edit.html',{'form':form})