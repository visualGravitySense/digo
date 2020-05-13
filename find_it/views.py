from django.shortcuts import render
from scraping.utils import *
from scraping.models import *

def home(request):
    jobs = djinni()
    city = City.objects.get(name='Lviv')
    speciality = Speciality.objects.get(name='Python')
    v = Vacancy.objects.filter(city=City, speciality=Speciality).values('url')
    url_list = [i['url'] for i in v]
    for job in jobs:
        if job['href'] not in url_list:
            vacancy = Vacancy(city=City, speciality=Speciality, url=job['href'],
                                title=job['title'], desvription=job['descript'],
                                company=job['company'])
            vacancy.save()

    return render(request, 'base.html', {'jobs': jobs})
