from django.contrib import admin
from .models import *

# Register your models here.

class VacancyAdmin(admin.ModelAdmin):
    class Meta:
        model = Vacancy
    list_display = ('title', 'url', 'city', 'specialty', 'timestamp')

admin.site.register(City)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Specialty)
admin.site.register(Site)
admin.site.register(Url)

"""
from django.contrib import admin
from .models import *

class VacancyAdnim(admin.ModelAdmin):
    class Meta:
        model = Vacancy
    list_display = ('title', 'url', 'city', 'specialty', 'timestamp')

admin.site.register(City)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Specialty)
admin.site.register(Site)
admin.site.register(Url)
admin.site.register(Error)
"""