from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('academic.html',views.academic, name='academic'),
path('achievement.html',views.achievement, name='achievement'),
path('personal.html',views.personal, name='personal'),
path('work.html',views.work, name='work'),
]