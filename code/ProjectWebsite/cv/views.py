from django.shortcuts import render

def index(request):
	return render(request, 'cv/index.html', {})
def academic(request):
	return render(request, 'cv/academic.html',{})
def achievement(request):
	return render(request, 'cv/achievement.html',{})
def work(request):
	return render(request, 'cv/work.html',{})
def personal(request):
	return render(request, 'cv/personal.html',{})
