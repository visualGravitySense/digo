from django.shortcuts import render
from .utils import *
from .models import *

def home(request):
    jobs = djinni()
    city = City.objects.get(name='Lviv')
    speciality = Speciality.objects.get(name='Python')
    v = Vacancy.objects.filter(city=city.id, speciality=speciality.id).values('url')
    url_list = [i['url'] for i in v]
    for job in jobs:
        if job['url'] not in url_list
            vacancy = Vacancy(city=city.id, speciality=speciality.id, url=job['url']
                                title=job['title'], description=job['descript'], company=job['company'])
            vacancy.save()

    return render(request, 'base.html', {'jobs': jobs})
