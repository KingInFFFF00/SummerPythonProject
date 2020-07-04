from django.contrib import admin
from .models import EducationHistory, WorkHistory,PersonalAchievement
# Register your models here.
admin.site.register(EducationHistory)
admin.site.register(WorkHistory)
admin.site.register(PersonalAchievement)