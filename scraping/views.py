from django.shortcuts import render
from scraping.utils import *
from scraping.models import *

def home(request):
    jobs = djinni()
#    jobs = []
#    jobs.extend(djinni())
#    jobs.extend(rabota())
#    jobs.extend(work())
    city = City.objects.get(name='Киев')
    speciality = Speciality.objects.get(name='Python')
    v = Vacancy.objects.filter(city=city, speciality=speciality).values('url')
    url_list = [i['url'] for i in v]
    for job in jobs:
        if job['href'] not in url_list:
            vacancy = Vacancy(city=city, speciality=speciality, url=job['href'], title=job['title'], description=job['descript'], company=job['company'])
            vacancy.save()

    return render(request, 'base.html', {'jobs': jobs})
