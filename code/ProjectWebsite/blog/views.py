from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'blog/index.html', {})
def academic(request):
	return render(request, 'blog/academic.html',{})
def achievement(request):
	return render(request, 'blog/achievement.html',{})
def work(request):
	return render(request, 'blog/work.html',{})
def personal(request):
	return render(request, 'blog/personal.html',{})