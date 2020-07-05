from django.shortcuts import render, redirect
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
	if request.method=="POST":
		form = EducationForm(request.POST)
		if form.is_valid():
			educationHistory = form.save(commit=False)
			educationHistory.save()
			return redirect('academic')
	else:
		form = EducationForm()
	return render(request, 'cv/education_edit.html',{'form':form})
def work_edit(request):
	if request.method=="POST":
		form = WorkForm(request.POST)
		if form.is_valid():
			workHistory = form.save(commit=False)
			workHistory.save()
			return redirect('work')
	else:
		form = WorkForm()
	return render(request, 'cv/work_edit.html',{'form':form})
def personal_edit(request):
	if request.method=="POST":
		form = AchievementForm(request.POST)
		if form.is_valid():
			personalAchievement = form.save(commit=False)
			personalAchievement.save()
			return redirect('achievement')
	else:
		form = AchievementForm()
	return render(request, 'cv/personal_edit.html',{'form':form})