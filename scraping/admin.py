from django.contrib import admin
from .models import *

class VacancyAdmin(admin.ModelAdmin):
    class Meta:
        model = Vacancy
    list_display = ('title', 'url', 'city', 'speciality', 'timestamp')

admin.site.register(City)
admin.site.register(Vacancy)
admin.site.register(Speciality)
admin.site.register(Site)
admin.site.register(Url)
