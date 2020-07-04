from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('academic.html',views.academic, name='academic'),
path('achievement.html',views.achievement, name='achievement'),
path('personal.html',views.personal, name='personal'),
path('work.html',views.work, name='work'),
path('education_edit.html',views.education_edit, name='education_edit'),
path('work_edit.html',views.work_edit, name='work_edit'),
path('personal_edit.html',views.personal_edit, name='personal_edit'),
]